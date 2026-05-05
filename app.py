import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="IA Musical Pro", layout="centered", page_icon="🎼")

# --- FUNCIÓN DE ANUNCIOS ---
def mostrar_anuncio(posicion):
    st.markdown(f"""<div style="text-align:center; margin: 10px 0; padding: 10px; background: #f0f2f6; border-radius: 8px; border: 1px dashed #ccc;"><p style="color: #666; font-size: 10px; margin: 0;">PUBLICIDAD - {posicion}</p></div>""", unsafe_allow_html=True)

# --- CONFIGURACIÓN DE IA ---
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("⚠️ ERROR: No se encontró la llave 'GOOGLE_API_KEY' en los Secrets.")
else:
    genai.configure(api_key=api_key)

# --- INTERFAZ ---
st.title("🎼 Generador de Canciones Pro")
mostrar_anuncio("BANNER SUPERIOR")

genero = st.text_input("Género Musical:", placeholder="Ej: Corrido, Bachata, Rap...")
tema = st.text_area("Historia de la canción:", placeholder="Ej: Alberto y Marissa...")

col_op1, col_op2 = st.columns(2)
with col_op1:
    generar_prompt = st.checkbox("Generar Prompt para Suno/Udio", value=True)
with col_op2:
    vibe = st.selectbox("Estilo:", ["Romántico", "Bélico", "Triste", "Fiesta"])

if st.button("Componer Obra Maestra ✨", use_container_width=True):
    if not api_key:
        st.error("No hay llave configurada.")
    elif genero and tema:
        placeholder = st.empty()
        placeholder.info("🚀 Conectando... (esto no debe tardar más de 10 segundos)")
        
        try:
            # Forzamos el modelo Flash que es el más rápido
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt_final = f"Escribe la letra de una canción de {genero} estilo {vibe} sobre: {tema}. Estructura: Intro, Versos, Coro, Final."
            if generar_prompt:
                prompt_final += "\nAl final añade un 'Prompt Musical' técnico en inglés para Suno/Udio."

            # Llamada con respuesta directa
            response = model.generate_content(prompt_final)
            
            placeholder.empty()
            if response.text:
                st.markdown("### 🎼 Resultado:")
                st.write(response.text)
                st.balloons()
        except Exception as e:
            placeholder.empty()
            st.error(f"❌ Error de Google: {str(e)}")
            st.info("Sugerencia: Si el error dice 'API key not valid', genera una nueva llave en Google AI Studio.")
    else:
        st.warning("Completa los campos.")

mostrar_anuncio("BANNER INFERIOR")
                
