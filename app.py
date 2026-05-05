if st.button("Componer Canción ✨", use_container_width=True):
    if genero and tema:
        with st.spinner("🚀 Escribiendo..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"Escribe un {genero} sobre {tema}")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                # ESTO NOS DIRÁ EL ERROR REAL
                st.error(f"Error detallado de Google: {e}")
    else:
        st.warning("Escribe el género y la historia.")
         
