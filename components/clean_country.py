from constant.column_name import PAYS

def clean_country(df):
  df.loc[df[PAYS] == 'France', 'Pays'] = 'FR'
  return df
