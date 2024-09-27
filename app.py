import streamlit as st
import pandas as pd


from components.rename_column import rename_column
from components.mobile_clean import mobile_clean
from components.clean_character import clean_character
from components.category_clean import category_clean
from components.clean_country import clean_country
from components.split_file import split_file
from components.address_clean import address_clean

st.title("DigitaleBox CRM: nettoyage de fichiers CSV")
st.write(
    "Uploader fichier CSV : encodage utf8, délimiteur virgule"
)


uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.write("Voici un aperçu du fichier chargé :")
    st.dataframe(df.head())
    
    # Nettoyage du fichier (par exemple, suppression des lignes avec des valeurs manquantes)
    if st.button("Nettoyer le fichier"):

        df = clean_character(df)
        df = rename_column(df)
        df = mobile_clean(df)
        df = clean_country(df)
        df = category_clean(df)
        df = address_clean(df)

        cleaned_csv = df.to_csv(index=False).encode('utf-8')
        
        # Bouton pour télécharger le fichier CSV nettoyé
        st.download_button(
            label="Télécharger le fichier CSV nettoyé",
            data=cleaned_csv,
            file_name='fichier_nettoye.csv',
            mime='text/csv'
        )
