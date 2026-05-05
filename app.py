import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(page_title="IA Musical Pro", layout="centered", page_icon="🎼")

# --- CONEXIÓN SEGURA CON LA LLAVE ---
try:
    # Esto toma la llave de la "Caja Fuerte" de Streamlit
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("Error: No se encontró la llave en los Secrets de Streamlit.")

# --- FUNCIÓN PARA MOSTRAR PUBLICIDAD ---
def mostrar_anuncio(posicion):
    # Aquí es donde pegarás el código que te dé AdSense después
    # Por ahora, dejamos el espacio listo y estético
    st.markdown(f"""
    <div style="text-align:center; margin: 20px 0; padding: 15px; background: #f0f2f6; border-radius: 10px; border: 1px dashed #ccc;">
        <p style="color: #666; font-size: 12px; margin: 0;">PUBLICIDAD - {posicion}</p>
        </div>
    """, unsafe_allow_html=True)

# --- DISEÑO DE LA APP ---
st.title("🎼 Generador de Canciones IA")
st.subheader("Crea letras originales en segundos")

mostrar_anuncio("BANNER SUPERIOR")

# Entradas del usuario
col1, col2 = st.columns(2)
with col1:
    genero = st.selectbox("Elige el género:", ["Corrido", "Rap", "Bachata", "Reggaeton", "Regional Mexicano", "Pop"])
with col2:
    ritmo = st.text_input("Ritmo (opcional):", placeholder="Ej: 3/4,
                          
