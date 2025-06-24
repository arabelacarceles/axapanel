import streamlit as st

st.set_page_config(page_title="Inicio", layout="centered")

# CSS: fondo azul, sin forzar altura fija
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #00008B;
    }
    .centered {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-top: 10vh;
    }
    h1 {
        color: white;
        font-size: 2.5em;
        margin-top: 2vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Contenido centrado
st.markdown('<div class="centered">', unsafe_allow_html=True)
st.image("images/logo.png", width=300)
st.markdown("<h1 style='color: white;'>TECH GRADUATE PROGRAM</h1>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
