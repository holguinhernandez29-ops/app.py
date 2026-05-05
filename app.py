import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(page_title="IA Musical Inteligente", layout="centered")

# --- AQUÍ ES DONDE PUSE TU LLAVE ---
API_KEY = "AIzaSyAQd7vtgDHInLCj2lkoOVSVtjQEfiOxa-k"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# --- DISEÑO DE LA APP ---
st.title("🎼 Generador de Canciones Originales")
st.write("Escribe el género y la historia para crear una letra única.")

# Espacio publicitario
st.markdown('<div style="text-align:center; background-color:#f0f0f0; padding:10px; border-radius:5px; border:1px solid #ddd;">ANUNCIO PUBLICITARIO</div>', unsafe_allow_html=True)

genero = st.text_input("¿Qué género musical quieres?", placeholder="Ej: Corrido, Rap, Trap...")
tema = st.text_area("¿De qué trata la canción?", placeholder="Cuéntame la historia...")

if st.button("Componer Canción Completa ✨"):
    if genero and tema:
        with st.spinner("La IA está escribiendo rimas originales..."):
            try:
                # Instrucción para la IA
                instruccion = f"Escribe una canción de {genero} muy completa y extensa. El tema es: {tema}. Incluye intro, versos detallados, coro pegajoso y un final. Que rime perfectamente."
                
                response = model.generate_content(instruccion)
                
                st.success("¡Composición terminada!")
                st.markdown(f"### Letra de {genero}")
                st.write(response.text)
                
            except Exception as e:
                st.error("Error al conectar con la IA. Intenta de nuevo.")
    else:
        st.warning("Por favor rellena ambos cuadros.")

st.markdown('<div style="text-align:center; background-color:#f0f0f0; padding:10px; border-radius:5px; border:1px solid #ddd; margin-top:30px;">ANUNCIO RELACIONADO</div>', unsafe_allow_html=True)
