# Pruebas de rendimiento con Locust(Python)
## Instalacion
1. Para la instalacion debe instalacion debera contar con las librerias de phyton

2. Debera instalar el complemento 

~~~
pip3 install locust
~~~
3. Para la instalacion en distribuciones basadas en archlinux.
~~~
- sudo pacman -S python-pipx
- pipx ensurepath
- pipx install locust
~~~
4. Verificar la version
~~~
locust -V
~~~
## Servicios probados
---
|Proyecto|Nombre Servicio|Tipo Request|Funcion|
|----------|----------|----------|----------|
|str-mul-minio-rest| Upload   | POST  | Carga de archivos al servidor de MINIO por multiform  |
|str-mul-minio-rest| Dowload   | GET   | Descarga de arachivos desde Minio  |
|str-muv-log-rest| Register    | POST   | Registro de logs en Elasticsearch por medio de la conexion de logstash (servicio en golang)   |