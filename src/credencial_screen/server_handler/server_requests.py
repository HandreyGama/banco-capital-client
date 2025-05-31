import socket
import json
import time
from .server_operations import *
from ...view.assets.default_photos import *
HOST = "proxy19.rt3.io"
PORT = 32752


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


def client_register(nome, cpf, email, senha, data_nasc, foto_perfil) -> None:
    OPERATION = CLIENT_REGISTER
    data = {
        "nome": nome, 
        "cpf": cpf, 
        "email": email, 
        "senha": senha,
        "data_nasc": data_nasc,
        "transferencias": {},
        "foto_perfil": foto_perfil
        }
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


def client_tranferencia(user_index, valor_transferencia, numero_conta):
    transfer_status = False
    OPERATION = CLIENT_TRANSFER
    data = {
        "user_index": user_index,
        "valor_transferencia": valor_transferencia,
        "numero_conta": numero_conta,
    }
    client.send(OPERATION.encode("utf-8"))
    time.sleep(1)
    client.send(json.dumps(data).encode("utf-8"))
    transferencia_status = client.recv(1024).decode("utf-8")
    if transferencia_status == "sucess":
        print("transferencia feita com sucesso")
        transfer_status = True
    else:
        print("Erro na transferencia")
        transfer_status = False
    return transfer_status


def client_informacoes(user_id):
    OPERATION = CLIENT_INFO
    client.send(OPERATION.encode("utf-8"))
    time.sleep(1)
    client.send(f"{user_id}".encode("utf-8"))
    client_return_info = client.recv(1024).decode("utf-8")
    return json.loads(client_return_info)


def close_conection():
    client.close()
