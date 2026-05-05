import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Songwriter AI Pro", layout="centered")

# --- CONEXIÓN ---
if "GOOGLE_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # NOMBRE ACTUALIZADO PARA EVITAR ERROR 404
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
    except Exception as e:
        st.error("Error al configurar el servidor.")
else:
    st.error("Falta la configuración en Secrets.")

st.title("🎼 Songwriter AI Pro")

genero = st.text_input("Género Musical")
tema = st.text_area("Historia/Detalles")

if st.button("Componer ✨", use_container_width=True):
    if genero and tema:
        with st.spinner("🚀 Escribiendo..."):
            try:
                # Intento de generación
                prompt = f"Escribe una canción de {genero} sobre: {tema}. Incluye Intro, Versos y Coro."
                response = model.generate_content(prompt)
                
                if response.text:
                    st.markdown("---")
                    st.markdown("### 🎼 Letra:")
                    st.write(response.text)
                    st.balloons()
            except Exception as e:
                # Si falla el anterior, este es el plan B
                try:
                    model_alt = genai.GenerativeModel('gemini-pro')
                    response = model_alt.generate_content(prompt)
                    st.write(response.text)
                    st.balloons()
                except:
                    st.error("El servidor está ocupado. Intenta de nuevo en unos segundos.")
    else:
        st.warning("Por favor completa los campos.")
        
