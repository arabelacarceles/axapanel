import streamlit as st

st.set_page_config(page_title="AXA Panel", layout="wide")

# Estado de la navegación
if "page" not in st.session_state:
    st.session_state.page = "home"

# Función para botón de navegación (reutilizable)
def nav_button(label, target, key):
    if st.button(label, key=key):
        st.session_state.page = target

# Estilos comunes
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: white;
    }
    h1 {
        color: #0040E5 !important;
        font-size: 4em;
        font-weight: bold;
        margin-bottom: 40px;
    }
    .stButton>button {
        margin-bottom: 1rem;
        font-weight: bold !important;
        color: #0040E5 !important;
        border: 2px solid #0040E5 !important;
    }
    .left-content {
        margin-top: 4vh;
    }
    .top-right-logo {
        position: absolute;
        top: 20px;
        right: 40px;
    }
    .nav-buttons {
        display: flex;
        gap: 2rem;
        justify-content: center;
        margin-top: 6vh;
    }
    .nav-buttons button {
        background-color: transparent !important;
        border: none !important;
        color: #0040E5 !important;
        font-weight: bold;
        font-size: 1.1em;
    }
    </style>
""", unsafe_allow_html=True)

# HOME PAGE
if st.session_state.page == "home":
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

# SOBRE MÍ PAGE
elif st.session_state.page == "sobre_mi":
    st.logo("images/logo.png", size="large")

    st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
    nav_button("🙋 Sobre mí", "sobre_mi", key="nav1")
    nav_button("🧩 Resolución del caso", "resolucion", key="nav2")
    nav_button("✅ Conclusiones", "conclusiones", key="nav3")
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("### 👋 ¡Hola! Soy [tu nombre], participante del AXA Tech Graduate Program...")
    st.write("Aquí puedes contar tu perfil, intereses, formación o lo que te apetezca destacar.")

# Puedes seguir creando más elif para "resolucion", "conclusiones", etc.
