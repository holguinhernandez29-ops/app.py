import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(page_title="IA Musical Pro", layout="centered", page_icon="🎼")

# --- CONEXIÓN SEGURA ---
try:
    # Busca la llave en los Secrets de Streamlit
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("Error: Configura la llave en los Secrets de Streamlit con el nombre GOOGLE_API_KEY")

# --- PUBLICIDAD ---
def mostrar_anuncio(posicion):
    st.markdown(f"""
    <div style="text-align:center; margin: 15px 0; padding: 10px; background: #f0f2f6; border-radius: 10px; border: 1px dashed #ccc;">
        <p style="color: #666; font-size: 10px; margin: 0;">PUBLICIDAD - {posicion}</p>
    </div>
    """, unsafe_allow_html=True)

# --- DISEÑO ---
st.title("🎼 Generador de Letras IA")
mostrar_anuncio("BANNER SUPERIOR")

# Entrada de Género Libre
genero = st.text_input("Género de la canción:", placeholder="Ej: Corrido, Rap, Bachata, Reggaeton...")

# Historia/Tema
tema = st.text_area("¿De qué trata la letra?", placeholder="Ej: Una historia de amor de Alberto y Marissa que superó la distancia...")

if st.button("Generar Letra ✨", use_container_width=True):
    if tema and genero:
        with st.spinner("Escribiendo rimas..."):
            try:
                # Usamos el modelo más estable para texto
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = f"""
                Eres un compositor experto. Escribe la letra de una canción de {genero}.
                Tema: {tema}.
                Estructura: Intro, Versos, Coro pegajoso y Final.
                Asegúrate de que las rimas sean buenas y tengan sentimiento.
                """
                
                response = model.generate_content(prompt)
                
                if response.text:
                    st.success("¡Letra generada!")
                    st.markdown("---")
                    st.write(response.text)
                    st.markdown("---")
            except Exception as e:
                st.error(f"Hubo un detalle: {str(e)}")
    else:
        st.warning("Escribe el género y la historia para poder componer.")

mostrar_anuncio("BANNER INFERIOR")
