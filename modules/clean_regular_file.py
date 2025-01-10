import streamlit as st
import pandas as pd

from components.rename_column import rename_column
from components.mobile_clean import mobile_clean
from components.clean_character import clean_character
from components.category_create import category_create
from components.clean_country import clean_country
from components.split_file import split_file
from components.address_clean import address_clean
from components.date_clean import date_clean

def clean_regular_file():
  uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv", key="clean_regular_file")

  if uploaded_file is not None:
      df = pd.read_csv(uploaded_file)
      
      st.write("Voici un aperçu du fichier chargé :")
      st.dataframe(df.head())
      
      
      if st.button("Nettoyer le fichier"):

          # cleaning logic
          df = clean_character(df)
          df = rename_column(df)

          # business logic
          df = date_clean(df)
          df = mobile_clean(df)
          df = clean_country(df)
          df = category_create(df)
          df = address_clean(df)
          # prenom keep first
          # email keep first

          split_file(df)
        
      