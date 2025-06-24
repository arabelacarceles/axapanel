import streamlit as st

st.set_page_config(page_title="Inicio", layout="wide")

# Estilos globales
st.markdown(
    """
    <style>
    body {
        background-color: #00008B;
        color: white;
    }
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        margin-top: 20px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Contenido centrado
st.markdown('<div class="container">', unsafe_allow_html=True)
st.image("images/logo.png", width=250)
st.markdown('<div class="title">TECH GRADUATE PROGRAM</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)