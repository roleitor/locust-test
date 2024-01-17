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
      self.client.get(url,params=query_params,headers={'accept': '*/*'},verify=False)

      
