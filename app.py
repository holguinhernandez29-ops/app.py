import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Compositor Final")

# CONEXIÓN ULTRA-SIMPLE
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Revisa los Secrets en Streamlit.")

st.title("🎼 Songwriter AI Pro")

genero = st.text_input("Género")
tema = st.text_area("Historia")

if st.button("Componer ✨"):
    if genero and tema:
        with st.spinner("Conectando..."):
            try:
                # Forzamos el modelo más estable que existe
                model = genai.GenerativeModel('gemini-pro')
                res = model.generate_content(f"Escribe un {genero} sobre {tema}")
                st.write(res.text)
                st.balloons()
            except Exception as e:
                # Si falla el pro, intentamos el flash a la fuerza
                try:
                    model2 = genai.GenerativeModel('gemini-1.5-flash')
                    res2 = model2.generate_content(f"Escribe un {genero} sobre {tema}")
                    st.write(res2.text)
                    st.balloons()
                except:
                    st.error(f"Error final: {e}. Verifica tu llave en Google AI Studio.")
                    
