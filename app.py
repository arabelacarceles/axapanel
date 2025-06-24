import streamlit as st

st.set_page_config(page_title="Inicio", layout="wide")

# Fondo azul y centrado vertical
st.markdown(
    """
    <style>
    body {
        background-color: #00008F;
        color: blue;
    }
    .centered {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Contenido
st.markdown('<div class="centered">', unsafe_allow_html=True)
st.image("images/logo.png", width=300)
st.markdown("<h1 style='color: white;'>TECH GRADUATE PROGRAM</h1>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
