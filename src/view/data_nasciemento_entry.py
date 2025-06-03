import customtkinter as ctk
import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime


class DataNascimentoEntry(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.selected_date = tk.StringVar(value="")

        # Caixa com borda
        self.container = ctk.CTkFrame(
            self,
            fg_color="#0a0a0a",
            border_color="#000",
            border_width=1,
            corner_radius=5
        )
        self.container.pack()

        CAMPO_WIDTH = 250
        CAMPO_PADX = 20
        CAMPO_PADY = 10
        BORDA_WIDTH = 1
        # Entry não editável
        self.entry = ctk.CTkEntry(
            self.container,
            textvariable=self.selected_date,
            placeholder_text="Data de nascimento",
            state="disabled",  # desativa digitação
            height=CAMPO_PADY,
            width=CAMPO_WIDTH - 35,
            fg_color="#0a0a0a",
            border_width=0,
            text_color="#e0e0e0"
        )
        self.entry.pack(side="left", padx=(5, 0), pady=2)

        # Botão com ícone do calendário
        self.cal_button = ctk.CTkButton(
            self.container,
            text="📅",
            width=30,
            height=28,
            fg_color="#0a0a0a",
            hover_color="#1e1e1e",
            command=self.abrir_calendario,
            corner_radius=0
        )
        self.cal_button.pack(side="right", padx=(0, 5))

    def abrir_calendario(self):
        self.popup = tk.Toplevel()
        self.popup.title("Data de nascimento")
        self.popup.grab_set()

        cal = Calendar(self.popup, date_pattern="dd/mm/yyyy", maxdate=datetime.today())
        cal.pack(padx=10, pady=10)

        confirmar = ctk.CTkButton(self.popup, text="Confirmar", command=lambda: self.selecionar_data(cal.get_date()))
        confirmar.pack(pady=5)

    def selecionar_data(self, data_str):
        self.selected_date.set(data_str)
        self.popup.destroy()

    def get(self):
        return self.selected_date.get()

    def validar_data(self):
        try:
            data_str = self.get()
            nascimento = datetime.strptime(data_str, "%d/%m/%Y")
            hoje = datetime.today()
            idade = (
                hoje.year
                - nascimento.year
                - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
            )
            if idade >= 18:
                return data_str
            else:
                return False
        except ValueError:
            return False
