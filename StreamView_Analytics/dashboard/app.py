import streamlit as st

st.set_page_config(
    page_title="StreamView Analytics",
    page_icon="🎬",
    layout="wide"
)

st.title("StreamView Analytics")
st.subheader("Análisis del catálogo de películas")

st.write(
    "Dashboard interactivo para analizar popularidad, valoración "
    "y desempeño financiero del catálogo."
)