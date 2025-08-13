import streamlit as st

st.set_page_config(
    page_title="Sala de Pruebas",
    page_icon="🧪"
)

st.title("🧪 La Sala de Pruebas")
st.write("Responde a los siguientes escenarios eligiendo la opción que te atrape más como lector/a. No hay respuestas correctas, solo preferencias.")

# --- Preguntas del Cuestionario ---

st.markdown("---")
st.subheader("Escenario 1: Tu Lugar Favorito")
# CORRECCIÓN: Se añade 'index=None' para que ninguna opción esté seleccionada al inicio.
q1 = st.radio(
    "Estás describiendo tu lugar favorito. ¿Qué frase te representa más?",
    (
        "Las paredes de adobe, gastadas por el sol, olían a tierra húmeda mientras la luz dorada se filtraba por la ventana, dibujando patrones en el suelo de baldosas.",
        "Debes visitar este lugar; es un santuario donde cada rincón te convence de que la belleza aún puede salvar al mundo. Sentirás una paz que no encontrarás en ningún otro sitio."
    ),
    index=None, # <--- ESTA ES LA CORRECCIÓN
    key="q1"
)

st.markdown("---")
st.subheader("Escenario 2: La Pista del Detective")
q2 = st.radio(
    "Un detective encuentra una pista crucial. ¿Cómo prefieres que te lo cuenten?",
    (
        "Siguió al sospechoso hasta el muelle, encontró la maleta y, al abrirla, descubrió el arma.",
        "El arma brillaba bajo la luz. ¿Cómo había llegado hasta aquí? Tres días antes, en el bar, una conversación sin importancia ahora cobraba un nuevo y siniestro significado."
    ),
    index=None, # <--- ESTA ES LA CORRECCIÓN
    key="q2"
)

st.markdown("---")
st.subheader("Escenario 3: La Casa Encantada")
q3 = st.radio(
    "El protagonista está a punto de entrar en una casa encantada. ¿Qué te atrapa más?",
    (
        "Sentí un escalofrío recorrer mi espalda. Mi mano temblaba mientras giraba el pomo helado de la puerta. No quería entrar, pero tenía que hacerlo.",
        "Él sintió un escalofrilo recorrer su espalda. Su mano temblaba mientras giraba el pomo helado de la puerta. No quería entrar, pero tenía que hacerlo."
    ),
    index=None, # <--- ESTA ES LA CORRECCIÓN
    key="q3"
)

st.markdown("---")
st.subheader("Escenario 4: El Objetivo de la Narración")
q4 = st.radio(
    "¿Cuál crees que es el propósito principal de una buena historia?",
    (
        "Transportarte a otro mundo con detalles vívidos y sensoriales.",
        "Hacerte reflexionar sobre una idea o convencerte de una verdad profunda."
    ),
    index=None, # <--- ESTA ES LA CORRECCIÓN
    key="q4"
)


# --- Botón para ver resultados ---
st.markdown("---")
if st.button("Analizar mi Estilo Narrativo", type="primary"):
    if st.session_state.q1 and st.session_state.q2 and st.session_state.q3 and st.session_state.q4:
        st.session_state['respuestas_completas'] = True
        st.success("¡Análisis completado! Ve a la 'Sala de Diagnóstico' para ver tu resultado.")
        st.balloons()
    else:
        st.warning("Por favor, responde todas las preguntas para poder analizar tu estilo.")
