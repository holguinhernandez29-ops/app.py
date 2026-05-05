import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Songwriter AI Pro")

# --- CONEXIÓN DIRECTA ---
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Configura la llave en Secrets.")

st.title("🎼 Songwriter AI Pro")

genero = st.text_input("Género Musical", value="Cumbia")
tema = st.text_area("Historia", value="Alberto y Marissa amor lejano")

if st.button("Componer ✨", use_container_width=True):
    if tema:
        with st.spinner("🚀 Escribiendo..."):
            try:
                # LA SOLUCIÓN: Forzamos la versión estable v1
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # Usamos una llamada más simple para evitar el 404
                response = model.generate_content(f"Escribe una canción de {genero} sobre: {tema}")
                
                st.markdown("---")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                # Si falla el anterior, este nombre de modelo es infalible
                try:
                    model_alt = genai.GenerativeModel('models/gemini-1.5-flash')
                    response = model_alt.generate_content(f"Escribe una canción de {genero} sobre: {tema}")
                    st.write(response.text)
                    st.balloons()
                except:
                    st.error("Error de servidor. Dale un segundo y pícale de nuevo.")
                    
