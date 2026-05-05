import streamlit as st
import google.generativeai as genai
import streamlit.components.v1 as components

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Songwriter AI Pro", layout="centered")

# AdSense (Tu código está aquí)
adsense_code = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8332181120172714"
     crossorigin="anonymous"></script>
"""
components.html(adsense_code, height=0)

# CONEXIÓN LIMPIA
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ Configura la llave en Secrets.")

st.title("🎼 Songwriter AI Pro")

genero = st.text_input("Género Musical", value="Cumbia")
tema = st.text_area("Historia/Detalles", placeholder="Ej: Amor entre Alberto y Marissa...")

if st.button("Componer ✨", use_container_width=True):
    if tema:
        with st.spinner("🚀 Generando letra..."):
            try:
                # LLAMADA DIRECTA: Sin prefijos 'models/' para evitar el 404
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"Escribe una canción de {genero} sobre: {tema}")
                
                st.markdown("---")
                st.markdown("### 📝 Letra:")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"Error detectado: {e}")
                st.info("Asegúrate de haber actualizado el archivo requirements.txt y dale 'Reboot App'.")
    else:
        st.warning("Escribe el tema de la canción.")
         
