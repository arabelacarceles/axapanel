import streamlit as st

st.set_page_config(
    page_title="AXA Tech Graduate Program",
    layout="wide"
)

# CSS para fondo y estilo centrado
st.markdown("""
    <style>
        body {
            background-color: #00008B;
        }
        .container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .logo {
            width: 100px;
            height: auto;
        }
        .title {
            color: white;
            font-size: 28px;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Contenido principal
st.markdown("""
    <div class="container">
        <img class="logo" src="https://raw.githubusercontent.com/arabelacarceles/axapanel/main/images/logo.png">
        <div class="title">TECH GRADUATE PROGRAM</div>
    </div>
""", unsafe_allow_html=True)
