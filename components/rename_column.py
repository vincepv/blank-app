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
        'Category': 'Categorie',
        'Mobile': 'Mobile',
        'First Name': 'Prénom',
        'Last Name': 'Nom',
        'Country': 'Pays',
        'Street Address': 'Adresse',
        'Zip': 'Code postal',
        'City': 'Ville',
        'Email': 'Email',
        'Gender': 'Sexe',
        'Date of Birth': 'Date de naissance',
        'Keywords': 'Mots clés',
    }

    # Renommer les colonnes
    df_renamed_column = df.rename(columns=column_to_rename)

    return df_renamed_column

