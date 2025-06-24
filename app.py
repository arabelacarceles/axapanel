import streamlit as st

st.set_page_config(page_title="AXA Tech Graduate Program", layout="centered")

# Fondo azul oscuro
st.markdown(
    """
    <style>
    .main {
        background-color: #00008B;
        color: white;
        text-align: center;
        padding-top: 50px;
    }
    img {
        max-width: 300px;
        margin-bottom: 30px;
    }
    .title {
        font-size: 32px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.image("images/logo.png.png")
    st.markdown('<div class="title">TECH GRADUATE PROGRAM</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
