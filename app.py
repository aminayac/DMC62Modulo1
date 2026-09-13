import streamlit as st

st.title("Especialización en Python for Analytics",text_alignment="center")

#crea tres columnas para mostrar la imagen centrada
col1, col2, col3 = st.columns(3)
#coloca la imagen en la columna del medio
with col2:
    st.image("python-logo.png")

#en la barra lateral izq muestra la imagen y crea el select box
st.sidebar.image("python-logo.png")
opcion = st.sidebar.selectbox(
    "**Seleccione una opción**",
    ("Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"),
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Autor")
st.sidebar.write("Aníbal Abraham Minaya Cubillas")
st.sidebar.write("Estudiante — Especialización en Python for Analytics")
st.sidebar.write("Año: ")

if st.sidebar.checkbox("Mostrar contacto"):
    st.sidebar.markdown("📧 anibal@example.com  ")
    st.sidebar.markdown("📍 Lima, Perú  ")

st.sidebar.markdown("---")
st.sidebar.markdown("_Esta aplicación utiliza únicamente la librería Streamlit para su interfaz._")

if opcion == "Home":
  #página home de presentación del proyecto
  #st.subheader("Módulo 1")
  st.write("Elaborado por Anibal Abraham Minaya Cubillas")
  st.write("Módulo 1")
  st.write("Información general del estudiante")  
  st.write("Año : ")
  st.write("Breve descripción del proyecto")
  st.write("Tecnologías utilizadas")

