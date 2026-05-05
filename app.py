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

# CONEXIÓN LIMPIA
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Falta la llave en Secrets.")

st.title("🎼 Songwriter AI Pro")

genero = st.text_input("Género Musical", value="Cumbia")
tema = st.text_area("Historia/Detalles", placeholder="Escribe la historia...")

if st.button("Componer ✨", use_container_width=True):
    if tema:
        with st.spinner("🚀 Generando letra..."):
            try:
                # TRUCO MAESTRO: Usamos solo el nombre del modelo sin prefijos
                # Esto evita que la librería vieja busque en 'v1beta'
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                response = model.generate_content(
                    f"Escribe una canción de {genero} sobre: {tema}",
                    generation_config={"version": "v1"} # Forzamos versión estable
                )
                
                st.markdown("---")
                st.markdown("### 📝 Letra:")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                # Si lo anterior falla, probamos con la ruta completa del servidor
                try:
                    model_alt = genai.GenerativeModel('models/gemini-1.5-flash')
                    response = model_alt.generate_content(f"Escribe un {genero} sobre {tema}")
                    st.write(response.text)
                    st.balloons()
                except Exception as e2:
                    st.error(f"Error persistente: {e2}")
                    st.info("Intenta darle 'Reboot App' en el menú de la derecha de Streamlit.")
                     
