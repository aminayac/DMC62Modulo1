import streamlit as st
import datetime
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Especialización en Python for Analytics - Módulo 1",
    page_icon="🐍",
    layout="wide",
)

# Estilos (solo usando Streamlit)
st.markdown(
    """
    <style>
    /* Contenedor principal */
    .header-card {
        background: linear-gradient(90deg,#0f172a,#0ea5a2);
        padding: 22px 26px;
        border-radius: 10px;
        color: white;
        box-shadow: 0 4px 20px rgba(2,6,23,0.2);
    }
    .app-title {font-size:28px; font-weight:700; margin:0}
    .app-subtitle {font-size:14px; margin:0; color:rgba(255,255,255,0.9)}

    .card {background: #ffffff; padding:18px; border-radius:8px; box-shadow: 0 1px 6px rgba(2,6,23,0.06);}
    .muted {color: #6b7280}
    .kpi {text-align:center}
    .kpi h2 {margin:0}

    .small {font-size:13px; color:#6b7280}

    /* Ajustes para imágenes en sidebar */
    .sidebar .css-1d391kg img{border-radius:8px}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header centrado con logo
with st.container():
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.markdown(
            """
            <div class='header-card' style='text-align:center'>
                <div style='display:flex;align-items:center;justify-content:center;gap:18px'>
                    <img src='python-logo.png' width='64' style='border-radius:8px' />
                    <div style='text-align:left'>
                        <div class='app-title'>Especialización en Python for Analytics</div>
                        <div class='app-subtitle'>Módulo 1 — Proyecto de Aníbal Abraham Minaya Cubillas</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("\n")

# --- Barra lateral (navegación y detalles)
st.sidebar.image("python-logo.png", width=110)
st.sidebar.markdown("## Navegación")
seccion = st.sidebar.radio(
    "Ir a",
    ("Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"),
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Autor")
st.sidebar.write("Aníbal Abraham Minaya Cubillas")
st.sidebar.write("Estudiante — Especialización en Python for Analytics")
st.sidebar.write(f"Año: {datetime.datetime.now().year}")

if st.sidebar.checkbox("Mostrar contacto"):
    st.sidebar.markdown("📧 anibal@example.com  ")
    st.sidebar.markdown("📍 Lima, Perú  ")

st.sidebar.markdown("---")
st.sidebar.markdown("_Esta aplicación utiliza únicamente la librería Streamlit para su interfaz._")

# --- Contenido principal
if seccion == "Home":
    left, right = st.columns([2, 1])

    with left:
        st.markdown("""
        <div class='card'>
        <h3>Resumen del proyecto</h3>
        <p class='muted'>Este repositorio contiene los ejercicios del Módulo 1 de la Especialización en Python for Analytics. El objetivo es practicar manipulación de datos, visualización y desarrollo de aplicaciones interactivas con Streamlit.</p>
        <ul>
            <li><strong>Tecnologías:</strong> Python, pandas, Streamlit</li>
            <li><strong>Objetivos:</strong> Limpieza de datos, análisis exploratorio, visualización y despliegue</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        k1, k2, k3 = st.columns(3)
        k1.metric("Ejercicios", "4", "+1 desde la versión anterior")
        k2.metric("Progreso", "40%", "en curso")
        k3.metric("Última actualización", datetime.datetime.now().strftime("%Y-%m-%d"))

        st.markdown("---")
        st.subheader("Acerca del autor")
        st.write("Soy Aníbal Abraham Minaya, estudiante de la especialización. En este módulo practico las bases de Python aplicadas al análisis de datos y la creación de micro-aplicaciones interactivas con Streamlit.")

        with st.expander("Objetivos del módulo"):
            st.write("• Aprender a manipular datos con pandas")
            st.write("• Crear visualizaciones básicas y avanzadas")
            st.write("• Construir apps interactivas con Streamlit")

    with right:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Recursos rápidos")
        st.write("- Documentación de Streamlit: https://docs.streamlit.io")
        st.write("- Repositorio del proyecto: (ver en GitHub)")
        st.markdown("</div>", unsafe_allow_html=True)

else:
    # Plantilla profesional para ejercicios
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader(seccion)
    st.write("En esta sección se colocará la explicación del ejercicio, el dataset y los controles interactivos.")

    st.markdown("**Ejemplo interactivo**")
    n = st.slider("Selecciona número de filas a mostrar", 1, 20, 5)

    df = pd.DataFrame({
        "Columna A": range(1, 101),
        "Columna B": [x * 2 for x in range(1, 101)],
        "Categoría": ["A" if x % 2 == 0 else "B" for x in range(1, 101)],
    })

    st.dataframe(df.head(n))
    st.markdown("---")
    st.write("Visualización de ejemplo")
    chart_data = df.head(50)[["Columna A", "Columna B"]]
    st.line_chart(chart_data.set_index("Columna A"))
    st.markdown("</div>", unsafe_allow_html=True)

# --- Footer
st.markdown("---")
st.markdown("<div style='text-align:center; color:#6b7280'>Built with ❤️ using Streamlit — Especialización en Python for Analytics</div>", unsafe_allow_html=True)
