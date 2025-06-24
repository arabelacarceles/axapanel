import streamlit as st

st.set_page_config(
    page_title="AXA Tech Graduate Program",
    layout="wide"
)

# CSS para fondo azul, centrado absoluto, imagen y texto
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            background-color: #00008B !important;
            height: 100%;
            margin: 0;
        }
        .centered-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .logo-img {
            max-width: 200px;
            height: auto;
        }
        .title-text {
            color: white;
            font-size: 36px;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# HTML + Streamlit para insertar contenido centrado
st.markdown(f"""
    <div class="centered-container">
        <img src="https://raw.githubusercontent.com/arabelacarceles/axapanel/main/images/logo.png" class="logo-img">
        <div class="title-text">TECH GRADUATE PROGRAM</div>
    </div>
""", unsafe_allow_html=True)
