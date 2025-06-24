import streamlit as st

st.set_page_config(page_title="Inicio", layout="wide")

st.logo("images/logo.png", size="large")

# CSS para centrar absolutamente todo sin columnas
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: white;
    }
    .main-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        margin-top: 10vh;
    }
    .main-content h1 {
        color: #00008B;
        font-size: 3.5em;
        font-weight: bold;
        margin-bottom: 40px;
    }
    .button-group {
        display: flex;
        gap: 2rem;
        justify-content: center;
        flex-wrap: wrap;
    }
    </style>
""", unsafe_allow_html=True)

# HTML layout: centrado total
st.markdown('<div class="main-content">', unsafe_allow_html=True)
st.markdown('<h1>TECH GRADUATE PROGRAM</h1>', unsafe_allow_html=True)

# Botones sin columnas, centrados con flex
st.markdown('<div class="button-group">', unsafe_allow_html=True)
sobre_mi = st.button("Sobre mí")
resolucion = st.button("Resolución del caso")
conclusiones = st.button("Conclusiones")
st.markdown('</div></div>', unsafe_allow_html=True)
