import streamlit as st
import google.generativeai as genai

# Configuración Pro
st.set_page_config(page_title="Compositor AI Pro", layout="centered", page_icon="🎼")

# --- CONEXIÓN SEGURA ---
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    else:
        st.error("⚠️ Falta la llave en Secrets.")
except:
    st.error("❌ Error de conexión.")

# --- PUBLICIDAD ---
def mostrar_anuncio(posicion):
    st.markdown(f"""<div style="text-align:center; margin: 10px 0; padding: 10px; background: #f0f2f6; border-radius: 8px; border: 1px dashed #ccc;"><p style="color: #666; font-size: 10px; margin: 0;">PUBLICIDAD - {posicion}</p></div>""", unsafe_allow_html=True)

# --- DISEÑO ---
st.title("🎼 Generador de Canciones Pro")
mostrar_anuncio("BANNER SUPERIOR")

# Entradas
genero = st.text_input("Género Musical:", placeholder="Ej: Corrido Tumbado, Bachata, Rap...")
tema = st.text_area("Historia de la canción:", placeholder="Ej: Alberto y Marissa...")

# Opciones adicionales
col_op1, col_op2 = st.columns(2)
with col_op1:
    generar_prompt = st.checkbox("Generar Prompt para Suno/Udio", value=True)
with col_op2:
    vibe = st.selectbox("Estilo:", ["Romántico", "Bélico", "Triste", "Fiesta"])

if st.button("Componer Obra Maestra ✨", use_container_width=True):
    if genero and tema:
        with st.spinner("🚀 Escribiendo rimas..."):
            try:
                # Usamos el modelo más rápido y disponible para evitar que se quede cargando
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                instruccion = f"Escribe la letra de una canción de {genero} estilo {vibe} sobre: {tema}. Estructura: Intro, Versos, Coro, Final."
                if generar_prompt:
                    instruccion += "\nAl final añade un 'Prompt Musical' técnico en inglés para Suno/Udio."

                response = model.generate_content(instruccion)
                
                if response.text:
                    st.markdown("### 🎼 Letra Generada:")
                    st.write(response.text)
                    st.balloons()
            except Exception as e:
                st.error("La IA está tardando en responder. Refresca la página e intenta con un tema más corto.")
    else:
        st.warning("Completa el género y la historia.")

mostrar_anuncio("BANNER INFERIOR")
