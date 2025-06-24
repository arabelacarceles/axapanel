import streamlit as st

st.set_page_config(
    page_title="AXA Tech Graduate Program",
    layout="wide"
)

logo_url = "https://raw.githubusercontent.com/arabelacarceles/axapanel/main/images/logo.png"

# Estilo para fondo y centrado
st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: #00008B !important;
            height: 100%;
            margin: 0;
        }
        .container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .title {
            color: white;
            font-size: 28px;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# HTML+Streamlit render
st.markdown('<div class="container">', unsafe_allow_html=True)
st.image(logo_url, width=100)
st.markdown('<div class="title">TECH GRADUATE PROGRAM</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
