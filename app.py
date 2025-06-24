import streamlit as st

st.set_page_config(page_title="Inicio", layout="wide")

# CSS: fondo azul, sin scroll, centrado
st.markdown("""
    <style>
        body {
            margin: 0;
            overflow: hidden;
        }
        [data-testid="stAppViewContainer"] {
            background-color: #00008B;
        }
        .slide {
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        .slide h1 {
            color: white;
            font-size: 3em;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# HTML estructurado como slide
st.markdown('<div class="slide">', unsafe_allow_html=True)
st.image("images/logo.png", width=300)
st.markdown('<h1>TECH GRADUATE PROGRAM</h1>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
