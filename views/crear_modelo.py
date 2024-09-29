import streamlit as st
from supabase_bucket import upload_to_supabase, files_in_supabase

st.title("Dinámica Estructural de Edificios Simples")

# Numero de pisos del edificio
col01, col02 = st.columns(2)
with col01:
    nombre_edificio =st.text_input("Nombre del edificio", key="nombre_edificio")
with col02:
    n_pisos =st.number_input("Número de pisos", min_value=1, step=1)

EI_choose = st.radio("Rigidez de las columnas (EI)", ["Constante en todas las columnas", "Diferente en todas las columnas"])
if EI_choose == "Constante en todas las columnas":
    EI_val =st.number_input("Rigidez de las columnas:", min_value=1, step=1, key="EI_val")


datos_edificio = []
for piso in range(1, n_pisos + 1):
    st.header(f"Piso {piso}")
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        masa =st.number_input("Masa del piso por metro lineal", min_value=1, step=1, key=f"masa_{piso}")
    with col2:
        longitud =st.number_input("Longitud del piso:", min_value=0.0, step=0.1, key=f"longitud_{piso}")
    with col3:
        altura =st.number_input("Altura del piso:", min_value=0.0, step=0.1, key=f"altura_{piso}")
    col4, col5 = st.columns([1,1])
    with col4:
        tipo_columna = st.selectbox("Tipo de columna:", ["Empotrada", "Articulada"], key=f"tipo_columna_{piso}")
    with col5:
        if EI_choose == "Diferente en todas las columnas":
            EI_val = st.number_input("Rigidez de la columna (EI):", min_value=0.0, step=0.1, key=f"EI_val_{piso}")

    # Almacenar los datos del piso en una lista
    datos_edificio.append({
        'masa': masa,
        'longitud': longitud,
        'altura': altura,
        'rigidez': EI_val,
        'tipo_columna': tipo_columna
    })

if st.button("Guardar datos"):
    if nombre_edificio in [item['name'][:-5] for item in files_in_supabase()]:
        st.error("El archivo ya existe en Supabase")
    else:
        if nombre_edificio == "":
            st.error("Debes ingresar un nombre para el edificio")
        else:
            # Almacenar los datos en supabase
            upload_to_supabase(datos_edificio, nombre_edificio)
            st.success("Archivo subido correctamente")