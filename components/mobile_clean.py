from constant.column_name import MOBILE

def mobile_clean(df):
    """
    Paramètres:
    df (pd.DataFrame): Le DataFrame contenant la colonne 'Mobile'.

    Retourne:
    pd.DataFrame: Le DataFrame avec les numéros de mobile nettoyés.
    """

    if MOBILE not in df:
        df.insert(loc=0, column=MOBILE,value = '')

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
 
    # Keep only mobile numbers starting with +336 or +337, remove content after first space
    df['Phone'] = df[MOBILE].copy()
    df[MOBILE] = df[MOBILE].str.extract(r'((\+336|\+337)\d{8})')[0]
    df['Phone'] = df['Phone'].str.replace(r'(\+336|\+337)\d*', '', regex=True).str.strip()

    return df
