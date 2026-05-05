import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="IA Musical Pro", layout="centered")

# --- CONEXIÓN ACTUALIZADA ---
API_KEY = "AIzaSyAQd7vtgDHInLCj2lkoOVSVtjQEfiOxa-k"

try:
    genai.configure(api_key=API_KEY)
    # Cambiamos a gemini-1.5-flash que es el modelo más nuevo y compatible
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Error de configuración inicial.")

st.title("🎼 Generador de Canciones Originales")

# Publicidad
st.markdown('<div style="text-align:center; background-color:#1e2130; padding:10px; border-radius:5px; color:white;">Espacio para Publicidad de Google AdSense</div>', unsafe_allow_html=True)

genero = st.text_input("¿Qué género quieres?", placeholder="Ej: Corrido, Rap, Regional...")
tema = st.text_area("¿De qué trata la canción?", placeholder="Escribe la historia aquí...")

if st.button("Componer Canción ✨"):
    if genero and tema:
        with st.spinner("La IA está rimando..."):
            try:
                # Instrucción para la IA
                prompt = f"Actúa como un compositor experto. Escribe una canción de {genero} sobre: {tema}. Que sea larga, con rimas excelentes, estructura de Intro, 4 Versos, Coro y Final. Usa el lenguaje propio del género."
                
                response = model.generate_content(prompt)
                
                if response.text:
                    st.success("¡Canción lista!")
                    st.markdown(f"### Letra de {genero}")
                    st.markdown(response.text)
                else:
                    st.error("La IA no pudo generar el texto.")
                    
            except Exception as e:
                st.error(f"Error técnico: {str(e)}")
    else:
        st.warning("Llena los campos por favor.")

st.markdown("---")
st.caption("Publicidad Inferior")
