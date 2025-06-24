import streamlit as st

st.set_page_config(page_title="Inicio", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "home"

# Fondo blanco y estilos
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: white;
    }
    h1 {
        color: #00008f !important;
        font-size: 4em;
        font-weight: bold;
        margin-bottom: 40px;
    }
    .stButton>button {
        margin-bottom: 1rem;
    }
    .left-content {
        margin-top: 4vh;
        color: #00008f !important;
        font-weight: bold !important;
        border: 2px solid #00008f !important;
    }
    </style>
""", unsafe_allow_html=True)

# Columnas: izquierda (texto), derecha (logo)
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.markdown('<div class="left-content">', unsafe_allow_html=True)
    st.markdown("<h1>TECH GRADUATE PROGRAM</h1>", unsafe_allow_html=True)
    if st.button("🙋 Sobre mí"):
        st.session_state.page = "sobre_mi"
    st.button("🧩 Resolución del caso")
    st.button("✅ Conclusiones")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.image("images/logo.png", use_container_width=True)
