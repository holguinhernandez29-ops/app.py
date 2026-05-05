import streamlit as st
import google.generativeai as genai
import streamlit.components.v1 as components

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Songwriter AI Pro", layout="centered")

# AdSense
adsense_code = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8332181120172714"
     crossorigin="anonymous"></script>
"""
components.html(adsense_code, height=0)

# Conexión Segura
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Falta la llave en Secrets.")

st.title("🎼 Songwriter AI Pro")

genero = st.text_input("Género Musical")
tema = st.text_area("Historia/Detalles")

if st.button("Componer ✨", use_container_width=True):
    if genero and tema:
        with st.spinner("🚀 Escribiendo..."):
            try:
                # Usamos el modelo más nuevo para evitar el error 404
                response = model.generate_content(f"Escribe una canción de {genero} sobre: {tema}")
                st.markdown("### 📝 Letra:")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"Error de Google: {e}")
    else:
        st.warning("Completa los campos.")
        
