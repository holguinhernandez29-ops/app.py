import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="IA Musical Pro", layout="centered")

# --- CONEXIÓN DIRECTA ---
# Asegúrate de que no haya espacios antes o después de la clave
API_KEY = "AIzaSyAQd7vtgDHInLCj2lkoOVSVtjQEfiOxa-k"

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error("Error de configuración inicial.")

st.title("🎼 Generador de Canciones Originales")

# Publicidad
st.info("Espacio para Publicidad de Google AdSense")

genero = st.text_input("¿Qué género quieres?", placeholder="Ej: Corrido, Rap, Regional...")
tema = st.text_area("¿De qué trata la canción?", placeholder="Escribe la historia aquí...")

if st.button("Componer Canción ✨"):
    if genero and tema:
        with st.spinner("La IA está rimando..."):
            try:
                # Instrucción optimizada
                prompt = f"Escribe una canción de {genero}. Tema: {tema}. Hazla larga, con rimas excelentes, intro, 4 versos, coro y final."
                
                response = model.generate_content(prompt)
                
                # Verificamos si la respuesta tiene texto
                if response.text:
                    st.success("¡Canción lista!")
                    st.markdown(f"### {genero}")
                    st.write(response.text)
                else:
                    st.error("La IA no pudo generar texto, intenta con otro tema.")
                    
            except Exception as e:
                # Esto nos dirá el error real si falla
                st.error(f"Error técnico: {str(e)}")
    else:
        st.warning("Llena los campos por favor.")

st.markdown("---")
st.caption("Publicidad Inferior")
