from constant.column_name import PRENOM

def firstname_clean(df):

  df[PRENOM] = df[PRENOM].str.extract(r'^(\S+)')

  return df