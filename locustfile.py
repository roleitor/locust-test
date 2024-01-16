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
      """ # Creamo la infomacion dinamica
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
      print(vLogJson) """
      # Crear un array de strings
      
      mi_array = ["an.suma.prbctp.repo/2024/Enero/15-01-2024/02987212-bd19-452e-b6bf-4ab4510e043c.pdf",
                  "an.suma.prbctp.repo/2024/Enero/15-01-2024/01b5731f-9cfa-4bfd-beec-b63e70c2cf1f.pdf", 
                  "an.suma.prbctp.repo/2024/Enero/15-01-2024/730d97d8-01bf-4213-a867-99afdf850993.pdf", 
                  "an.suma.prbctp.repo/2024/Enero/15-01-2024/30ebeecd-4381-4ec7-a241-754c98ef3ff1.pdf",
                  "an.suma.prbctp.repo/2024/Enero/15-01-2024/adf1d068-da0b-403d-b768-9a7d4ea4c11f.pdf"]
      # Seleccionar un elemento aleatorio
      elemento_aleatorio = random.choice(mi_array)
      url = '/str-mul-rest/documentos/dowloadstream'
      query_params = {
        'id': elemento_aleatorio
      }
      #self.client.post("/str-log-rest/v1/log/registrar", data=vLogJson, headers={"Content-Type": "application/json"},verify=False)
      
      self.client.get(url,params=query_params,headers={'accept': '*/*'},verify=False)

      
def jsonDefault(object):
    return object.__dict__