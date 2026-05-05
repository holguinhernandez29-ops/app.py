import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Songwriter AI Pro", layout="centered")

# --- CONEXIÓN DIRECTA ---
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Configura la llave en Secrets.")

st.title("🎼 Songwriter AI Pro")

genero = st.text_input("Género Musical")
tema = st.text_area("Historia/Detalles")

if st.button("Componer ✨", use_container_width=True):
    if genero and tema:
        with st.spinner("🚀 Escribiendo..."):
            # INTENTO 1: Modelo Flash Estable
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"Escribe una canción de {genero} sobre: {tema}")
                st.markdown("---")
                st.write(response.text)
                st.balloons()
            except:
                # INTENTO 2: Modelo Pro (Respaldo)
                try:
                    model_alt = genai.GenerativeModel('gemini-1.5-pro')
                    response = model_alt.generate_content(f"Escribe una canción de {genero} sobre: {tema}")
                    st.write(response.text)
                    st.balloons()
                except Exception as e:
                    st.error("Servidor saturado. Intenta de nuevo en 10 segundos.")
    else:
        st.warning("Completa los campos.")
    
