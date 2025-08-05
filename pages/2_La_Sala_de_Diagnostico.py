import streamlit as st

st.set_page_config(
    page_title="Sala de Diagnóstico",
    page_icon="💡"
)

st.title("💡 La Sala de Diagnóstico")

# --- Descripciones de cada Estilo Narrativo ---
# Basado en el artículo de Indeed.com
DESCRIPCIONES = {
    "Descriptivo": {
        "titulo": "Tu Estilo Dominante es: Descriptivo 🎨",
        "texto": "Te sumerges en los mundos a través de los sentidos. Para ti, una historia no es solo lo que pasa, sino dónde, cuándo y cómo se siente. Te deleitas en los detalles que pintan una imagen vívida en tu mente, desde el color de un atardecer hasta la textura de una pared. Valoras la atmósfera y la inmersión por encima de todo.",
        "autores": "Virginia Woolf, Marcel Proust, Gabriel García Márquez."
    },
    "Persuasivo": {
        "titulo": "Tu Estilo Dominante es: Persuasivo 📣",
        "texto": "Buscas historias con un propósito, que te inviten a pensar y a sentir de una manera particular. No solo quieres entretenimiento, quieres un argumento, una idea que te desafíe o una emoción que te transforme. Valoras las narrativas que defienden una causa, exploran una filosofía o intentan cambiar tu forma de ver el mundo.",
        "autores": "George Orwell, Platón, Ayn Rand."
    },
    "Híbrido": {
        "titulo": "Tu Estilo Dominante es: Híbrido (Descriptivo y Persuasivo) 🎨📣",
        "texto": "Aprecias lo mejor de dos mundos. Te encanta sumergirte en un ambiente rico en detalles, pero también necesitas que la historia tenga un propósito o un mensaje que te haga reflexionar. Buscas tanto la belleza de la forma como la profundidad del contenido.",
        "autores": "Ursula K. Le Guin, James Baldwin."
    }
}

# --- Lógica del Diagnóstico ---

# Verificar si el usuario ha respondido todas las preguntas
if 'q1' not in st.session_state or 'q2' not in st.session_state or 'q3' not in st.session_state or 'q4' not in st.session_state:
    st.warning("⚠️ Primero debes completar el cuestionario en la 'Sala de Pruebas' para recibir tu diagnóstico.")
    st.link_button("Ir a la Sala de Pruebas", "/La_Sala_de_Pruebas")
else:
    # Contar los puntos para el estilo principal
    puntos_descriptivo = 0
    puntos_persuasivo = 0

    if "Las paredes de adobe" in st.session_state.q1:
        puntos_descriptivo += 1
    else:
        puntos_persuasivo += 1
    
    if "Transportarte a otro mundo" in st.session_state.q4:
        puntos_descriptivo += 1
    else:
        puntos_persuasivo += 1

    # Determinar el estilo principal
    if puntos_descriptivo == 2:
        estilo_principal = "Descriptivo"
    elif puntos_persuasivo == 2:
        estilo_principal = "Persuasivo"
    else:
        estilo_principal = "Híbrido"

    # Determinar características secundarias
    estructura = "Lineal" if "Siguió al sospechoso" in st.session_state.q2 else "No Lineal"
    punto_de_vista = "Primera Persona" if "Sentí un escalofrío" in st.session_state.q3 else "Tercera Persona"

    # --- Mostrar los Resultados ---
    st.header("Tu Perfil de Lector")

    resultado = DESCRIPCIONES[estilo_principal]
    st.success(resultado["titulo"])
    st.write(resultado["texto"])
    st.caption(f"**Autores que te podrían gustar:** {resultado['autores']}")
    
    st.markdown("---")
    
    st.subheader("Características Secundarias de tu Estilo:")
    st.markdown(f"- **Estructura Preferida:** `{estructura}`")
    st.markdown(f"- **Punto de Vista Preferido:** `{punto_de_vista}`")
