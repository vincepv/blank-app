def clean_country(df):
  df.loc[df['Pays'] == 'France', 'Pays'] = 'FR'
  return df
