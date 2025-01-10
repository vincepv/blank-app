from constant.column_name import PAYS

def clean_country(df):
    if PAYS not in df.columns:
        df[PAYS] = ''

    # Remplace 'France' et 'FRANCE' par 'FR'
    df.loc[df[PAYS].isin(['France', 'FRANCE']), PAYS] = 'FR'
    
    return df