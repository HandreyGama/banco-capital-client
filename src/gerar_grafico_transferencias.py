import matplotlib.pyplot as plt
from .credencial_screen.server_handler.server_requests import *
from datetime import datetime
import matplotlib.dates as mdates


def client_gerar_grafico_transferencias(user_index):
    datas = []
    transferencias_list = []
    transferencias = client_extrato(user_index)
    for i in transferencias:
        for j in range(0, len(i)):
            if j == 2:
                datas.append(datetime.strptime(i[j], "%Y-%m-%d %H:%M:%S.%f"))
            if j == 1:
                transferencias_list.append(int(i[j].replace("R$ ", "")))
        # Tema escuro
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(12, 6))

    # Linha principal
    ax.plot(
        datas,
        transferencias_list,
        marker="o",
        linestyle="-",
        linewidth=2.5,
        color="#00f5d4",
        markerfacecolor="black",
        markeredgewidth=2,
    )
    y_base = min(transferencias_list) - 100  # margem pode ser 0 ou algo como 100

    # Preenchimento abaixo da linha
    ax.fill_between(datas, transferencias_list, y2=y_base, color="#00f5d4", alpha=0.2)

    # Eixo X formatado
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
    fig.autofmt_xdate()

    # Títulos
    ax.set_title(
        "Transferências por Data", fontsize=16, fontweight="bold", color="white"
    )
    ax.set_xlabel("Data", fontsize=12, color="white")
    ax.set_ylabel("Valor (R$)", fontsize=12, color="white")

    # Grid e fundo
    ax.grid(True, linestyle="--", alpha=0.3)
    ax.set_facecolor("#121212")
    fig.patch.set_facecolor("#121212")
    ax.tick_params(colors="white", which="both")

    # Rótulos dos pontos
    for x, y in zip(datas, transferencias_list):
        ax.text(
            x, y + 50, f"R${y}", ha="center", va="bottom", fontsize=10, color="white"
        )

    plt.tight_layout()
    plt.savefig("grafico_transferencias.png", dpi=300, bbox_inches="tight")


def client_gerar_grafico_saldo(user_index):
    datas = []
    saldo = []
    transferencias = client_extrato(user_index)
    for i in transferencias:
        print(transferencias)
        for j in range(0, len(i)):
            print(j)
            print(i[j])
            if j == 2:
                datas.append(datetime.strptime(i[j], "%Y-%m-%d %H:%M:%S.%f"))
            if j == 5:
                saldo.append(float(i[j]))
        # Tema escuro
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(12, 6))

    # Linha principal
    ax.plot(
        datas,
        saldo,
        marker="o",
        linestyle="-",
        linewidth=2.5,
        color="#00f5d4",
        markerfacecolor="black",
        markeredgewidth=2,
    )
    y_base = min(saldo) - 100  # margem pode ser 0 ou algo como 100

    # Preenchimento abaixo da linha
    ax.fill_between(datas, saldo, y2=y_base, color="#00f5d4", alpha=0.2)

    # Eixo X formatado
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
    fig.autofmt_xdate()

    # Títulos
    ax.set_title(
        "Transferências por Data", fontsize=16, fontweight="bold", color="white"
    )
    ax.set_xlabel("Data", fontsize=12, color="white")
    ax.set_ylabel("Valor (R$)", fontsize=12, color="white")

    # Grid e fundo
    ax.grid(True, linestyle="--", alpha=0.3)
    ax.set_facecolor("#121212")
    fig.patch.set_facecolor("#121212")
    ax.tick_params(colors="white", which="both")

    # Rótulos dos pontos
    for x, y in zip(datas, saldo):
        ax.text(
            x, y + 50, f"R${y}", ha="center", va="bottom", fontsize=10, color="white"
        )

    plt.tight_layout()
    plt.savefig("grafico_saldo.png", dpi=300, bbox_inches="tight")
