import socket
import json
import time
from ..server_handler.server_operations import *

HOST = "192.168.0.16"
PORT = 14532

username = socket.gethostbyname(socket.gethostname())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST, PORT))
except:
    print(
        "[ERROR] o sistema não pode conectar-se ao servidor, verifique se o server esta online"
    )
    exit()
OPERATION = "NONE"


def client_register(nome, cpf, email, senha) -> None:
    OPERATION = CLIENT_REGISTER
    data = {"nome": nome, "cpf": cpf, "email": email, "senha": senha}
    client.send(OPERATION.encode("utf-8"))
    time.sleep(1)
    client.send(json.dumps(data).encode("utf-8"))


def client_login(cpf, senha):
    OPERATION = CLIENT_LOGIN
    data = {"cpf": cpf, "senha": senha}
    client.send(OPERATION.encode("utf-8"))
    time.sleep(1)
    client.send(json.dumps(data).encode("utf-8"))
    client_exists = client.recv(1024).decode("utf-8") == "True"
    client_index = int(client.recv(1024).decode("utf-8"))
    return client_exists, client_index


def close_conection():
    client.close()
