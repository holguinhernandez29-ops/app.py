import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="IA Musical Pro", layout="centered")

# --- TU LLAVE MAESTRA ---
API_KEY = "AIzaSyAQd7vtgDHInLCj2lkoOVSVtjQEfiOxa-k"

try:
    genai.configure(api_key=API_KEY)
    # Usamos solo el nombre del modelo, sin el prefijo "models/"
    # Esto soluciona el error 404 en la mayoría de los casos
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error("Error al conectar con el cerebro de la IA.")

st.title("🎼 Generador de Canciones Originales")

# Publicidad
st.markdown('<div style="text-align:center; background-color:#1e2130; padding:10px; border-radius:10px; color:white;">Espacio para Publicidad de Google AdSense</div>', unsafe_allow_html=True)

genero = st.text_input("¿Qué género quieres?", placeholder="Ej: Corrido, Rap, Trap...")
tema = st.text_area("¿De qué trata la canción?", placeholder="Escribe la historia o para quién es...")

if st.button("Componer Canción ✨"):
    if genero and tema:
        with st.spinner("Escribiendo rimas únicas..."):
            try:
                # Instrucción directa
                prompt = f"Escribe una canción completa de {genero} sobre {tema}. Estructura: Intro, Versos, Coro y Final. Que rime bien y sea larga."
                
                response = model.generate_content(prompt)
                
                if response.text:
                    st.success("¡Canción generada!")
                    st.markdown(f"### Letra de {genero}")
                    st.write(response.text)
                else:
                    st.error("La IA no pudo generar el texto.")
                    
            except Exception as e:
                # Si esto vuelve a fallar, intentamos con el nombre viejo pero sin prefijo
                try:
                    model_alt = genai.GenerativeModel("gemini-pro")
                    response = model_alt.generate_content(prompt)
                    st.success("¡Canción generada (Modo Respaldo)!")
                    st.write(response.text)
                except:
                    st.error(f"Aviso del sistema: {str(e)}")
    else:
        st.warning("Escribe el género y el tema.")

st.markdown("---")
st.caption("Publicidad Inferior")
