import streamlit as st

st.set_page_config(
    page_title="Sala de Diagnóstico",
    page_icon="💡"
)

st.title("💡 La Sala de Diagnóstico")

# --- Definimos los textos exactos de las opciones para una comparación perfecta ---
Q1_OPCION_A = "Las paredes de adobe, gastadas por el sol, olían a tierra húmeda mientras la luz dorada se filtraba por la ventana, dibujando patrones en el suelo de baldosas."
Q4_OPCION_A = "Transportarte a otro mundo con detalles vívidos y sensoriales."
Q2_OPCION_A = "Siguió al sospechoso hasta el muelle, encontró la maleta y, al abrirla, descubrió el arma."
Q3_OPCION_A = "Sentí un escalofrío recorrer mi espalda. Mi mano temblaba mientras giraba el pomo helado de la puerta. No quería entrar, pero tenía que hacerlo."


# --- Descripciones de cada Estilo Narrativo ---
DESCRIPCIONES = {
    "Descriptivo": {
        "titulo": "Tu Estilo Dominante es: Descriptivo 🎨",
        "texto": "Te sumerges en los mundos a través de los sentidos. Para ti, una historia no es solo lo que pasa, sino dónde, cuándo y cómo se siente. Te deleitas en los detalles que pintan una imagen vívida en tu mente. Valoras la atmósfera y la inmersión por encima de todo.",
        "autores": "Virginia Woolf, Marcel Proust, Gabriel García Márquez."
    },
    "Persuasivo": {
        "titulo": "Tu Estilo Dominante es: Persuasivo 📣",
        "texto": "Buscas historias con un propósito, que te inviten a pensar y a sentir de una manera particular. Valoras las narrativas que defienden una causa, exploran una filosofía o intentan cambiar tu forma de ver el mundo.",
        "autores": "George Orwell, Platón, Ayn Rand."
    },
    "Híbrido": {
        "titulo": "Tu Estilo Dominante es: Híbrido (Descriptivo y Persuasivo) 🎨📣",
        "texto": "Aprecias lo mejor de dos mundos. Te encanta sumergirte en un ambiente rico en detalles, pero también necesitas que la historia tenga un propósito o un mensaje que te haga reflexionar.",
        "autores": "Ursula K. Le Guin, James Baldwin."
    }
}

# --- Lógica del Diagnóstico ---

if st.session_state.get('respuestas_completas', False):
    
    # Leemos las respuestas de forma segura
    respuesta_q1 = st.session_state.get("q1", "")
    respuesta_q2 = st.session_state.get("q2", "")
    respuesta_q3 = st.session_state.get("q3", "")
    respuesta_q4 = st.session_state.get("q4", "")
    
    puntos_descriptivo = 0
    puntos_persuasivo = 0

    # CORRECCIÓN: Comparamos la respuesta completa para ser exactos
    if respuesta_q1 == Q1_OPCION_A:
        puntos_descriptivo += 1
    else:
        puntos_persuasivo += 1
    
    if respuesta_q4 == Q4_OPCION_A:
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
    estructura = "Lineal" if respuesta_q2 == Q2_OPCION_A else "No Lineal"
    punto_de_vista = "Primera Persona" if respuesta_q3 == Q3_OPCION_A else "Tercera Persona"

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

else:
    st.warning("⚠️ Primero debes completar el cuestionario en la 'Sala de Pruebas' y hacer clic en 'Analizar' para recibir tu diagnóstico.")
    st.link_button("Ir a la Sala de Pruebas", "/La_Sala_de_Pruebas")
