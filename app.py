import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Compositor Pro")

# CONEXIÓN
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Falta la llave en Secrets.")

st.title("🎼 Songwriter AI Pro")

genero = st.text_input("Género Musical", value="Cumbia")
tema = st.text_area("Historia", value="Alberto y Marissa amor lejano")

if st.button("Componer ✨"):
    with st.spinner("Escribiendo..."):
        try:
            # ESTA ES LA CLAVE: Usamos el modelo v1 que es el más estable
            model = genai.GenerativeModel(model_name='models/gemini-1.5-flash')
            response = model.generate_content(f"Escribe un {genero} sobre {tema}")
            st.success("¡Listo!")
            st.write(response.text)
            st.balloons()
        except Exception as e:
            st.error(f"Error de conexión. Intenta una vez más. ({e})")
            
