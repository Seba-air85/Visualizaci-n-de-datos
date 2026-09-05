import streamlit as st
import pandas as pd

from src.preprocessing import (
    load_clean_movies,
    explode_genres,
    get_financial_subset,
)


# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="StreamView Analytics",
    page_icon="🎬",
    layout="wide",
)


# ============================================================
# CARGA DE DATOS
# ============================================================

@st.cache_data
def load_data():
    return load_clean_movies()


df = load_data()


# ============================================================
# TÍTULO
# ============================================================

st.title("🎬 StreamView Analytics")

st.subheader("Análisis del catálogo de películas")

st.write(
    "Dashboard interactivo para analizar popularidad, valoración "
    "y desempeño financiero del catálogo."
)


# ============================================================
# PREPARACIÓN PARA KPIs
# ============================================================

# Películas que tienen al menos un voto
df_ratings = df[df["vote_count"] > 0].copy()

# Películas con presupuesto e ingresos disponibles
df_financial = get_financial_subset(df)


# ============================================================
# KPIs
# ============================================================

total_movies = len(df)

avg_rating = df_ratings["vote_average"].mean()

avg_popularity = df["popularity"].mean()

avg_revenue = df_financial["revenue"].mean()


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        label="🎬 Total de películas",
        value=f"{total_movies:,}"
    )


with col2:
    st.metric(
        label="⭐ Valoración promedio",
        value=f"{avg_rating:.2f}"
    )


with col3:
    st.metric(
        label="🔥 Popularidad promedio",
        value=f"{avg_popularity:.2f}"
    )


with col4:
    st.metric(
        label="💰 Ingresos promedio",
        value=f"${avg_revenue:,.0f}"
    )


# ============================================================
# VISTA PREVIA
# ============================================================

st.divider()

st.write("### Catálogo")

with st.expander("Ver datos del catálogo"):

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

# ============================================================
# FILTROS
# ============================================================

st.sidebar.header("🔎 Filtros")

# Filtro por año
years = sorted(df["release_year"].dropna().unique())

selected_year = st.sidebar.selectbox(
    "Año de estreno",
    ["Todos"] + years
)

# Filtro por género
genres = sorted(
    set(
        genre.strip()
        for value in df["genres"].dropna()
        for genre in value.split(",")
    )
)

selected_genre = st.sidebar.selectbox(
    "Género",
    ["Todos"] + genres
)