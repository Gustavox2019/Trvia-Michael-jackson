import streamlit as st
import random

# Configuración de la página
st.set_page_config(
    page_title="Michael Jackson Trivia",
    page_icon="🎤",
    layout="centered"
)

# Base de preguntas
questions = [
    {
        "question": "¿Qué canción incluye el famoso Moonwalk?",
        "options": ["Thriller", "Billie Jean", "Beat It", "Bad"],
        "answer": "Billie Jean"
    },
    {
        "question": "¿Qué canción dice 'Annie, are you okay?'",
        "options": ["Smooth Criminal", "Dangerous", "Bad", "Jam"],
        "answer": "Smooth Criminal"
    },
    {
        "question": "¿Qué canción tiene temática de zombies?",
        "options": ["Ghosts", "Thriller", "Beat It", "Heal the World"],
        "answer": "Thriller"
    },
    {
        "question": "¿Qué canción fue un himno contra la violencia callejera?",
        "options": ["Beat It", "Bad", "Black or White", "Jam"],
        "answer": "Beat It"
    },
    {
        "question": "¿Qué canción contiene el mensaje 'Make that change'?",
        "options": ["Earth Song", "Man in the Mirror", "Heal the World", "Bad"],
        "answer": "Man in the Mirror"
    },
    {
        "question": "¿Qué álbum contiene 'Black or White'?",
        "options": ["Dangerous", "Thriller", "Bad", "HIStory"],
        "answer": "Dangerous"
    },
    {
        "question": "¿Qué canción tiene el videoclip inspirado en Egipto?",
        "options": ["Remember the Time", "Thriller", "Ghosts", "Beat It"],
        "answer": "Remember the Time"
    }
]

# Inicializar variables de sesión
if "score" not in st.session_state:
    st.session_state.score = 0

if "question_index" not in st.session_state:
    st.session_state.question_index = 0
    random.shuffle(questions)

# Título
st.title("🎤 Michael Jackson Song Trivia")
st.subheader("Pon a prueba tus conocimientos")

# Verificar si aún hay preguntas
if st.session_state.question_index < len(questions):

    # Pregunta actual
    current_question = questions[st.session_state.question_index]

    st.markdown(f"## Pregunta {st.session_state.question_index + 1}")
    st.write(current_question["question"])

    # Opciones
    selected = st.radio(
        "Selecciona una respuesta:",
        current_question["options"],
        key=st.session_state.question_index
    )

    # Botón responder
    if st.button("Responder"):

        if selected == current_question["answer"]:
            st.success("✅ ¡Correcto!")
            st.session_state.score += 1
        else:
            st.error(
                f"❌ Incorrecto. La respuesta correcta era: {current_question['answer']}"
            )

        st.session_state.question_index += 1
        st.rerun()

# Final del juego
else:

    st.balloons()

    st.success(
        f"🎉 Trivia terminada. Puntaje final: "
        f"{st.session_state.score}/{len(questions)}"
    )

    # Mensaje según puntaje
    if st.session_state.score == len(questions):
        st.markdown("### 👑 ¡Eres un verdadero fan de Michael Jackson!")
    elif st.session_state.score >= 4:
        st.markdown("### 🔥 Muy buen conocimiento musical")
    else:
        st.markdown("### 🎵 Sigue escuchando a Michael Jackson")

    # Reiniciar
    if st.button("Jugar nuevamente"):
        st.session_state.score = 0
        st.session_state.question_index = 0
        random.shuffle(questions)
        st.rerun()

# Sidebar
st.sidebar.title("📊 Puntaje")
st.sidebar.metric("Puntos", st.session_state.score)

pregunta_actual = min(
    st.session_state.question_index + 1,
    len(questions)
)

st.sidebar.metric(
    "Pregunta",
    f"{pregunta_actual}/{len(questions)}"
)

st.sidebar.markdown("---")
st.sidebar.write("🎵 Trivia dedicada a Michael Jackson")
