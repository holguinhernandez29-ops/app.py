import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(page_title="IA Musical Pro", layout="centered", page_icon="🎼")

# --- CONEXIÓN SEGURA ---
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("Error: Configura la llave en los Secrets de Streamlit.")

# --- FUNCIÓN PARA PUBLICIDAD ---
def mostrar_anuncio(posicion):
    st.markdown(f"""
    <div style="text-align:center; margin: 15px 0; padding: 10px; background: #f0f2f6; border-radius: 10px; border: 1px dashed #ccc;">
        <p style="color: #666; font-size: 10px; margin: 0;">PUBLICIDAD - {posicion}</p>
    </div>
    """, unsafe_allow_html=True)

# --- DISEÑO ---
st.title("🎼 Generador de Canciones Pro")
mostrar_anuncio("BANNER SUPERIOR")

# Entradas del usuario mejoradas
col1, col2 = st.columns(2)
with col1:
    genero = st.text_input("Género Musical:", placeholder="Ej: Corrido Tumbado, Bachata...")
with col2:
    instrumentos = st.text_input("Instrumentos:", placeholder="Ej: Acordeón, Trompetas, Guitarra...")

tema = st.text_area("¿De qué trata la historia?", placeholder="Ej: La historia de amor de Marissa y Alberto...")

if st.button("Componer Obra Maestra ✨", use_container_width=True):
    if tema and genero:
        with st.spinner("Escribiendo rimas..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # El prompt ahora incluye los instrumentos para que la letra tenga ese estilo
                prompt = f"""
                Escribe la letra de una canción de {genero}. 
                Debe estar pensada para sonar con {instrumentos}.
                Tema: {tema}.
                Estructura: Intro, Versos, Coro pegajoso y Final.
                Haz rimas de alta calidad y usa lenguaje acorde al género.
                """
                
                response = model.generate_content(prompt)
                
                if response.text:
                    st.success("¡Listo! Aquí tienes tu canción:")
                    st.markdown("---")
                    st.write(response.text)
                    st.markdown("---")
                else:
                    st.error("No se pudo generar la letra, intenta de nuevo.")
            except Exception as e:
                st.error(f"Asegúrate de que la llave en Secrets esté bien guardada. Error: {str(e)}")
    else:
        st.warning("Por favor escribe el Género y la Historia.")

mostrar_anuncio("BANNER INFERIOR")
