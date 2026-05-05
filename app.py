import streamlit as st
import google.generativeai as genai

# Configuración estética de la página
st.set_page_config(
    page_title="Songwriter AI Pro",
    page_icon="🎵",
    layout="centered"
)

# --- ESTILOS PERSONALIZADOS (CSS) ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 10px;
    }
    .song-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #FF4B4B;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONEXIÓN SEGURA ---
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    else:
        st.error("⚠️ Configuración pendiente: Agregue la llave en Secrets.")
except:
    st.error("❌ Error de conexión.")

# --- ENCABEZADO ---
st.title("🎵 Songwriter AI Pro")
st.markdown("---")

# --- INTERFAZ PROFESIONAL ---
col1, col2 = st.columns([1, 1])

with col1:
    genero = st.text_input("✨ Género Musical", placeholder="Ej: Corrido, Bachata, Rap...")
    
with col2:
    vibe = st.selectbox("🎭 Sentimiento", ["Romántico", "Triste", "Alegre/Fiesta", "Bélico", "Motivacional"])

tema = st.text_area("📝 Historia o Detalles", placeholder="Cuéntanos la historia de la canción (ej: Alberto y Marissa)...", height=100)

# Opciones avanzadas en un desplegable
with st.expander("⚙️ Opciones de IA"):
    generar_prompt = st.checkbox("Generar Prompt técnico para Suno/Udio", value=True)
    creatividad = st.slider("Nivel de creatividad", 0.0, 1.0, 0.7)

# --- LÓGICA DE GENERACIÓN ---
if st.button("Componer Obra Maestra"):
    if genero and tema:
        with st.spinner("🚀 Nuestra IA está componiendo tus rimas..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt_final = f"""
                Actúa como un compositor premiado. Escribe una canción de {genero} con un sentimiento {vibe}.
                Tema principal: {tema}.
                Estructura: Intro, Versos, Coro potente, Puente y Final.
                """
                if generar_prompt:
                    prompt_final += "\nAl final, incluye una sección llamada 'PROMPT PARA IA MUSICAL' con etiquetas técnicas en inglés."

                response = model.generate_content(prompt_final)
                
                if response.text:
                    st.markdown("### 🎼 Resultado de la Composición")
                    st.markdown(f'<div class="song-box">{response.text}</div>', unsafe_allow_html=True)
                    st.balloons() # ¡Efecto de celebración!
            except Exception as e:
                st.error("El servidor está saturado. Intenta de nuevo en 10 segundos.")
    else:
        st.warning("⚠️ Por favor rellena el género y la historia.")

st.markdown("---")
st.caption("© 2026 AI Musical Studio - Chihuahua, MX")
