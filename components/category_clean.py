def category_clean(df):
    """
    Reassigns values in the 'Categorie' column of a DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the 'Categorie' column.

    Returns:
    pd.DataFrame: The DataFrame with reassigned values in the 'Categorie' column.
    """
    dic_category = {
        '\.0$': '', 
    }
    category_mapping = {2: 1, 3: 2, 4: 3, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4}
    df['Categorie'] = df['Categorie'].map(category_mapping)
    df['Categorie'] = df['Categorie'].astype(str).replace(dic_category, regex=True)
    return df