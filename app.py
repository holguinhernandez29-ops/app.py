import streamlit as st
import google.generativeai as genai
import streamlit.components.v1 as components

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Songwriter AI Pro", layout="centered")

# AdSense (Tu código personal)
adsense_code = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8332181120172714"
     crossorigin="anonymous"></script>
"""
components.html(adsense_code, height=0)

# CONEXIÓN DIRECTA A LA VERSIÓN ESTABLE
if "GOOGLE_API_KEY" in st.secrets:
    # Configuramos la llave
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ Configura la llave en Secrets.")

st.title("🎼 Songwriter AI Pro")

genero = st.text_input("Género Musical", value="Cumbia")
tema = st.text_area("Historia/Detalles", value="Amor")

if st.button("Componer ✨", use_container_width=True):
    if tema:
        with st.spinner("🚀 Generando canción..."):
            try:
                # LLAMADA FORZADA A LA VERSIÓN ESTABLE v1
                # Usamos el nombre del modelo sin el prefijo 'models/' para evitar el 404
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                response = model.generate_content(
                    f"Escribe una canción de {genero} sobre: {tema}"
                )
                
                st.markdown("---")
                st.markdown("### 📝 Letra Generada:")
                st.write(response.text)
                st.balloons()
                
            except Exception as e:
                st.error(f"Error detectado: {e}")
                st.info("Si el error persiste, dale clic a 'Reboot App' en el menú de Streamlit.")
    else:
        st.warning("Escribe el tema de la canción.")
         
