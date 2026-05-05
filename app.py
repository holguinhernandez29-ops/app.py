import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Generador de Canciones Pro", layout="centered")

# --- BLOQUE DE ANUNCIO SUPERIOR ---
st.markdown("""
<div style="text-align:center; background-color:#f0f0f0; padding:10px; border-radius:5px; margin-bottom:20px;">
    <p style="color:#666; font-size:12px; margin:0;">ANUNCIO</p>
    <div style="height:90px; display:flex; align-items:center; justify-content:center; border:1px dashed #ccc;">
        <b>Espacio para Banner Publicitario</b>
    </div>
</div>
""", unsafe_allow_html=True)

st.title("🎵 Escritor de Canciones Profesional")
st.subheader("Genera letras completas con tu propio estilo")

# --- ENTRADAS DEL USUARIO ---
# Aquí tú escribes el género que quieras
genero_input = st.text_input("¿Qué género musical quieres?", placeholder="Ej: Corrido Tumbado, Rap de los 90s, Trap Bélico...")

# Aquí escribes el tema detallado
tema_input = st.text_area("¿De qué quieres que hable la canción?", placeholder="Escribe aquí la historia, nombres o detalles que quieras incluir...")

# Botón para generar
if st.button("Generar Canción Completa ✨"):
    if genero_input and tema_input:
        with st.spinner(f"Componiendo un {genero_input} sobre tu historia..."):
            time.sleep(3)
            
            st.success("¡Composición terminada!")
            st.markdown(f"### Letra: {genero_input}")
            st.divider()
            
            # Estructura de canción larga y completa
            letra_final = f"""
            **(Intro Instrumental - Estilo {genero_input})**
            
            **(Verso 1)**
            Suena el ritmo fuerte, la historia va comenzando,
            aquí les traigo los versos que se están cocinando.
            Hablamos de {tema_input}, para que vayan checando,
            que en este mundo de locos, seguimos aquí al mando.
            
            **(Verso 2)**
            Los pasos han sido largos, la vereda fue pesada,
            pero la mente está firme y la fe bien enfocada.
            No importa que el viento sople o que no tengamos nada,
            con el estilo del {genero_input}
            
