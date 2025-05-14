import socket
import json
import time

HOST = "server ip"
PORT = 14532

username = socket.gethostbyname(socket.gethostname())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def register(nome, cpf, email, senha):
    OPERATION = "REGISTER"
    data = {"nome": nome, "cpf": cpf, "email": email, "senha": senha}
    client.send(OPERATION.encode("utf-8"))
    time.sleep(1)
    client.send(json.dumps(data).encode("utf-8"))


def close_conection():
    client.close()
