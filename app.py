import streamlit as st
import google.generativeai as genai
import streamlit.components.v1 as components
import os

# --- ADSENSE ---
adsense_code = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8332181120172714"
     crossorigin="anonymous"></script>
"""
components.html(adsense_code, height=0)

# --- CONEXIÓN FORZADA ---
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
else:
    st.error("Falta la llave en Secrets.")

st.title("🎼 Songwriter AI Pro")

genero = st.text_input("Género Musical", value="Cumbia")
tema = st.text_area("Historia", value="Amor entre Alberto y Marissa")

if st.button("Componer ✨", use_container_width=True):
    if tema:
        with st.spinner("🚀 Escribiendo..."):
            try:
                # LLAMADA LIMPIA
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"Escribe una canción de {genero} sobre {tema}")
                st.success("¡Logrado!")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"Error: {e}")
                st.info("Si ves esto, ve a 'Manage App' -> 'Reboot App'.")
                 
