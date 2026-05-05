import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="IA Musical Pro", layout="centered")

# Tu llave que ya tenemos
API_KEY = "AIzaSyAQd7vtgDHInLCj2lkoOVSVtjQEfiOxa-k"
genai.configure(api_key=API_KEY)

st.title("🎼 Generador de Canciones")
st.markdown('<div style="text-align:center; background-color:#1e2130; padding:10px; border-radius:10px; color:white;">ESPACIO PUBLICITARIO</div>', unsafe_allow_html=True)

genero = st.text_input("Género musical:")
tema = st.text_area("Historia de la canción:")

if st.button("Componer ✨"):
    if genero and tema:
        with st.spinner("La IA está buscando el mejor camino para escribir..."):
            try:
                # TRUCO FINAL: Listamos los modelos y agarramos el primero que genere contenido
                modelos_disponibles = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                
                # Intentamos con el primero de la lista (suele ser el más nuevo)
                model = genai.GenerativeModel(modelos_disponibles[0])
                
                prompt = f"Escribe una canción de {genero} sobre {tema}. Que sea larga, con rimas, intro, versos y coro."
                response = model.generate_content(prompt)
                
                st.success("¡Lo logramos!")
                st.write(response.text)
            except Exception as e:
                st.error("El sistema está actualizando. Dale un minuto y presiona 'Componer' otra vez.")
    else:
        st.warning("Faltan datos.")

st.markdown("---")
st.caption("Publicidad Inferior")
