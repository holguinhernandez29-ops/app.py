import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Songwriter Pro")

# Conexión directa
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Falta la llave en Secrets")

st.title("🎼 Songwriter AI")

genero = st.text_input("Género", value="Cumbia")
tema = st.text_input("Historia", value="Alberto y Marissa")

if st.button("Componer ✨"):
    if tema:
        with st.spinner("Escribiendo..."):
            try:
                response = model.generate_content(f"Escribe una canción de {genero} sobre {tema}")
                st.markdown("---")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"Error: {e}")
