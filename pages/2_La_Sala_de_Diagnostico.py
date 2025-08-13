import streamlit as st

st.set_page_config(
    page_title="Sala de Diagnóstico",
    page_icon="💡"
)

st.title("💡 La Sala de Diagnóstico")

# --- Textos exactos de las opciones (deben ser idénticos al otro archivo) ---
Q1_OPCION_A = "Las paredes de adobe, gastadas por el sol, olían a tierra húmeda mientras la luz dorada se filtraba por la ventana, dibujando patrones en el suelo de baldosas."
Q4_OPCION_A = "Transportarte a otro mundo con detalles vívidos y sensoriales."
Q2_OPCION_A = "Siguió al sospechoso hasta el muelle, encontró la maleta y, al abrirla, descubrió el arma."
Q3_OPCION_A = "Sentí un escalofrío recorrer mi espalda. Mi mano temblaba mientras giraba el pomo helado de la puerta. No quería entrar, pero tenía que hacerlo."

# --- Descripciones de cada Estilo Narrativo ---
DESCRIPCIONES = {
    "Descriptivo": {"titulo": "Tu Estilo Dominante es: Descriptivo 🎨", "texto": "Te sumerges en los mundos a través de los sentidos...", "autores": "Virginia Woolf, Marcel Proust..."},
    "Persuasivo": {"titulo": "Tu Estilo Dominante es: Persuasivo 📣", "texto": "Buscas historias con un propósito, que te inviten a pensar...", "autores": "George Orwell, Platón..."},
    "Híbrido": {"titulo": "Tu Estilo Dominante es: Híbrido 🎨📣", "texto": "Aprecias lo mejor de dos mundos. Te encanta sumergirte en detalles...", "autores": "Ursula K. Le Guin, James Baldwin."}
}

# --- Lógica del Diagnóstico ---
if st.session_state.get('respuestas_completas', False):
    
    respuesta_q1 = st.session_state.get("q1_saved", "")
    respuesta_q2 = st.session_state.get("q2_saved", "")
    respuesta_q3 = st.session_state.get("q3_saved", "")
    respuesta_q4 = st.session_state.get("q4_saved", "")
    
    puntos_descriptivo = 0
    puntos_persuasivo = 0

    if respuesta_q1 == Q1_OPCION_A:
        puntos_descriptivo += 1
    else:
        puntos_persuasivo += 1
    
    if respuesta_q4 == Q4_OPCION_A:
        puntos_descriptivo += 1
    else:
        puntos_persuasivo += 1

    if puntos_descriptivo == 2: estilo_principal = "Descriptivo"
    elif puntos_persuasivo == 2: estilo_principal = "Persuasivo"
    else: estilo_principal = "Híbrido"

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
