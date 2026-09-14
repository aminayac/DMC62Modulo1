import streamlit as st
import datetime
import pandas

#opciones del selectbox
HOME       = "Home"
EJERCICIO1 = "Ejercicio 1"
EJERCICIO2 = "Ejercicio 2"
EJERCICIO3 = "Ejercicio 3"
EJERCICIO4 = "Ejercicio 4"

# Configuración de la página
st.set_page_config(
    page_title="Especialización en Python for Analytics - Módulo 1",
    page_icon=":armenia:"
)

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
    (HOME, EJERCICIO1, EJERCICIO2, EJERCICIO3, EJERCICIO4),
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

if opcion == HOME:
  #página home de presentación del proyecto
  #st.subheader("Módulo 1")
  st.write("Elaborado por Anibal Abraham Minaya Cubillas")
  st.write("Módulo 1")
  st.write("Información general del estudiante")  
  st.write(f"Año: {datetime.datetime.now().year}")
  st.write("Breve descripción del proyecto")
  st.write("Tecnologías utilizadas")
elif opcion == EJERCICIO1:
  #inicializa listas
  lista_conceptos = []
  lista_tipos_mov = []
  lista_valores   = []
  #verifica si existen las variables de sesion: lista de conceptos, tipos y montos
  #si no existen, las inicializa, si existen, las recupera
  if 'MISESION' not in st.session_state:
    st.session_state['MISESION'] = True
    st.session_state['LISTA_CONCEPTOS'] = lista_conceptos
    st.session_state['LISTA_TIPO_MOV'] = lista_tipos_mov
    st.session_state['LISTA_VALOR'] = lista_valores
  else:
    lista_conceptos = st.session_state['LISTA_CONCEPTOS']
    lista_tipos_mov = st.session_state['LISTA_TIPO_MOV']
    lista_valores   = st.session_state['LISTA_VALOR']

  #Ejercicio 1 – Flujo de caja con listas
  st.write("Ejercicio 1 – Flujo de caja con listas")
  #crea 4 columnas para mostrar los elementos del formulario
  col1, col2, col3, col4 = st.columns(4)
  #concepto
  concepto = col1.text_input("Concepto")
  tipo_mov = col2.selectbox("Tipo Movimiento",("Ingreso","Gasto"),index=None,placeholder="Seleccione...")
  valor = col3.number_input("Valor",value=0)
  col4.write("")
  col4.write("")
  if col4.button("Añadir"):
      #st.write("Registro añadido.. Hacer listas de conceptos, etc. Luego hacerlo diccionario y luego dataframe")
      lista_conceptos.append(concepto)
      lista_tipos_mov.append(tipo_mov)
      lista_valores.append(valor)
      st.session_state['LISTA_CONCEPTOS'] = lista_conceptos
      st.session_state['LISTA_TIPO_MOV'] = lista_tipos_mov
      st.session_state['LISTA_VALOR'] = lista_valores
      #st.write(lista_conceptos)  
      #st.write(lista_tipos_mov)
      #st.write(lista_valores)
  diccionario_datos = {"Concepto" : lista_conceptos, "Tipo Movimiento" : lista_tipos_mov, "Valor" : lista_valores}
  tabla = pandas.DataFrame(diccionario_datos)
  st.write(tabla, index=None)
  col1.text_input.value = ""
  col2.selectbox.index=None
  col3.number_input.value=0
