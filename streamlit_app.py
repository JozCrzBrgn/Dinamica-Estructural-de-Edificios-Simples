import streamlit as st

#? --- PAGE SETUP ---#
st.set_page_config(layout="wide")


data_page = st.Page(
    page="views/crear_modelo.py",
    title="Crear modelo",
    icon="💾",
    default=True
)

otro_page = st.Page(
    page="views/otro.py",
    title="Otro",
    icon="💾"
)

#? --- NAVEGATION SETUP [WITH SECTIONS] ---#
pg = st.navigation(
    {
        "Ingreso de datos": [data_page],
    }
)

#? --- SHARE ON ALL PAGES ---#
#st.logo("assets/code_ingeneiria.png")
st.sidebar.text("Made by Code Ingeniería 🧑‍💻")

#? --- RUN NAVEGATION ---#
pg.run()