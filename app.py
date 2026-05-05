import streamlit as st
import google.generativeai as genai

# PEGA TU LLAVE AQUÍ DIRECTAMENTE PARA PROBAR
genai.configure(api_key="AIzaSyDSfUxU8Bn64hYhdhDYnqO_NnF9W9-8O3o")

st.title("Prueba de Conexión")
if st.button("Probar"):
    model = genai.GenerativeModel('gemini-1.5-flash')
    res = model.generate_content("Hola")
    st.write(res.text)
    
