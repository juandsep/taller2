import streamlit as st

import pandas as pd



primaryColor = "#d33682"
backgroundColor = "#002b36"
secondaryBackgroundColor = "#586e75"
textColor = "#fafafa"
font = "monospace"

st.set_page_config(page_title="Recomendacion lugares nocturnos",page_icon="🧊", layout="wide",initial_sidebar_state="expanded")

datos_csv=pd.read_csv("usuarios y recomendacion.csv")

st.title("Best nightlife for you")

users=["user1","user2"]

col1, col2 = st.columns(2)


with col1:
    st.image("https://planning-org-uploaded-media.s3.amazonaws.com/image/Planning-2020-02-image26.jpg", width=400)
with col2:
    usuario = st.text_input('Write your user ID', 'User ID')
    if usuario in users:
        resultados=datos_csv[datos_csv["usuario"].str.contains(usuario)]
        st.text("This are the best places for you based on your califications")
        st.dataframe(resultados)  # Same as st.write(df)
    else:
        st.text("User not found")
        resultados=None
        st.page_link("pages/registrar.py", label="Best places in your city!")







