import streamlit as st

st.title("Especialización en Python for Analytics",text_alignment="center")

# Crea tres columnas
col1, col2, col3 = st.columns(3)
# Coloca la imagen en la columna del medio
with col2:
    st.image("python-logo.png")
    
#st.image("python-logo.png")
st.sidebar.image("python-logo.png")
opcion = st.sidebar.selectbox(
    "Seleccione una opción",
    ("Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"),
    index=0
)

if opcion == "Home":
  #página home de presentación del proyecto
  st.subheader("Módulo 1")
  st.write("Elaborado por Anibal Minaya")
  st.markdown("prueba") 

