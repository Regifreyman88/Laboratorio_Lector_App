import streamlit as st

st.set_page_config(
    page_title="Sala de Pruebas",
    page_icon="🧪"
)

st.title("🧪 La Sala de Pruebas")
st.write("Responde a los siguientes escenarios eligiendo la opción que te atrape más como lector/a. No hay respuestas correctas, solo preferencias.")

# --- Textos exactos de las opciones ---
# Definimos los textos aquí para asegurar que sean idénticos en ambos archivos.
Q1_OPCION_A = "Las paredes de adobe, gastadas por el sol, olían a tierra húmeda mientras la luz dorada se filtraba por la ventana, dibujando patrones en el suelo de baldosas."
Q1_OPCION_B = "Debes visitar este lugar; es un santuario donde cada rincón te convence de que la belleza aún puede salvar al mundo. Sentirás una paz que no encontrarás en ningún otro sitio."

Q2_OPCION_A = "Siguió al sospechoso hasta el muelle, encontró la maleta y, al abrirla, descubrió el arma."
Q2_OPCION_B = "El arma brillaba bajo la luz. ¿Cómo había llegado hasta aquí? Tres días antes, en el bar, una conversación sin importancia ahora cobraba un nuevo y siniestro significado."

Q3_OPCION_A = "Sentí un escalofrío recorrer mi espalda. Mi mano temblaba mientras giraba el pomo helado de la puerta. No quería entrar, pero tenía que hacerlo."
Q3_OPCION_B = "Él sintió un escalofrilo recorrer su espalda. Su mano temblaba mientras giraba el pomo helado de la puerta. No quería entrar, pero tenía que hacerlo."

Q4_OPCION_A = "Transportarte a otro mundo con detalles vívidos y sensoriales."
Q4_OPCION_B = "Hacerte reflexionar sobre una idea o convencerte de una verdad profunda."

# --- Preguntas del Cuestionario ---

st.markdown("---")
st.subheader("Escenario 1: Tu Lugar Favorito")
q1 = st.radio("Estás describiendo tu lugar favorito...", [Q1_OPCION_A, Q1_OPCION_B], index=None, key="q1")

st.markdown("---")
st.subheader("Escenario 2: La Pista del Detective")
q2 = st.radio("Un detective encuentra una pista crucial...", [Q2_OPCION_A, Q2_OPCION_B], index=None, key="q2")

st.markdown("---")
st.subheader("Escenario 3: La Casa Encantada")
q3 = st.radio("El protagonista está a punto de entrar en una casa encantada...", [Q3_OPCION_A, Q3_OPCION_B], index=None, key="q3")

st.markdown("---")
st.subheader("Escenario 4: El Objetivo de la Narración")
q4 = st.radio("¿Cuál crees que es el propósito principal de una buena historia?", [Q4_OPCION_A, Q4_OPCION_B], index=None, key="q4")

# --- Botón para ver resultados ---
st.markdown("---")
if st.button("Analizar mi Estilo Narrativo", type="primary"):
    if q1 and q2 and q3 and q4:
        st.session_state['q1_saved'] = q1
        st.session_state['q2_saved'] = q2
        st.session_state['q3_saved'] = q3
        st.session_state['q4_saved'] = q4
        st.session_state['respuestas_completas'] = True
        st.success("¡Análisis completado! Ve a la 'Sala de Diagnóstico' para ver tu resultado.")
        st.balloons()
    else:
        st.warning("Por favor, responde todas las preguntas para poder analizar tu estilo.")
