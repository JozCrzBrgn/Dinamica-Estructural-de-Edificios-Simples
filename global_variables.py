
import streamlit as st
from supabase import create_client

# Variables globales
class Variables:
    def __init__(self):
        #? Conexión a la base de datos        
        self.SUPABASE = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
        #? Bucket
        self.BUCKET_ES = st.secrets["BUCKET_ES"]

# Instanciamos la clase
vars = Variables()