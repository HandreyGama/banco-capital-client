import customtkinter as ctk
from PIL import Image
from src.credencial_screen.server_handler.server_requests import *

class ContaApp(ctk.CTkToplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.geometry("900x600")
        self.title("Conta do Cliente")
        self.configure(fg_color="#f9f9f9")

        # Obtem dados do usuário
        user = client_informacoes(self.controller.USER_INDEX)

        # Sidebar
        sidebar = ctk.CTkFrame(self, width=200, fg_color="#ffffff", corner_radius=20)
        sidebar.pack(side="left", fill="y", padx=20, pady=20)

        # Foto de perfil
        image_path = user['foto_perfil']
        try:
            profile_pil = Image.open(image_path)
            profile_image = ctk.CTkImage(light_image=profile_pil, dark_image=profile_pil, size=(100, 100))
        except Exception as e:
            print(f"[Erro ao carregar imagem]: {e}")
            profile_image = None

        profile_label = ctk.CTkLabel(sidebar, image=profile_image, text="")
        profile_label.pack(pady=10)

        ctk.CTkLabel(sidebar, text=f"{user['nome']}", font=ctk.CTkFont(size=16, weight="bold")).pack()
        ctk.CTkLabel(sidebar, text="Caixa", font=ctk.CTkFont(size=12), text_color="gray").pack(pady=(0, 30))

        ctk.CTkButton(sidebar, text="Personal Information", fg_color="#f7be8f", text_color="#000000", hover=False).pack(fill="x", pady=5)
        ctk.CTkButton(sidebar, text="Login & Password", fg_color="transparent", text_color="#333333", hover_color="#f1f1f1").pack(fill="x", pady=5)
        ctk.CTkButton(sidebar, text="Log Out", fg_color="transparent", text_color="#333333", hover_color="#f1f1f1").pack(fill="x", pady=5)

        # Conteúdo principal
        content = ctk.CTkFrame(self, fg_color="#ffffff", corner_radius=20)
        content.pack(side="left", fill="both", expand=True, padx=10, pady=20)

        title = ctk.CTkLabel(content, text="Personal Information", font=ctk.CTkFont(size=20, weight="bold"), text_color="#000")
        title.pack(anchor="nw", pady=(10, 5), padx=20)

        # Gênero
        gender_frame = ctk.CTkFrame(content, fg_color="transparent")
        gender_frame.pack(anchor="nw", padx=20, pady=(0, 10))
        gender = ctk.StringVar(value="Male")
        ctk.CTkRadioButton(gender_frame, text="Male", variable=gender, value="Male").pack(side="left", padx=10)
        ctk.CTkRadioButton(gender_frame, text="Female", variable=gender, value="Female").pack(side="left", padx=10)

        # Entradas
        def create_input_row(parent, label1, value1, label2, value2):
            row = ctk.CTkFrame(parent, fg_color="transparent")
            row.pack(fill="x", padx=20, pady=5)

            entry1 = ctk.CTkEntry(row, placeholder_text=label1)
            entry1.insert(0, value1)
            entry1.pack(side="left", expand=True, padx=5)

            entry2 = ctk.CTkEntry(row, placeholder_text=label2)
            entry2.insert(0, value2)
            entry2.pack(side="left", expand=True, padx=5)

        create_input_row(content, "First Name", user['nome'].split()[0], "Last Name", user['nome'].split()[-1])
        create_input_row(content, "Email", user['email'], "Status", "Verified")
        create_input_row(content, "Address", user['endereco'], "Date of Birth", user['data_nascimento'])
        create_input_row(content, "Phone Number", user['telefone'], "Postal Code", user['cep'])
        create_input_row(content, "Location", f"{user['cidade']}, {user['pais']}", "", "")

        # Botões
        button_row = ctk.CTkFrame(content, fg_color="transparent")
        button_row.pack(padx=20, pady=20, anchor="e")

        ctk.CTkButton(button_row, text="Discard Changes", fg_color="white", border_color="#ff6600", border_width=2,
                      text_color="#ff6600", hover_color="#f5f5f5", width=140).pack(side="left", padx=10)
        ctk.CTkButton(button_row, text="Save Changes", fg_color="#ff6600", text_color="white",
                      hover_color="#e65c00", width=140).pack(side="left")
