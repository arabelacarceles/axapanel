import streamlit as st

st.set_page_config(page_title="Inicio", layout="centered")

# Fondo azul oscuro y estilo general
st.markdown(
    """
    <style>
    .main {
        background-color: #00008B;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Página centrada con logo e introducción
st.markdown(
    """
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh;">
        <img src="images/logo.png" style="width: 300px;">
        <h1 style="color: white; margin-top: 20px;">TECH GRADUATE PROGRAM</h1>
    </div>
    """,
    unsafe_allow_html=True
)
