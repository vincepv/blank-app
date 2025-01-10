from constant.column_name import EMAIL


def email_clean(df):
  if EMAIL not in df.columns:
    df[EMAIL] = ''

  df[EMAIL] = df[EMAIL].fillna('')
  df[EMAIL] = df[EMAIL].str.lower()
  # email keep first 
  df[EMAIL] = df[EMAIL].str.extract(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')


  df = df.drop_duplicates(subset=[EMAIL])

  
  return df