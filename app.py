import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Canciones Pro AI", layout="centered")

# --- CONEXIÓN ---
# Reemplaza esto con tu llave real solo para probar esta vez
llave_real = "AIzaSyDSfUxU8Bn64hYhdhDYnqO_NnF9W9-8O3o" 

try:
    genai.configure(api_key=llave_real)
    # Este es el nombre correcto que NO da error 404
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error de inicio: {e}")

st.title("🎼 Songwriter AI Pro")

genero = st.text_input("Género Musical")
tema = st.text_area("Historia de la canción")

if st.button("Componer Obra Maestra ✨"):
    if genero and tema:
        with st.spinner("🚀 Escribiendo..."):
            try:
                prompt = f"Escribe un {genero} sobre: {tema}"
                # Aquí está el truco: quitamos cualquier parámetro raro
                response = model.generate_content(prompt)
                st.markdown("### Letra:")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"Error de Google: {e}")
    else:
        st.warning("Llena los campos.")
        
