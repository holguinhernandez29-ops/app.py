import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(page_title="IA Musical Pro", layout="centered", page_icon="🎼")

# --- CONEXIÓN SEGURA CON LA LLAVE ---
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("Error: Configura la llave en los Secrets de Streamlit.")

# --- FUNCIÓN PARA PUBLICIDAD ---
def mostrar_anuncio(posicion):
    st.markdown(f"""
    <div style="text-align:center; margin: 20px 0; padding: 15px; background: #f0f2f6; border-radius: 10px; border: 1px dashed #ccc;">
        <p style="color: #666; font-size: 12px; margin: 0;">PUBLICIDAD - {posicion}</p>
    </div>
    """, unsafe_allow_html=True)

# --- DISEÑO ---
st.title("🎼 Generador de Canciones IA")
mostrar_anuncio("BANNER SUPERIOR")

col1, col2 = st.columns(2)
with col1:
    genero = st.selectbox("Género:", ["Bachata", "Corrido", "Rap", "Regional Mexicano"])
with col2:
    ritmo = st.text_input("Ritmo (opcional):", placeholder="Ej: 4/4")

tema = st.text_area("Historia:", placeholder="Ej: Amor a distancia Marissa y Alberto")

if st.button("Componer ✨", use_container_width=True):
    if tema:
        with st.spinner("Escribiendo..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"Escribe una canción de {genero} sobre: {tema}"
                response = model.generate_content(prompt)
                st.success("¡Listo!")
                st.write(response.text)
            except:
                st.error("Intenta de nuevo en un momento.")
    else:
        st.warning("Escribe una historia.")

mostrar_anuncio("BANNER INFERIOR")

