import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Compositor AI", layout="centered", page_icon="🎼")

# Conexión Segura
try:
    # Intentamos obtener la llave de los Secrets
    if "GOOGLE_API_KEY" in st.secrets:
        key = st.secrets["GOOGLE_API_KEY"]
        genai.configure(api_key=key)
    else:
        st.error("⚠️ Falta la llave GOOGLE_API_KEY en los Secrets de Streamlit.")
except Exception as e:
    st.error(f"❌ Error de configuración: {e}")

st.title("🎼 Generador de Canciones")

genero = st.text_input("Género Musical:", placeholder="Ej: Corrido, Bachata, Rap...")
tema = st.text_area("Historia de la canción:", placeholder="Ej: Alberto y Marissa...")

if st.button("Componer ✨", use_container_width=True):
    if genero and tema:
        with st.spinner("Escribiendo..."):
            try:
                # Intentamos con el modelo Pro (más inteligente)
                model = genai.GenerativeModel('gemini-1.5-pro')
                prompt = f"Escribe la letra de una canción de {genero} sobre: {tema}. Incluye intro, versos y coro."
                
                response = model.generate_content(prompt)
                
                if response.text:
                    st.subheader("Tu Letra:")
                    st.write(response.text)
                    st.balloons()
            except:
                try:
                    # Si el Pro falla, intentamos con el Flash (más rápido)
                    model_flash = genai.GenerativeModel('gemini-1.5-flash')
                    response_flash = model_flash.generate_content(prompt)
                    st.subheader("Tu Letra:")
                    st.write(response_flash.text)
                except Exception as e:
                    st.error("No se pudo conectar con la IA. Revisa que tu llave API sea correcta y no tenga restricciones.")
    else:
        st.warning("Por favor rellena los campos.")
        
