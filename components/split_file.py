import streamlit as st
import pandas as pd
import numpy as np
import io
import zipfile
import math

def split_file(df):
    max_number_line_file = 24000
    number_chunk = math.ceil(len(df) / max_number_line_file)
    
    # Diviser le DataFrame en plusieurs morceaux
    df_chunks = np.array_split(df, number_chunk)
    
    # Créer un buffer en mémoire pour stocker le fichier ZIP
    zip_buffer = io.BytesIO()

    # Créer un fichier ZIP en mémoire
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        # Boucler sur les morceaux et les ajouter au ZIP
        for i, chunk in enumerate(df_chunks):
            # Convertir le DataFrame en CSV
            csv_buffer = io.StringIO()
            chunk.to_csv(csv_buffer, index=False)
            
            # Ajouter le fichier CSV au ZIP
            zip_file.writestr(f"fichier_nettoye_part_{i+1}.csv", csv_buffer.getvalue())
    
    # Remettre le buffer au début pour le téléchargement
    zip_buffer.seek(0)

    # Télécharger le fichier ZIP via un bouton Streamlit
    st.download_button(
        label="Télécharger le fichier ZIP contenant les CSV découpés",
        file_name="fichiers_nettoyes.zip",
        mime="application/zip",
        data=zip_buffer
    )