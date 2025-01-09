from constant.column_name import MOBILE

def mobile_clean(df):
    """
    Paramètres:
    df (pd.DataFrame): Le DataFrame contenant la colonne 'Mobile'.

    Retourne:
    pd.DataFrame: Le DataFrame avec les numéros de mobile nettoyés.
    """
        
    dic_mobile_character = {
        '\.0$': '', 
        ' ': '', 
        '\.': '',
        '\-': '',
        '\_': '',
        '\(': '',
        '\)': '',
        '\,': '', 
        'nan': '',
        '/':''
    }
    dic_mobile_number = {
        '^06': '+336',
        '^07': '+337',
        '^6': '+336',
        '^7': '+337',
        '^33': '+33',
    }
    # Remove special characters
    df[MOBILE] = df[MOBILE].astype(str).replace(dic_mobile_character, regex=True)
    
    # international format
    df[MOBILE] = df[MOBILE].astype(str).replace(dic_mobile_number, regex=True)
    
    df.loc[df[MOBILE].duplicated(), [MOBILE]] = ''

   
    df['Mobile Other'] = df[MOBILE].copy()
    # Remove inside [MOBILE] values not starting with +336 or +337
    df[MOBILE] = df[MOBILE].apply(lambda x: x if str(x).startswith('+336') or str(x).startswith('+337') else None)
    # Inside [Mobile Other] column, remove values starting with +336 or +337
    df['Mobile Other'] = df['Mobile Other'].apply(lambda x: None if str(x).startswith('+336') or str(x).startswith('+337') else x)

    return df
