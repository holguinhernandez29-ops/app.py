import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="IA Musical Pro", layout="centered")

# --- CONEXIÓN CON LLAVE ---
API_KEY = "AIzaSyAQd7vtgDHInLCj2lkoOVSVtjQEfiOxa-k"
genai.configure(api_key=API_KEY)

st.title("🎼 Generador de Canciones Originales")

# Publicidad
st.markdown('<div style="text-align:center; background-color:#1e2130; padding:10px; border-radius:10px; color:white;">Espacio para Publicidad de Google AdSense</div>', unsafe_allow_html=True)

genero = st.text_input("¿Qué género quieres?", placeholder="Ej: Corrido, Rap...")
tema = st.text_area("¿De qué trata la canción?", placeholder="Escribe la historia aquí...")

if st.button("Componer Canción ✨"):
    if genero and tema:
        with st.spinner("Buscando rimas..."):
            # LISTA DE MODELOS A PROBAR (Uno tiene que funcionar)
            modelos_a_probar = ["gemini-1.5-flash", "gemini-pro", "models/gemini-1.5-flash", "models/gemini-pro"]
            exito = False
            
            for nombre_modelo in modelos_a_probar:
                try:
                    model = genai.GenerativeModel(nombre_modelo)
                    prompt = f"Escribe una canción completa de {genero} sobre {tema}. Estructura: Intro, Versos, Coro y Final. Que rime bien."
                    response = model.generate_content(prompt)
                    
                    if response.text:
                        st.success(f"¡Listo! (Usando {nombre_modelo})")
                        st.markdown(response.text)
                        exito = True
                        break # Si funciona, salimos del ciclo
                except:
                    continue # Si falla, brinca al siguiente nombre
            
            if not exito:
                st.error("El servidor de Google está saturado o no reconoce los nombres. Intenta de nuevo en un minuto.")
    else:
        st.warning("Llena los campos.")

st.markdown("---")
st.caption("Publicidad Inferior")
