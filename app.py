import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Songwriter AI Pro", layout="centered")

# --- CONEXIÓN DIRECTA ---
# Pon tu llave real aquí para asegurar el tiro
LLAVE_API = "AIzaSyDSfUxU8Bn64hYhdhDYnqO_NnF9W9-8O3o" 

try:
    genai.configure(api_key=LLAVE_API)
    # USAMOS ESTE NOMBRE QUE ES EL ESTÁNDAR GLOBAL
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error("Error de inicio.")

st.title("🎼 Songwriter AI Pro")

genero = st.text_input("Género Musical", value="Cumbia")
tema = st.text_area("Historia de la canción", placeholder="Alberto y Marissa amor de lejos...")

if st.button("Componer Obra Maestra ✨"):
    if tema:
        with st.spinner("🚀 Escribiendo..."):
            try:
                # Prompt directo y sencillo
                response = model.generate_content(f"Escribe una canción de {genero} sobre: {tema}")
                st.markdown("### 🎼 Letra:")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                # Si falla el flash, intentamos el pro automáticamente
                try:
                    model_pro = genai.GenerativeModel('gemini-1.5-pro-latest')
                    response = model_pro.generate_content(f"Escribe una canción de {genero} sobre: {tema}")
                    st.write(response.text)
                    st.balloons()
                except:
                    st.error("Google no encontró el modelo. Intenta de nuevo en un momento.")
    else:
        st.warning("Escribe la historia.")
        
