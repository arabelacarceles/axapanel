import streamlit as st

st.set_page_config(page_title="Inicio", layout="wide")

# Fondo blanco y estilo general
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: white;
    }
    h1 {
        color: #00008B;
        font-size: 4em;
        font-weight: bold;
        margin-bottom: 40px;
    }
    .stButton>button {
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Dos columnas: contenido izquierda / logo derecha
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.markdown("###")
    st.markdown("###")
    st.markdown("<h1>TECH GRADUATE PROGRAM</h1>", unsafe_allow_html=True)
    st.button("Sobre mí")
    st.button("Resolución del caso")
    st.button("Conclusiones")

with col2:
    st.image("images/logo.png", use_container_width=True)
