import streamlit as st
import google.generativeai as genai
import streamlit.components.v1 as components

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Songwriter AI Pro", layout="centered", page_icon="🎼")

# --- BLOQUE DE ADSENSE (ANUNCIOS AUTOMÁTICOS) ---
# Sustituye con tu código si llegas a cambiar de cuenta, por ahora es el tuyo:
adsense_code = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8332181120172714"
     crossorigin="anonymous"></script>
"""
# Inyectamos el script de forma invisible
components.html(adsense_code, height=0)

# --- CONEXIÓN CON LA API DE GOOGLE ---
if "GOOGLE_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # Usamos el modelo más estable para evitar errores 404
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error("Error al conectar con el servidor de inteligencia artificial.")
else:
    st.error("⚠️ Falta la configuración de la API Key en los Secrets de Streamlit.")

# --- DISEÑO DE LA APLICACIÓN ---
st.title("🎼 Songwriter AI Pro")
st.markdown("Genera letras de canciones personalizadas en segundos.")

# Entradas del usuario
genero = st.text_input("Género Musical", placeholder="Ej: Cumbia, Regional Mexicano, Rap...")
tema = st.text_area("¿De qué trata la canción?", placeholder="Ej: Una historia de amor a distancia entre Alberto y Marissa...")

# Botón principal
if st.button("Componer Canción ✨", use_container_width=True):
    if genero and tema:
        with st.spinner("🚀 Escribiendo letra..."):
            try:
                # Instrucción para la IA
                prompt = f"Escribe la letra de una canción de {genero} que trate sobre: {tema}. Estructura la canción con Intro, Versos, Coro y Outro."
                
                response = model.generate_content(prompt)
                
                if response.text:
                    st.markdown("---")
                    st.markdown("### 📝 Letra Generada:")
                    st.write(response.text)
                    st.balloons()
            except Exception as e:
                # Intento de respaldo con modelo Pro si el Flash falla
                try:
                    model_pro = genai.GenerativeModel('gemini-1.5-pro')
                    response = model_pro.generate_content(f"Escribe una canción de {genero} sobre {tema}")
                    st.write(response.text)
                    st.balloons()
                except:
                    st.error("El servidor está saturado. Por favor, intenta de nuevo en unos segundos.")
    else:
        st.warning("⚠️ Por favor, escribe un género y una historia para poder componer.")

# --- PIE DE PÁGINA ---
st.markdown("---")
st.caption("Desarrollado con IA - 2026")
