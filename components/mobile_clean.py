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
    
    df['Mobile'] = df['Mobile'].astype(str).replace(dic_mobile_character, regex=True)
    df['Mobile'] = df['Mobile'].astype(str).replace(dic_mobile_number, regex=True)

    return df
