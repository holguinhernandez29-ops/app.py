import streamlit as st
import google.generativeai as genai
import streamlit.components.v1 as components

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Songwriter AI Pro", layout="centered")

# AdSense (Tu código está activo aquí)
adsense_code = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8332181120172714"
     crossorigin="anonymous"></script>
"""
components.html(adsense_code, height=0)

# CONEXIÓN SEGURA
if "GOOGLE_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # USAMOS EL NOMBRE ESTABLE (Sin "models/" y sin "beta")
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error("Error de configuración.")
else:
    st.error("Configura la llave en Secrets.")

st.title("🎼 Songwriter AI Pro")

genero = st.text_input("Género Musical", value="Cumbia")
tema = st.text_area("Historia/Detalles", placeholder="Historia de amor entre Alberto y Marissa...")

if st.button("Componer ✨", use_container_width=True):
    if tema:
        with st.spinner("🚀 Escribiendo..."):
            try:
                # La llamada ahora es limpia y directa
                response = model.generate_content(f"Escribe una canción de {genero} sobre: {tema}")
                st.markdown("---")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"Hubo un detalle: {e}")
    else:
        st.warning("Escribe de qué trata la canción.")
         
