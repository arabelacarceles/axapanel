import streamlit as st

st.set_page_config(page_title="Inicio", layout="centered")

st.logo("images/logo.png", size="large")

# CSS para fondo, título centrado, botones centrados
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
    }
    .main-content h1 {
        text-align: center;
        color: #00008B;
        font-size: 3.5em;
        font-weight: bold;
        margin: 5vh 0 3vh 0;
    }
    .button-row {
        display: flex;
        gap: 2rem;
        justify-content: center;
        margin-top: 2vh;
    }
    </style>
""", unsafe_allow_html=True)

# Contenido estructurado y centrado
st.markdown('<div class="main-content">', unsafe_allow_html=True)
st.markdown('<h1>TECH GRADUATE PROGRAM</h1>', unsafe_allow_html=True)

# Botones centrados horizontalmente
st.markdown('<div class="button-row">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    sobre_mi = st.button("Sobre mí")
with col2:
    resolucion = st.button("Resolución del caso")
with col3:
    conclusiones = st.button("Conclusiones")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
