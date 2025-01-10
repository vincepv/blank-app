import streamlit as st

from modules.migration import migration
from modules.clean_regular_file import clean_regular_file

st.title("DigitaleBox: nettoyage de fichiers CSV")
st.write(
    "Uploader fichier CSV : encodage utf8, délimiteur virgule. "
)
st.divider()
st.header("Script Migration")
st.write ("Le CSV doit contenir les colonnes suivantes : First Name,Last Name,Email,Gender,Category,Date of Birth,Keywords, Notes, Mobile, Zip, Street Address, City,Country")
migration()


st.divider()
st.header("Script nettoyage CSV")
st.write ("Le CSV doit contenir les colonnes suivantes : First Name,Last Name,Email,Gender,Category,Date of Birth,Keywords, Notes, Mobile, Zip, Street Address, City,Country")
clean_regular_file()