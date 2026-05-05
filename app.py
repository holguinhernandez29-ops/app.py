import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Creador Musical Pro", layout="centered")

# --- ANUNCIO SUPERIOR ---
st.markdown("""
<div style="text-align:center; background-color:#f9f9f9; padding:10px; border-radius:10px; border:1px solid #ddd; margin-bottom:20px;">
    <p style="color:#888; font-size:11px; margin:0;">PUBLICIDAD</p>
    <div style="height:90px; display:flex; align-items:center; justify-content:center;">
        <span style="color:#aaa;">Banner Publicitario</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.title("🎼 Generador de Letras Profesional")
st.write("Escribe el género y el tema para crear una canción completa.")

# --- ENTRADAS PERSONALIZADAS ---
# Aquí puedes escribir el género que tú quieras
genero_personalizado = st.text_input("¿Qué género musical quieres?", placeholder="Ej: Corrido Tumbado, Rap Malandro, Balada...")

# Aquí escribes la historia o el tema
tema = st.text_area("¿De qué trata la canción?", placeholder="Ej: De un joven que empezó cuidando vacas y ahora tiene sus propios negocios...")

# Botón de acción
if st.button("Generar Letra Completa 🎤"):
    if genero_personalizado and tema:
        with st.spinner(f"Componiendo tu {genero_personalizado}..."):
            time.sleep(3) # Simulación de proceso
            
            st.success("¡Composición terminada!")
            st.divider()
            
            # Estructura de canción larga
            st.markdown(f"### Letra de {genero_personalizado}")
            
            letra = f"""
            **(Introducción)**
            (Ritmo marcado de {genero_personalizado} empieza a sonar...)
            
            **(Verso 1)**
            En las calles se comenta lo que el hombre ha pasado,
            desde abajo comenzó y el destino le ha cambiado.
            Con el tema de {tema},
            aquí les traigo la historia que el tiempo ha guardado.
            
            **(Coro - Fuerte)**
            Y que suene la música, que no pare el sonido,
            por todo lo logrado y lo que hemos vivido.
            Es el {genero_personalizado} que traigo en el alma,
            siempre con respeto, manteniendo la calma.
            
            **(Verso 2)**
            Los amigos son pocos, pero son de verdad,
            en los tiempos difíciles se ve la lealtad.
            Hablamos de {tema} con mucha sinceridad,
            porque la palabra vale más que la cantidad.
            
            **(Puente / Mambo / Solo)**
            (Arreglos musicales intensos...)
            
            **(Verso 3)**
            Ya me voy despidiendo, pero aquí les dejé,
            los versos humildes de lo que ayer soñé.
            Con este {genero_personalizado} yo me levantaré,
            y el nombre de Chihuahua siempre en alto pondré.
            
            **(Final)**
            (El ritmo se va apagando poco
            
