import streamlit as st

st.title("Dinamica Estructural de Edificios Simples")

# Numero de pisos del edificio
n_pisos =st.number_input("Número de pisos", min_value=1, step=1)

modulo_elasticidad_all = st.radio("Modulo de Elasticidad de las columnas", ["Constante en todos los pisos", "Variable en todos los pisos"])
if modulo_elasticidad_all == "Constante en todos los pisos":
    modulo_elasticidad =st.number_input("Modulo de Elasticidad de las columnas:", min_value=1, step=1, key="modulo_elasticidad")


for piso in range(1, n_pisos + 1):
    st.header(f"Piso {piso}")
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        masa =st.number_input("Masa del piso por metro lineal", min_value=1, step=1, key=f"masa_{piso}")
    with col2:
        longitud =st.number_input("Longitud del piso:", min_value=0.0, step=0.1, key=f"longitud_{piso}")
    with col3:
        altura =st.number_input("Altura del piso:", min_value=0.0, step=0.1, key=f"altura_{piso}")
    col4, col5, col6 = st.columns([1,1,1])
    with col4:
        momento_inercia =st.number_input("Momento de inercia de las columnas:", min_value=0.0, step=0.1, key=f"momento_inercia_{piso}")
    with col5:
        if modulo_elasticidad_all == "Variable en todos los pisos":
            modulo_elasticidad = st.number_input("Mod. de Elast. de las columnas:", min_value=0.0, step=0.1, key=f"modulo_elasticidad_{piso}")
    with col6:
        tipo_columna = st.selectbox("Tipo de columna:", ["Empotrada", "Articulada"], key=f"tipo_columna_{piso}")
