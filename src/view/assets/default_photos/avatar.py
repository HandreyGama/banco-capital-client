import os
import random

pasta_imagens = "src/view/assets/default_photos/"


imagens_disponiveis = [
    f for f in os.listdir(pasta_imagens)
    if f.lower().endswith(('.png', '.jpg', '.jpeg'))
]

# Função para atribuir uma imagem aleatória a um novo usuário
def atribuir_imagem_aleatoria():
    if not imagens_disponiveis:
        return None
    imagem_escolhida = random.choice(imagens_disponiveis)
    caminho_completo = os.path.join(pasta_imagens, imagem_escolhida)
    return {
        "avatar": f'{caminho_completo}'
        }

# Exemplo de uso
novo_usuario = "joao123"
foto_perfil = atribuir_imagem_aleatoria()

print(f"Usuário: {novo_usuario}")
print(f"Imagem atribuída: {foto_perfil}")
