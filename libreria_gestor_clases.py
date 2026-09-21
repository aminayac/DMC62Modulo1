import librería_clases_proyecto1
import numpy as np

class GestorServidores:
  def __init__(self):
    self.servidores = []

  def validar_existencia_servidor(self, nombre):
    for serv in self.servidores:
      if serv.nombre == nombre:
        return True
    return False
  
  def crear_servidor(self, servidor):
    if self.validar_existencia_servidor(servidor.nombre):
      raise ValueError(f"Servidor con nombre {servidor.nombre} ya existe.")
    self.servidores.append(servidor)

  def mostrar_info_servidores(self):
    arreglo_servidores=np.empty((0, 8), dtype=object)
    
    for serv in self.servidores:
      resumen_serv = serv.resumen()
      nuevo_registro = np.array([[serv.nombre, serv.tiempo_total_h, serv.tiempo_caida_h,
                                  serv.almacenamiento_total_gb, serv.almacenamiento_usado_gb,
                                  resumen_serv["disponibilidad_pct"],
                                  resumen_serv["uso_almacenamiento_pct"],
                                  resumen_serv["estado"]]], dtype=object)
      arreglo_servidores = np.vstack((arreglo_servidores, nuevo_registro))
    return arreglo_servidores

  def mostrar_nombres_servidores(self):
    nombres = [serv.nombre for serv in self.servidores]
    return nombres

  def eliminar_servidor(self, nombre_servidor):
    original_len = len(self.servidores)
    # la sgte linea recorre la lista de servidores y crea una nueva lista 
    # que excluye el servidor con el nombre especificado
    self.servidores = [serv for serv in self.servidores if serv.nombre != nombre_servidor]
    if len(self.servidores) == original_len:
      raise ValueError(f"Servidor con nombre {nombre_servidor} no encontrado.")

"""""
  def actualizar_cuenta(self, numero_cuenta, nuevo_titular=None, nuevo_saldo=None):
    for cuenta in self.cuentas:
      if cuenta.numero_cuenta == numero_cuenta:
        if nuevo_titular:
          cuenta.titular = nuevo_titular
        if nuevo_saldo is not None:
          cuenta.saldo = nuevo_saldo
        print(f"Cuenta {numero_cuenta} actualizada exitosamente.")
        return
    print(f"Cuenta con número {numero_cuenta} no encontrada.")

  def eliminar_cuenta(self, numero_cuenta):
    original_len = len(self.cuentas)
    self.cuentas = [cuenta for cuenta in self.cuentas if cuenta.numero_cuenta != numero_cuenta]
    if len(self.cuentas) < original_len:
      print(f"Cuenta con número {numero_cuenta} eliminada exitosamente.")
    else:
      print(f"Cuenta con número {numero_cuenta} no encontrada.")
"""