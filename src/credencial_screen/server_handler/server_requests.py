import socket
import json
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from .server_operations import *
from src.view.assets.default_photos import *

HOST = "127.0.0.1"
PORT = 69


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


def client_register(nome, cpf, email, senha, data_nasc, foto_perfil, telefone) -> None:
    OPERATION = CLIENT_REGISTER
    data = {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "senha": senha,
        "data_nasc": data_nasc,
        "transferencias": [],
        "foto_perfil": foto_perfil,
        "telefone": telefone,
    }
    client.send(OPERATION.encode("utf-8"))
    time.sleep(1)
    client.send(json.dumps(data).encode("utf-8"))
    status_register = client.recv(1024).decode("utf-8")
    if status_register == "True":
        print("operação feita com sucesso!")
    elif status_register == "False":
        print(
            "[ERRO] DADOS CADASTRADOS JA EXISTEM NO BANCO DE DADOS!\nCANCELANDO REGISTRO!"
        )


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
        print("transferencia feita com sucesso!")
        print("-" * 6 + " TRANSFERENCIA FINALIZADA " + "-" * 6)
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


def client_extrato(user_id):
    OPERATION = CLIENT_EXTRATO
    client.send(OPERATION.encode("utf-8"))
    time.sleep(1)
    client.send(f"{user_id}".encode("utf-8"))
    client_return_extrato = client.recv(1024).decode("utf-8")
    return json.loads(client_return_extrato)


def client_get_user_target(numero_conta):
    OPERATION = CLIENT_TARGET
    client.send(OPERATION.encode("utf-8"))
    time.sleep(1)
    client.send(numero_conta.encode("utf-8"))
    client_target_nome = client.recv(1024).decode("utf-8")
    return client_target_nome


def client_update_info(user_option, user_new_info, user_index):
    OPERATION = CLIENT_UPDATE_INFO
    client.send(OPERATION.encode("utf-8"))
    time.sleep(1)
    client.send(json.dumps([user_option, user_new_info, user_index]).encode("utf-8"))
    status_update_info = client.recv(1024).decode("utf-8")


def close_conection():
    client.close()
