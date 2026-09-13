import streamlit as st

st.title("Especialización en Python for Analytics")
st.image("python-logo.png",width =400)
opcion = st.selectbox(
    "Seleccione una opción",
    ("Home", "Módulo 1", "Módulo 2", "Módulo 3", "Módulo 4"),
    index=0
)

if opcion == "Home":
  #página home de preseentación del proyecto
  st.subheader("Módulo 1")
  st.write("Elaborado por Anibal Minaya")
  st.markdown("prueba") 

