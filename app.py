import streamlit as st
import google.generativeai as genai

st.title("Conexión Directa")

# Prueba con tu llave nueva
llave = "AIzaSyDSfUxU8Bn64hYhdhDYnqO_NnF9W9-8O3o" 

if st.button("Probar"):
    try:
        genai.configure(api_key=llave)
        # Usamos 'gemini-pro' que es el nombre más estable
        model = genai.GenerativeModel('gemini-pro')
        
        response = model.generate_content("Hola, dime una frase corta de éxito")
        
        st.success("¡CONECTADO!")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
        
