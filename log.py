class Log:
    # Constructor de la clase
    def __init__(self, ambiente,hostname,nivel,mensaje, fecha, hora, proceso):
        self.ambiente = ambiente
        self.hostname = hostname
        self.nivel = nivel
        self.mensaje = mensaje
        self.fecha = fecha
        self.hora = hora
        self.procesoId = proceso