import streamlit as st
import google.generativeai as genai

# Configuración
st.set_page_config(page_title="Compositor Pro IA", layout="centered", page_icon="🎼")

# --- CONEXIÓN SEGURA ---
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("Error: Configura 'GOOGLE_API_KEY' en los Secrets de Streamlit.")

# --- PUBLICIDAD ---
def mostrar_anuncio(posicion):
    st.markdown(f"""<div style="text-align:center; margin: 10px 0; padding: 10px; background: #f0f2f6; border-radius: 8px; border: 1px dashed #ccc;"><p style="color: #666; font-size: 10px; margin: 0;">PUBLICIDAD - {posicion}</p></div>""", unsafe_allow_html=True)

# --- DISEÑO ---
st.title("🎼 Generador de Letras y Prompts")
mostrar_anuncio("BANNER SUPERIOR")

genero = st.text_input("Género Musical:", placeholder="Ej: Corrido Tumbado, Bachata Romántica...")
tema = st.text_area("¿De qué trata la historia?", placeholder="Escribe los detalles aquí...")

# NUEVA OPCIÓN: Generar también el prompt para música
generar_prompt_ia = st.checkbox("Generar Prompt para IA Musical (Suno/Udio)", value=True)

if st.button("Componer ✨", use_container_width=True):
    if tema and genero:
        with st.spinner("Escribiendo rimas y estilo..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash-latest')
                
                # Instrucción para que haga ambas cosas
                prompt_input = f"""
                1. Escribe la letra de una canción de {genero} sobre: {tema}. Estructura: Intro, Versos, Coro, Final.
                """
                if generar_prompt_ia:
                    prompt_input += f"\n2. Al final, crea un 'Prompt Musical' corto y técnico en inglés y español para generar esta canción en una IA de música, detallando el estilo, tempo y vibra."

                response = model.generate_content(prompt_input)
                
                if response.text:
                    st.success("¡Composición lista!")
                    st.markdown("---")
                    st.write(response.text)
                    st.markdown("---")
                else:
                    st.error("No se pudo generar, intenta de nuevo.")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Falta el género o la historia.")

mostrar_anuncio("BANNER INFERIOR")
