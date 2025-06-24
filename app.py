import streamlit as st

st.set_page_config(page_title="Inicio", layout="centered")

# Logo de la cabecera
st.logo("images/logo.png", size="large")

# Fondo azul para el cuerpo
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #00008B;
    }
    h1 {
        text-align: center;
        color: white;
        font-size: 2.5em;
        margin-top: 3vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título
st.markdown("<h1>TECH GRADUATE PROGRAM</h1>", unsafe_allow_html=True)
