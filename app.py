import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="IA Musical Pro", page_icon="🎵")

# --- ESPACIO PARA ANUNCIO (Superior) ---
# Aquí es donde pegarás el código de Google AdSense después
st.markdown('<div style="text-align: center; color: gray; font-size: 12px;">ANUNCIO</div>', unsafe_allow_html=True)
st.components.v1.html("""
    <div style="background-color: #f0f0f0; height: 90px; display: flex; align-items: center; justify-content: center; border: 1px dashed #ccc;">
        <p style="color: #999;">Banner Publicitario 728x90</p>
    </div>
""", height=100)

# --- TÍTULO E INTERFAZ ---
st.title("🎵 Asistente Creativo para Músicos")
st.write("Genera letras, rimas e ideas para tus próximas canciones.")

col1, col2 = st.columns(2)

with col1:
    genero = st.selectbox("Elige el género", ["Rap", "Corrido", "Reggaeton", "Romántica"])
with col2:
    tema = st.text_input("¿De qué trata la canción?", "Amor y fortuna")

# --- BOTÓN DE ACCIÓN ---
if st.button("Generar Letra Mágica ✨"):
    with st.spinner('La IA está componiendo...'):
        # Aquí conectaríamos con el modelo de IA
        # Por ahora te pongo un ejemplo de cómo saldría el resultado:
        st.success(f"Aquí tienes una idea para tu {genero}:")
        st.code(f"""
        Caminando por las calles con la suerte de mi lado,
        buscando ese destino que el tiempo me ha guardado.
        Con rimas en el alma y el ritmo en el corazón,
        escribo esta letra que hoy se vuelve mi canción.
        """, language="text")

# --- ESPACIO PARA ANUNCIO (Lateral o Inferior) ---
st.sidebar.title("Patrocinadores")
st.sidebar.info("¿Quieres anunciar tu estudio de grabación aquí?")
st.sidebar.markdown("---")

st.markdown("---")
st.components.v1.html("""
    <div style="background-color: #f0f0f0; height: 250px; display: flex; align-items: center; justify-content: center; border: 1px dashed #ccc;">
        <p style="color: #999;">Anuncio Cuadrado 300x250</p>
    </div>
""", height=260)
