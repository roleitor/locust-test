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
      self.client.get("/", headers={"Content-Type": "application/json"},verify=False)      
def jsonDefault(object):
    return object.__dict__