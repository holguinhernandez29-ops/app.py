import streamlit as st
import google.generativeai as genai

# Configuración estética
st.set_page_config(page_title="Songwriter AI Pro", layout="centered", page_icon="🎼")

# --- CONEXIÓN INVISIBLE ---
def inicializar_servicio():
    try:
        # Intenta conectar usando la llave guardada en los secretos
        if "GOOGLE_API_KEY" in st.secrets:
            genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
            return True
        return False
    except:
        return False

# --- DISEÑO DE LA APP ---
st.title("🎼 Songwriter AI Pro")

# Espacio publicitario superior
st.markdown("""<div style="text-align:center; padding:10px; background:#f0f2f6; border-radius:8px; border:1px solid #ddd; margin-bottom:20px;"><p style="color:#888; font-size:12px; margin:0;">ESPACIO PUBLICITARIO</p></div>""", unsafe_allow_html=True)

# Entradas del usuario
col1, col2 = st.columns(2)
with col1:
    genero = st.text_input("Género Musical", placeholder="Ej: Corrido, Pop, Rap...")
with col2:
    estilo = st.selectbox("Estilo", ["Romántico", "Alegre", "Triste", "Bélico"])

tema = st.text_area("¿De qué quieres que hable la canción?", placeholder="Escribe los detalles o la historia aquí...", height=100)

if st.button("Componer Canción ✨", use_container_width=True):
    if genero and tema:
        with st.spinner("Escribiendo tu próxima obra maestra..."):
            if inicializar_servicio():
                try:
                    # Modelo estándar para máxima compatibilidad
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    
                    prompt = f"Escribe la letra de una canción de {genero} estilo {estilo} sobre: {tema}. Incluye Intro, Versos, Coro y Final. También incluye al final un prompt técnico en inglés para generar la música en IA."
                    
                    response = model.generate_content(prompt)
                    
                    if response.text:
                        st.markdown("---")
                        st.markdown("### 🎼 Letra Generada")
                        st.write(response.text)
                        st.balloons()
                except:
                    st.error("Lo sentimos, el servicio está experimentando alta demanda. Por favor, intenta de nuevo en unos momentos.")
            else:
                # Mensaje genérico por si la llave falla, para que el usuario no sepa qué es
                st.error("Servicio temporalmente no disponible. Inténtelo más tarde.")
    else:
        st.warning("Por favor, completa los campos de género e historia.")

# Espacio publicitario inferior
st.markdown("""<div style="text-align:center; padding:10px; background:#f0f2f6; border-radius:8px; border:1px solid #ddd; margin-top:30px;"><p style="color:#888; font-size:12px; margin:0;">ESPACIO PUBLICITARIO</p></div>""", unsafe_allow_html=True)
