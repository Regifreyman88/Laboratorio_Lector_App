import streamlit as st

st.set_page_config(
    page_title="Laboratorio del Lector",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Bienvenida al Laboratorio del Lector")

# Usando el video de portada
try:
    st.video("portada_video.mp4")
except Exception:
    st.warning("Asegúrate de haber subido el video 'portada_video.mp4'.")

st.header("Descubre tu Estilo Narrativo Dominante")
st.info(
    """
    **Instrucciones:**
    1.  Usa el **menú de la izquierda** para navegar.
    2.  Comienza tu diagnóstico en la **"Sala de Pruebas"**.
    3.  Cuando termines, ve a la **"Sala de Diagnóstico"** para ver tu resultado.
    4.  Explora la **"Biblioteca de Estilos"** para aprender más.
    """
)

# Módulo de Apoyo en la Barra Lateral
st.sidebar.markdown("---")
st.sidebar.header("Apoya este Proyecto")
st.sidebar.write("Si disfrutas esta herramienta, considera apoyar su creación.")
st.sidebar.link_button("Invítame un café ☕", "https://coff.ee/regifreyman8")
