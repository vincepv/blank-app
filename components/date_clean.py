import pandas as pd
from constant.column_name import DATE_NAISSANCE

def date_clean (df):

  #clean false date format
  if DATE_NAISSANCE not in df:
    df.insert(loc=0, column=DATE_NAISSANCE,value = '')

  clean_value = {
    '^00':'01',
    '/00/':'/01/',
  }
  df[DATE_NAISSANCE] = df[DATE_NAISSANCE].replace(clean_value,regex=True)

  # convert in: yyyy-mm-dd
  df[DATE_NAISSANCE] = pd.to_datetime(
    df[DATE_NAISSANCE],
    errors='ignore',
    dayfirst=True,)

  return df