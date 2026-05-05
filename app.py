import streamlit as st
import google.generativeai as genai

# Configuración de la página
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

# --- INTERFAZ ---
st.title("🎼 Generador de Letras y Prompts")
mostrar_anuncio("BANNER SUPERIOR")

genero = st.text_input("Género Musical:", placeholder="Ej: Corrido Tumbado, Bachata, Rap...")
tema = st.text_area("¿De qué trata la historia?", placeholder="Escribe los detalles aquí...")

generar_prompt_ia = st.checkbox("Generar Prompt para IA Musical (Suno/Udio)", value=True)

if st.button("Componer ✨", use_container_width=True):
    if tema and genero:
        with st.spinner("Componiendo..."):
            try:
                # CAMBIO CLAVE: Usamos 'gemini-pro' que es el más compatible
                model = genai.GenerativeModel('gemini-pro')
                
                instruccion = f"Escribe la letra de una canción de {genero} sobre: {tema}. Incluye Intro, Versos, Coro y Final."
                if generar_prompt_ia:
                    instruccion += "\nAl final añade un 'Prompt Musical' técnico en inglés para generar la música en una IA como Suno."

                response = model.generate_content(instruccion)
                
                if response.text:
                    st.success("¡Listo!")
                    st.markdown("---")
                    st.write(response.text)
                    st.markdown("---")
            except Exception as e:
                st.error("Error de conexión. Revisa que tu llave API sea válida.")
    else:
        st.warning("Completa los campos de género e historia.")

mostrar_anuncio("BANNER INFERIOR")
