from locust import HttpUser, task, between
from datetime import datetime
import os
import socket
import random
import json
from log import Log

class HelloWorldUser(HttpUser):
    wait_time = between(1, 2)    
    @task
    def prueba_rest_log(self):
      # Creamo la infomacion dinamica
      #vAmbiente = os.environ['AMBIENTE']
      vAmbiente = 'calidad'
      vHostname = socket.gethostname()
      vNivel = random.randint(1, 4)
      fecha_hora_actual = datetime.now()
      #Uso de la fecha
      vFecha = fecha_hora_actual.strftime("%d/%m/%Y")
      #Uso de la hora
      vHora = fecha_hora_actual.strftime("%H:%M:%S")
      #para el procesoId
      vProcesoId = 102030
      # Mensaje
      vMensaje = 'Ejemplo de uso de logs'
      # Creamos la entidad de logs
      vLog = Log(vAmbiente,vHostname,vNivel,vMensaje,vFecha,vHora,vProcesoId)
      # Convertir la entidad a formato JSON
      vLogJson = json.dumps(vLog.__dict__, indent=2)
      #Pasar json
      print(vLog.__dict__)
      print(vLogJson) 

      self.client.post("/str-log-rest/v1/log/registrar", data=vLogJson, headers={"Content-Type": "application/json"},verify=False)      
def jsonDefault(object):
    return object.__dict__