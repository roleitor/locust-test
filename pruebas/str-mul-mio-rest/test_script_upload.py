from locust import HttpUser, task, between
from datetime import datetime
import os
import socket
import random
import json
from log import Log

class TestMinioService(HttpUser):
    wait_time = between(60, 60)
    @task
    def upload_file(self):
        # Ruta al archivo que deseas cargar
        file_path = "/home/rmquispe/Documentos/ProyectosPersonales/Locust (QA-TEST)/locust-test/pruebas/str-mul-mio-rest/data/00c0223b-7428-4226-b1aa-d8d1a769d5a0.pdf"
        print("Ruta: ",file_path)

        # Construir la ruta completa al archivo
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_path))

        # Configurar el contenido del archivo como datos binarios en el cuerpo de la solicitud
        with open(file_path, "rb") as file:
            # Enviar la solicitud POST con el archivo adjunto
            response = self.client.post(
                "/str-mul-rest/documentos/upload?repositorio=an.sen.repo",
                files={"file": (os.path.basename(file_path), file, "application/pdf")}
            ,verify=False)