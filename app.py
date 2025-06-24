import streamlit as st

st.set_page_config(page_title="Inicio", layout="wide")

# CSS: fondo azul, sin scroll, centrado total
st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
        background-color: #00008B;
        height: 100vh;
        overflow: hidden;
    }
    .centered {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    h1 {
        color: white;
        font-size: 2.5rem;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Contenido
st.markdown('<div class="centered">', unsafe_allow_html=True)
st.image("images/logo.png", width=300)
st.markdown("<h1>TECH GRADUATE PROGRAM</h1>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
