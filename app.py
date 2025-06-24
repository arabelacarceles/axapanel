import streamlit as st

st.set_page_config(page_title="Inicio", layout="centered")

# CSS para fondo azul total
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #00008B;
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

# Contenido centrado
st.markdown('<div class="centered">', unsafe_allow_html=True)
st.image("images/logo.png", width=300)
st.markdown("<h1 style='color: white;'>TECH GRADUATE PROGRAM</h1>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
