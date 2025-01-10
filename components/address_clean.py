import pandas as pd

from constant.column_name import ADRESSE, CP


def address_clean(df):


  """
  Extrait le numéro de rue et le nom de la rue d'une colonne 'Adresse' dans un DataFrame pandas.
  Paramètres:
  df (pd.DataFrame): Le DataFrame contenant la colonne 'Adresse'.
  Retourne:
  pd.DataFrame: Le DataFrame avec deux nouvelles colonnes 'Numéro Rue' et 'Nom Rue'.
  """

  dic_zip_code = {
    '\.0$': '', 
    'nan': '',
  }

  df[CP] = df[CP].astype(str).replace(dic_zip_code, regex=True)

  # prepare data
  df[ADRESSE] = df[ADRESSE].fillna('')
  df[ADRESSE] = df[ADRESSE].str.replace(',','')
  df[ADRESSE] = df[ADRESSE].str.strip()

  # extract street number and street name
  # dans ADRESSE on extrait ce qui commence par des lettres, chiffres et caractères speciaux et on met dans 'Numéro Rue'
  df['Numéro Rue'] = df[ADRESSE].str.extract(r'^(\S+)')
  df['Nom Rue'] = df[ADRESSE].str.extract(r'(?<=\s)([\w\s]+)')
  
  df.drop(ADRESSE, axis=1, inplace=True)
  return df