import streamlit as st
import google.generativeai as genai

st.title("🎼 Songwriter AI")

if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Falta la llave en Secrets")

genero = st.text_input("Género", value="Cumbia")
tema = st.text_input("Historia", value="Amor")

if st.button("Componer ✨"):
    try:
        response = model.generate_content(f"Escribe una canción de {genero} sobre {tema}")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
        
