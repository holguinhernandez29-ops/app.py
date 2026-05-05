import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="IA Musical Pro", layout="centered")

# --- CONEXIÓN MAESTRA ---
API_KEY = "AIzaSyAQd7vtgDHInLCj2lkoOVSVtjQEfiOxa-k"

try:
    genai.configure(api_key=API_KEY)
    # Usamos la versión 'latest' que es la más compatible
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error("Error al configurar el cerebro de la IA.")

st.title("🎼 Generador de Canciones Originales")

# Publicidad
st.markdown('<div style="text-align:center; background-color:#1e2130; padding:10px; border-radius:10px; color:white; border:1px solid #444;">Espacio para Publicidad de Google AdSense</div>', unsafe_allow_html=True)

genero = st.text_input("¿Qué género quieres?", placeholder="Ej: Corrido, Rap, Trap...")
tema = st.text_area("¿De qué trata la canción?", placeholder="Escribe la historia o para quién es...")

if st.button("Componer Canción ✨"):
    if genero and tema:
        with st.spinner("Escribiendo rimas únicas..."):
            try:
                # Instrucción para que la IA no falle
                prompt = f"Escribe una canción de {genero} sobre {tema}. Estructura: Intro, Versos, Coro y Final. Que rime bien y sea larga."
                
                response = model.generate_content(prompt)
                
                if response.text:
                    st.success("¡Canción generada con éxito!")
                    st.markdown(f"### Letra de {genero}")
                    st.write(response.text)
                else:
                    st.error("La IA respondió pero sin texto. Intenta de nuevo.")
                    
            except Exception as e:
                # Si esto falla, nos dirá exactamente por qué
                st.error(f"Aviso del sistema: {str(e)}")
    else:
        st.warning("Escribe el género y el tema para empezar.")

st.markdown("---")
st.caption("Publicidad Inferior")
