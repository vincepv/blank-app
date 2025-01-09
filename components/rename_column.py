from constant.column_name import CATEGORIE, PRENOM, NOM, PAYS, ADRESSE, CP, VILLE, EMAIL, SEXE, DATE_NAISSANCE, MOT_CLE

def rename_column(df):
    """
    Renomme les colonnes spécifiques d'un DataFrame pandas.

    Paramètres:
    df (pd.DataFrame): Le DataFrame dont les colonnes doivent être renommées.

    Retourne:
    pd.DataFrame: Le DataFrame avec les colonnes renommées.
    """
 

    # Dictionnaire de renommage
    column_to_rename = {
        'Category': CATEGORIE,
        'First Name': PRENOM,
        'first name': PRENOM,
        'firstname': PRENOM,
        'First Name': PRENOM,
        'first name': PRENOM,
        'firstname': PRENOM,
        'Last Name': NOM,
        'last name': NOM,
        'lastname': NOM,
        'Country': PAYS,
        'Street Address': ADRESSE,
        'Zip': CP,
        'City': VILLE,
        'Email': EMAIL,
        'email': EMAIL,
        'mail': EMAIL,
        'MAIL': EMAIL,
        'Gender': SEXE,
        'Date of Birth': DATE_NAISSANCE,
        'date': DATE_NAISSANCE,
        'Date': DATE_NAISSANCE,
        'Keywords': MOT_CLE,
    }

    

    # Renommer les colonnes
    df_renamed_column = df.rename(columns=column_to_rename)

    return df_renamed_column

