import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Songwriter Pro")

# Intento de conexión
if "GOOGLE_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"Error de configuración: {e}")
else:
    st.error("No se encontró la llave en Secrets")

st.title("🎼 Songwriter AI Pro")

genero = st.text_input("Género")
tema = st.text_area("Historia")

if st.button("Componer ✨"):
    try:
        response = model.generate_content(f"Escribe un {genero} sobre {tema}")
        st.write(response.text)
        st.balloons()
    except Exception as e:
        # Esto nos dirá el error REAL (ej. Key not valid, Quota exceeded)
        st.error(f"Error real de Google: {e}")
        
