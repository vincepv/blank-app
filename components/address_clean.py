import pandas as pd


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

  df['Code postal'] = df['Code postal'].astype(str).replace(dic_zip_code, regex=True)

  df['Adresse'] = df['Adresse'].fillna('')
  df[['Numéro Rue', 'Nom Rue']] = df['Adresse'].str.extract(r'(\d+\w*)\s+(.*)', expand=True)
  df['Numéro Rue'] = df['Numéro Rue'].fillna('')
  df['Nom Rue'] = df.apply(lambda row: row['Adresse'] if row['Numéro Rue'] == '' else row['Nom Rue'], axis=1)
  
  df.drop('Adresse', axis=1, inplace=True)
  return df