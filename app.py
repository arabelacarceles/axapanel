import streamlit as st

st.set_page_config(page_title="AXA Tech Graduate Program", layout="centered")

# Estilo global
st.markdown("""
    <style>
        body {
            background-color: #00008B;
        }
        .main {
            background-color: #00008B !important;
        }
        .logo {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 150px;
            margin-top: 60px;
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

# Cuerpo de la página
st.markdown(f'<img src="images/logo.png" class="logo">', unsafe_allow_html=True)
st.markdown('<div class="title">TECH GRADUATE PROGRAM</div>', unsafe_allow_html=True)