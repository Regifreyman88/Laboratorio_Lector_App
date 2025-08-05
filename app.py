import streamlit as st

st.set_page_config(
    page_title="Laboratorio del Lector",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Bienvenida al Laboratorio del Lector")

# --- Portada con Video ---
# Asegúrate de haber subido tu video a GitHub con el nombre 'portada_video.mp4'.
try:
    st.video("portada_video.mp4")
except Exception:
    st.warning("Asegúrate de haber subido el video de portada 'portada_video.mp4' a tu repositorio.")

st.header("Descubre tu Estilo Narrativo Dominante")
st.write(
    """
    ¿Alguna vez te has preguntado por qué ciertas historias te atrapan más que otras? 
    ¿Prefieres las descripciones detalladas o la acción directa? ¿La voz íntima de un narrador 
    o una visión más objetiva?
    """
)
st.info(
    """
    **Instrucciones para Descubrir tu Perfil:**

    1.  Usa el **menú de la izquierda** para navegar.
    2.  Comienza tu diagnóstico en la **"Sala de Pruebas"** y responde los escenarios.
    3.  Cuando termines, ve a la **"Sala de Diagnóstico"** para ver tu resultado personalizado.
    """
)

# --- Módulo de Apoyo en la Barra Lateral ---
st.sidebar.markdown("---")
st.sidebar.header("Apoya este Proyecto")
st.sidebar.write(
    """
    Si disfrutas esta herramienta, considera apoyar su creación y mantenimiento. 
    ¡Cada contribución ayuda a mantener vivos estos espacios creativos!
    """
)
st.sidebar.link_button("Invítame un café ☕", "https://coff.ee/regifreyman8")
