import streamlit as st

st.set_page_config(
    page_title="AXA Tech Graduate Program",
    layout="centered"
)

# Estilo general
st.markdown("""
    <style>
        .main {
            background-color: #00008B;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding-top: 60px;
        }
        .title {
            text-align: center;
            color: white;
            font-size: 36px;
            font-weight: bold;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Fondo azul en toda la app
st.markdown('<div class="container">', unsafe_allow_html=True)

# Imagen del logo (correctamente referenciada desde carpeta)
st.image("images/logo.png", width=150)

# Título
st.markdown('<div class="title">TECH GRADUATE PROGRAM</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
