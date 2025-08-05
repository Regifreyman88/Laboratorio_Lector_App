import streamlit as st

st.set_page_config(page_title="Biblioteca de Estilos", page_icon="📚")
st.title("📚 Biblioteca de Estilos Narrativos")
st.write("Explora las diferentes herramientas que usan los escritores para contar sus historias.")

st.markdown("---")

with st.expander("🎨 Estilo Descriptivo"):
    st.image("descriptivo.png", use_container_width=True)
    st.write("**Objetivo:** Pintar una imagen vívida en la mente del lector usando detalles sensoriales.")

with st.expander("📣 Estilo Persuasivo"):
    st.image("persuasivo.png", use_container_width=True)
    st.write("**Objetivo:** Convencer al lector de una idea, argumento u opinión.")

with st.expander("👤 Punto de Vista (Primera vs. Tercera Persona)"):
    st.image("puntodevista.png", use_container_width=True)
    st.write("**Primera Persona ('Yo'):** El narrador es un personaje dentro de la historia. Crea una conexión íntima y personal.")
    st.write("**Tercera Persona ('Él/Ella'):** El narrador está fuera de la historia. Ofrece una visión más amplia y objetiva.")

with st.expander("⏳ Estructura Narrativa (Lineal vs. No Lineal)"):
    st.image("narrativo.png", use_container_width=True)
    st.write("**Lineal:** La historia se cuenta en orden cronológico, de principio a fin.")
    st.write("**No Lineal:** La historia salta en el tiempo, usando flashbacks o flashforwards.")
    
with st.expander("ℹ️ Estilo Expositivo"):
    st.image("expositivo.png", use_container_width=True)
    st.write("**Objetivo:** Explicar hechos, dar información o definir conceptos de forma clara y directa.")
