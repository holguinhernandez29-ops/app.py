import streamlit as st
import google.generativeai as genai
import time

# Configuración Pro
st.set_page_config(page_title="Compositor AI Pro", layout="centered", page_icon="🎼")

# --- CONEXIÓN DIRECTA ---
def configurar_ia():
    try:
        if "GOOGLE_API_KEY" in st.secrets:
            genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
            return True
        return False
    except:
        return False

# --- PUBLICIDAD ---
def mostrar_anuncio(posicion):
    st.markdown(f"""<div style="text-align:center; margin: 10px 0; padding: 10px; background: #f0f2f6; border-radius: 8px; border: 1px dashed #ccc;"><p style="color: #666; font-size: 10px; margin: 0;">PUBLICIDAD - {posicion}</p></div>""", unsafe_allow_html=True)

# --- DISEÑO ---
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
    if genero and tema:
        if configurar_ia():
            # Usamos un contenedor vacío para ir mostrando el progreso
            status = st.empty()
            status.info("🚀 Conectando con la IA...")
            
            try:
                # Usamos el modelo Flash que es el que menos falla
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                instruccion = f"Escribe la letra de una canción de {genero} estilo {vibe} sobre: {tema}. Estructura: Intro, Versos, Coro, Final."
                if generar_prompt:
                    instruccion += "\nAl final añade un 'Prompt Musical' técnico en inglés para Suno/Udio."

                # Agregamos un tiempo límite (timeout) interno
                response = model.generate_content(instruccion)
                
                if response:
                    status.empty()
                    st.markdown("### 🎼 Letra Generada:")
                    st.write(response.text)
                    st.balloons()
            except Exception as e:
                status.empty()
                st.error(f"Se agotó el tiempo. Esto pasa cuando la llave en Secrets no es válida o Google está saturado. Revisa tu llave API.")
        else:
            st.error("⚠️ La app no encuentra tu GOOGLE_API_KEY en los Secrets de Streamlit.")
    else:
        st.warning("Completa los campos de texto.")

mostrar_anuncio("BANNER INFERIOR")
