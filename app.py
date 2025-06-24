import streamlit as st

st.set_page_config(page_title="Inicio", layout="centered")

# Fondo azul usando componentes de Streamlit (con st.markdown seguro)
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
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Espaciado arriba
st.markdown("###")
st.markdown("###")

# Mostrar imagen (ajusta el path y tamaño)
st.image("images/logo.png", width=300)

# Título
st.markdown("<h1>TECH GRADUATE PROGRAM</h1>", unsafe_allow_html=True)
