import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Songwriter Pro", layout="centered", page_icon="🎼")

# --- CONEXIÓN DIRECTA ---
try:
    # Intentamos jalar la llave de los secretos
    key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=key)
except Exception as e:
    st.error("Error de configuración. Por favor, contacta al administrador.")

st.title("🎼 Songwriter AI Pro")

# Publicidad sencilla
st.markdown('<div style="text-align:center; background:#f0f2f6; padding:10px; border-radius:5px; font-size:12px; color:#888;">ANUNCIO</div>', unsafe_allow_html=True)

genero = st.text_input("Género Musical")
tema = st.text_area("Historia/Detalles")

if st.button("Componer ✨", use_container_width=True):
    if genero and tema:
        with st.spinner("Escribiendo..."):
            try:
                # Usamos el modelo más estable de todos
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = f"Escribe la letra de una canción de {genero} sobre: {tema}. Incluye Intro, Versos y Coro."
                
                response = model.generate_content(prompt)
                
                if response.text:
                    st.markdown("### Letra:")
                    st.write(response.text)
                    st.balloons()
            except Exception as e:
                # Este mensaje te dirá qué está pasando realmente sin asustar al usuario
                st.error("Servidor ocupado. Por favor intenta en 1 minuto.")
                # Solo para que tú lo veas en la consola si es necesario
                print(f"DEBUG: {e}")
    else:
        st.warning("Llena los datos.")
        
