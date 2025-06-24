import streamlit as st

st.set_page_config(page_title="Inicio", layout="centered")

# Mostrar logo arriba a la izquierda (logo AXA grande)
st.logo("images/logo.png", size="large")

# CSS para centrar contenido y estilizar texto/botones
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: white;
    }
    .title {
        text-align: center;
        color: #00008B;
        font-size: 3.5em;
        font-weight: bold;
        margin-top: 5vh;
        margin-bottom: 5vh;
    }
    .button-container {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-top: 4vh;
    }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<div class="title">TECH GRADUATE PROGRAM</div>', unsafe_allow_html=True)

# Botones
col1, col2, col3 = st.columns(3)
with col1:
    sobre_mi = st.button("Sobre mí")
with col2:
    resolucion = st.button("Resolución del caso")
with col3:
    conclusiones = st.button("Conclusiones")
