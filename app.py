import streamlit as st
import google.generativeai as genai
import streamlit.components.v1 as components

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Songwriter AI Pro", layout="centered")

# --- ADSENSE ---
adsense_code = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8332181120172714"
     crossorigin="anonymous"></script>
"""
components.html(adsense_code, height=0)

# --- CONEXIÓN ESTABLE ---
# Buscamos la llave en los Secrets de Streamlit
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
else:
    st.error("⚠️ Configura la llave en los Secrets de Streamlit.")

st.title("🎼 Songwriter AI Pro")

genero = st.text_input("Género Musical", value="Cumbia")
tema = st.text_area("Historia/Detalles", placeholder="Escribe aquí la historia...")

if st.button("Componer ✨", use_container_width=True):
    if tema:
        with st.spinner("🚀 Escribiendo..."):
            try:
                # LA SOLUCIÓN AL 404: Usar el nombre exacto sin prefijos raros
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # Forzamos que use la versión estable de la API
                response = model.generate_content(f"Escribe una canción de {genero} sobre: {tema}")
                
                st.markdown("---")
                st.markdown("### 📝 Letra Generada:")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                # Si falla, este error nos dirá exactamente qué falta
                st.error(f"Detalle técnico: {e}")
    else:
        st.warning("Escribe algo para empezar.")
         
