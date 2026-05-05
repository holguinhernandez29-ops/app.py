import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Canciones Pro AI", layout="centered", page_icon="🎼")

# --- CONEXIÓN SEGURA ---
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ Configura la llave en los Secrets de Streamlit.")

# --- PUBLICIDAD ---
def mostrar_anuncio(posicion):
    st.markdown(f"""<div style="text-align:center; margin: 10px 0; padding: 10px; background: #f0f2f6; border-radius: 8px; border: 1px dashed #ccc;"><p style="color: #666; font-size: 10px; margin: 0;">PUBLICIDAD - {posicion}</p></div>""", unsafe_allow_html=True)

st.title("🎼 Canciones Pro AI")
mostrar_anuncio("BANNER SUPERIOR")

col1, col2 = st.columns(2)
with col1:
    genero = st.text_input("Género Musical:", placeholder="Ej: Corrido, Rap...")
with col2:
    estilo = st.selectbox("Estilo:", ["Romántico", "Bélico", "Triste", "Fiesta"])

tema = st.text_area("Historia de la canción:", placeholder="Ej: Alberto y Marissa...")
generar_suno = st.checkbox("Generar Prompt para Suno/Udio", value=True)

if st.button("Componer Obra Maestra ✨", use_container_width=True):
    if genero and tema:
        with st.spinner("🚀 Componiendo..."):
            try:
                # NOMBRE CORREGIDO PARA EVITAR EL ERROR 404
                model = genai.GenerativeModel('gemini-1.5-flash-001')
                
                prompt = f"Escribe la letra de una canción de {genero} {estilo} sobre: {tema}. Incluye Intro, Versos, Coro y Final."
                if generar_suno:
                    prompt += "\nAl final añade un 'Prompt Musical' técnico en inglés para Suno/Udio."
                
                response = model.generate_content(prompt)
                
                if response.text:
                    st.markdown("### 🎼 Letra Generada:")
                    st.write(response.text)
                    st.balloons()
            except Exception as e:
                # Si el anterior falla, intenta con la versión estable
                try:
                    model_alt = genai.GenerativeModel('gemini-1.5-pro-001')
                    response = model_alt.generate_content(prompt)
                    st.write(response.text)
                    st.balloons()
                except:
                    st.error("Hubo un detalle con la conexión de Google. Revisa que tu llave en Secrets no tenga espacios.")
    else:
        st.warning("Por favor, llena los campos.")

mostrar_anuncio("BANNER INFERIOR")
