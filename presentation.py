import streamlit as st

st.set_page_config(page_title="Inicio", layout="wide")

# Fondo azul con estilo
st.markdown(
    """
    <style>
    .main {
        background-color: #00008F;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Mostrar imagen con st.image()
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.image("images/logo.png", width=300)
st.markdown("<h1 style='text-align: center; color: white;'>TECH GRADUATE PROGRAM</h1>", unsafe_allow_html=True)
