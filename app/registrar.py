import streamlit as st

import pandas as pd


st.set_page_config(
)

st.title("Best nightife places in your city")

datos_csv=pd.read_csv("recomendacion por lugar.csv")

datos_csv["rating"]=0

col1, col2 = st.columns(2)

with col1:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEcRboZDta7sR5JhDYIL0_MhELyWdhQx4G4YQNd9aHgw&s", width=350)
with col2:
    ciudad = st.text_input('Please write your city', 'City')
    if ciudad in datos_csv["city"].values:
        resultados=datos_csv[datos_csv["city"].str.contains(ciudad)]
        st.text("This are the top rated places in your city")
        st.data_editor(resultados)
    else:
        resultados=None
        st.text("City not available")

        














