from locust import HttpUser, task, between
from datetime import datetime
import os
import socket
import random
import json
from log import Log

class HelloWorldUser(HttpUser):
    wait_time = between(5, 10)    
    @task
    def prueba_rest_log(self):
      # Tu string JSON
      vLogJson = '{"ambiente": "DESARROLLO","fecha": "12/01/2023","hora": "12:30:00 p.m.","usuarioId":"DATA","usuario":"rmquispe","hostname": "ADUANA","mensaje": "Un mensaje de informacion","nivel": 1,"procesoId": 102030,"ip":"10.20.1.2","documento":"6767082","transaccionId":"8e45e741-e344-4ca5-91ef-20d30c40d51a","sesionId":"50201","agente":"mozilla"}'
      # Convertir el string JSON a un objeto Python
      datos = json.loads(vLogJson) 
      
      self.client.post("/str-log-rest/v1/log/registrar", data=vLogJson, headers={"Content-Type": "application/json"},verify=False)      
      
def jsonDefault(object):
    return object.__dict__