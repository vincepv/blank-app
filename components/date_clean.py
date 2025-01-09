import pandas as pd

def date_clean (my_dataframe):
  DATE_OF_BIRTH = 'Date'

  df = my_dataframe.copy()

  #clean false date format
  
  if DATE_OF_BIRTH not in df:
        df.insert(loc=0, column=DATE_OF_BIRTH,value = '')

  clean_value = {
    '^00':'01',
    '/00/':'/01/',
  }

  df['clean_date'] = df[DATE_OF_BIRTH].replace(clean_value,regex=True)

  # convert in: yyyy-mm-dd
  df['clean_date'] = pd.to_datetime(
    df['clean_date'],
    errors='ignore',
    dayfirst=True,)

  return df['clean_date']