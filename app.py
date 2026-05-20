import streamlit as st
if "score" not in st.session_state:
    st.session_state.score = 0

if "question_index" not in st.session_state:
    st.session_state.question_index = 0
    random.shuffle(questions)

st.title("🎤 Michael Jackson Song Trivia")
st.subheader("Pon a prueba tus conocimientos")

# Obtener pregunta actual
current_question = questions[st.session_state.question_index]

st.markdown(f"## Pregunta {st.session_state.question_index + 1}")
st.write(current_question["question"])

selected = st.radio(
    "Selecciona una respuesta:",
    current_question["options"],
    key=st.session_state.question_index
)

if st.button("Responder"):

    if selected == current_question["answer"]:
        st.success("✅ ¡Correcto!")
        st.session_state.score += 1
    else:
        st.error(
            f"❌ Incorrecto. La respuesta correcta era: {current_question['answer']}"
        )

    st.session_state.question_index += 1

    if st.session_state.question_index >= len(questions):
        st.balloons()
        st.success(
            f"🎉 Trivia terminada. Puntaje final: {st.session_state.score}/{len(questions)}"
        )

        if st.button("Jugar nuevamente"):
            st.session_state.score = 0
            st.session_state.question_index = 0
            random.shuffle(questions)
            st.rerun()
    else:
        st.rerun()

# Mostrar puntaje actual
st.sidebar.title("📊 Puntaje")
st.sidebar.metric("Puntos", st.session_state.score)
st.sidebar.metric(
    "Pregunta",
    f"{min(st.session_state.question_index + 1, len(questions))}/{len(questions)}"
)
