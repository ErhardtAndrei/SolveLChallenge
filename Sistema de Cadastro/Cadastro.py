import os
import traceback
import warnings
import sqlite3
import customtkinter as ctk
from tkinter import *
import sqlite3
from tkinter import messagebox

warnings.filterwarnings("ignore") #Usado temporariamente para ignorar o aviso CTkimage

notas = [1, 2, 5, 10, 20, 50, 100]
qtdNotas = [0, 0, 0, 0, 0, 0, 0]
qtdTotalNotas = 0
valorRestante = 0
vetPreco = []
vetProduto = []
valorTot= i =  0
class BackEnd(): #A classe backend herda os componentes da classe principal App, por isso está dentro de App
    
    def connect_db(self): #Conectando ao banco de dados
        self.conn = sqlite3.connect('Users_data.db')
        self.cursor = self.conn.cursor()
        print("Data base has been connected.")
    
    def desconect_db(self):
        self.conn.close()
        print("Data base has desconnected.")

    def create_table(self):
        self.connect_db()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL,
                Usermail TEXT NOT NULL,
                Password TEXT NOT NULL,
                Confirm_Password TEXT NOT NULL
                );
        """)#Em caixa alta são os comandos sql
        self.conn.commit()
        print("Tabela criada com sucesso.")
        self.desconect_db()

    def register_user(self):#Pegando as entrys de cadastro e armazenando em variáveis
        self.username_logon = self.username_logon_entry.get()
        self.usermail_logon = self.usermail_logon_entry.get()
        self.password_logon = self.password_logon_entry.get()
        self.confirm_password_logon = self.confirm_password_logon_entry.get()

        self.connect_db()

        self.cursor.execute("""
            INSERT INTO Usuarios (Username, Usermail, Password, Confirm_Password)
            VALUES (?, ?, ?, ?)""", (self.username_logon, self.usermail_logon, self.password_logon, self.confirm_password_logon))

        try: #Verificando se algum dos campos de formulário de cadastro estão vazios
            if(self.username_logon == "" or self.usermail_logon == "" or self.password_logon == "" or self.confirm_password_logon == ""):
                messagebox.showerror(title="Sistema de Login", message="Preencha todos os campos.")
                
            elif(len(self.username_logon) < 4):
                messagebox.showwarning(title="Sistema de Login", message="O nome de usuário é muito curto.")    
            
            elif(len(self.password_logon) < 4):
                messagebox.showwarning(title="Sistema de Login", message="A senha precisa de ao menos 6 caractéres.")
                
            elif(self.password_logon != self.confirm_password_logon):
                messagebox.showerror(title="Sistema de Login", message="Senhas não compátivel.")
            else:
                self.conn.commit()
                messagebox.showinfo(title="Sistema de Login", message="Usuário cadastrado.")
                self.desconect_db()
                self.limpa_entrys_cadastro()
    
        except:
            messagebox.showerror(title="Sistema de Login", message="Erro ao cadastrar.\nTente novamente.")
            self.desconect_db()
            
    def verify_login(self): #Verificação de Login
        self.username_login = self.username_login_entry.get()
        self.password_login = self.password_login_entry.get()

        self.connect_db()

        self.cursor.execute("""SELECT * FROM Usuarios WHERE(Username = ? AND Password = ?)""", (self.username_login, self.password_login))

        self.verify_data = self.cursor.fetchone() #percorrendo na tabela de usuarios para verificar se o usuario e a senha existem

        try:
            if(self.username_login == "" or self.password_login==""):
                messagebox.showwarning(title="Sistema de login", message=("Preencha todos os campos."))

            elif(self.username_login in self.verify_data and self.password_login in self.verify_data):
                messagebox.showinfo(title="Sistema de login", message="Usuario conectado.")
                self.desconect_db()
                self.limpa_entrys_login()
                self.register_products()
        except:
            messagebox.showerror(title="Sistema de Login", message="Erro, usuário não encontrado.")
            self.desconect_db()

    def calc_registers(self):
        
        self.product_name = self.product_name_entry.get()
        self.product_value = self.product_value_entry.get()
        
        try:
            if(self.product_name == "" or self.product_value == ""): #Verifica se os campos estão vazios
                messagebox.showwarning(title="Sistema de Cadastro de Produtos", message="Preencha todos os campos.")
            else:
                if (len(vetProduto) < 10):
                    vetProduto.append(self.product_name)
                    vetPreco.append(int(self.product_value))
                    messagebox.showinfo(title="Sistema de Cadastro de Produtos", message="Produto cadastrado.")
                    self.limpa_entrys_products()                   
        except:
            traceback.print_exc() #Conferir quais erros estão chegando ao except   

    def finish_registers(self):
        
        global qtdTotalNotas
        valorTot = sum(vetPreco)
        self.valorTot = valorTot
        valorRestante = valorTot

        for i in range(6, -1, -1):
                qtdNotas[i] = valorRestante // notas[i]
                qtdTotalNotas += qtdNotas[i]
                valorRestante %= notas[i]
        
        self.qntTotal = qtdTotalNotas
        self.notas100 = qtdNotas[6]
        self.notas50  = qtdNotas[5]
        self.notas20  = qtdNotas[4]
        self.notas10  = qtdNotas[3]
        self.notas5   = qtdNotas[2]
        self.notas2   = qtdNotas[1]
        self.notas1   = qtdNotas[0]
        
        self.ballots_result()

#Classe principal. Inicia a janela
class App(ctk.CTk, BackEnd): 
    def __init__(self): #função inicial da classe
        super().__init__() #define que init é a função mais importante dentro da classe
        self.config_janela_inicial() #da o start nas config da janela inicial
        self.tela_de_login()
        self.create_table()

    #Configurando a janela principal
    def config_janela_inicial(self):
        self.geometry("700x345")
        self.title("Sistema de Cadastro Solve Light")
        self.resizable(False,False)

    def tela_de_login(self): 
    #Buscando o caminho da imagem
        current_dir = os.getcwd()
        img_path = os.path.join(current_dir, "solvel-img.png")
        self.img = PhotoImage(file=img_path)
        self.lb_img = ctk.CTkLabel(self, text=None,image=self.img)
        self.lb_img.grid(row=1,column=0,padx=10, pady=20)

    #Adicionando frame tela login (fundo)
        self.frame_login = ctk.CTkFrame(self, width=380,fg_color="#dcdcdc", height=310)
        self.frame_login.place(x=365, y=8)

    #Widgets dentro do frame (caixas de texto e botões) (#490077 = cor do logo)
        self.lb_title = ctk.CTkLabel(self.frame_login, text="Faça o Login", font=("Century Gothic bold", 22))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Nome de usuario..",font=("Century Gothic bold", 16), corner_radius=20, border_color="#490077")
        self.username_login_entry.grid(row=1, column=0, padx=10, pady=10)
        self.username_login_entry.bind('<Return>', lambda event: self.verify_login())

        self.password_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Senha..",font=("Century Gothic bold", 16), corner_radius=20, show="*", border_color="#490077")
        self.password_login_entry.grid(row=2, column=0, padx=10, pady=10)
        self.password_login_entry.bind('<Return>', lambda event: self.verify_login())

        self.btn_login = ctk.CTkButton(self.frame_login, width=300, fg_color="#490077", text="Login",font=("Century Gothic bold", 16),corner_radius=20, command=self.verify_login)
        self.btn_login.grid(row=4, column=0, padx=10, pady=10)
        self.btn_login.bind('<Return>', lambda event: self.verify_login())

        self.span = ctk.CTkLabel(self.frame_login, text="Não possui cadastro?", font=("Century Gothic", 10))
        self.span.grid(row=5, column=0, padx=10, pady=20)

        self.btn_logon = ctk.CTkButton(self.frame_login, width=300, text="Logon".upper(),font=("Century Gothic bold", 10),corner_radius=20, command=self.tela_de_cadastro)
        self.btn_logon.grid(row=6, column=0, padx=10, pady=30)
    
    #criando a tela de cadastro
    def tela_de_cadastro(self):
    
        #Adicionando frame de cadastro (fundo)
        self.frame_logon = ctk.CTkFrame(self, width=380,fg_color="#dcdcdc", height=310)
        self.frame_logon.place(x=365, y=8)

        #Removendo a tela de login
        self.frame_login.place_forget()
        
        #Titulo tela de cadastro
        self.lb_title = ctk.CTkLabel(self.frame_logon, text="Faça o cadastro de usuário", font=("Century Gothic bold", 22))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        #Nova frame com widgets da tela de cadastro
        self.username_logon_entry = ctk.CTkEntry(self.frame_logon, width=300, placeholder_text="Nome de usuario..",font=("Century Gothic bold", 16), corner_radius=20, border_color="#490077")
        self.username_logon_entry.grid(row=1, column=0, padx=10, pady=5)

        self.usermail_logon_entry = ctk.CTkEntry(self.frame_logon, width=300, placeholder_text="Digite o e-mail..",font=("Century Gothic bold", 16), corner_radius=20, border_color="#490077")
        self.usermail_logon_entry.grid(row=2, column=0, padx=10, pady=5)

        self.password_logon_entry = ctk.CTkEntry(self.frame_logon, width=300, placeholder_text="Digite a senha..",font=("Century Gothic bold", 16), corner_radius=20, show="*", border_color="#490077")
        self.password_logon_entry.grid(row=3, column=0, padx=10, pady=5)
 
        self.confirm_password_logon_entry = ctk.CTkEntry(self.frame_logon, width=300, placeholder_text="Confirme a senha..",font=("Century Gothic bold", 16), corner_radius=20, show="*", border_color="#490077")
        self.confirm_password_logon_entry.grid(row=4, column=0, padx=10, pady=5)
 
        self.btn_register = ctk.CTkButton(self.frame_logon, width=300, fg_color="#490077", text="Cadastrar",font=("Century Gothic bold", 16),corner_radius=20, command=self.register_user)
        self.btn_register.grid(row=5, column=0, padx=10, pady=5)

        self.span = ctk.CTkLabel(self.frame_logon, text="Já possui cadastro?", font=("Century Gothic", 10))
        self.span.grid(row=6, column=0, padx=10)

        self.btn_login_back = ctk.CTkButton(self.frame_logon, width=300, text="Voltar".upper(),font=("Century Gothic bold", 10),corner_radius=20, command=self.tela_de_login)
        self.btn_login_back.grid(row=7, column=0, padx=10, pady=12)

    def register_products(self):
    
        #Adicionando frame de cadastro de produtos
        self.frame_register_products = ctk.CTkFrame(self, width=380,fg_color="#dcdcdc", height=310)
        self.frame_register_products.place(x=365, y=8)
        
        #Removendo a tela de login
        self.frame_login.place_forget()

        #Titulo tela cadastro de produtos
        self.lb_title = ctk.CTkLabel(self.frame_register_products, text="Faça o cadastro dos produtos", font=("Century Gothic bold", 22))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        #Nova frame com widgets da tela de cadastro de produtos
        self.product_name_entry = ctk.CTkEntry(self.frame_register_products, width=300, placeholder_text="Insira o nome do produto..", font=("Century Gothic bold", 16), corner_radius=20, border_color="#490077")
        self.product_name_entry.grid(row=1, column=0, padx=10, pady=5)

        self.product_value_entry = ctk.CTkEntry(self.frame_register_products, width=300, placeholder_text="Insira o valor do produto..", font=("Century Gothic bold", 16), corner_radius=20, border_color="#490077")
        self.product_value_entry.grid(row=2, column=0, padx=10, pady=5)

        self.btn_register_new_product = ctk.CTkButton(self.frame_register_products, width=300, text="Cadastrar produto", font=("Century Gothic Bold", 16), corner_radius=20, command=self.calc_registers)
        self.btn_register_new_product.grid(row=3, column=0, padx=10, pady=5)

        self.btn_finish_register = ctk.CTkButton(self.frame_register_products, width=300, text="Encerrar cadastros", font=("Century Gothic Bold", 16), corner_radius=20, command=self.finish_registers)
        self.btn_finish_register.grid(row=4, column=0, padx=10, pady=5)
        
        self.btn_login_back = ctk.CTkButton(self.frame_register_products, width=300, text="Voltar".upper(),font=("Century Gothic bold", 12),corner_radius=20, command=self.tela_de_login)
        self.btn_login_back.grid(row=10, column=0, padx=10, pady=80)
          
    def ballots_result(self):
        #Adiciona frame tela de resultados
        self.frame_ballots_result = ctk.CTkFrame(self, width=380, fg_color="#dcdcdc", height=310)
        self.frame_ballots_result.place(x=365, y=8)

        #Removendo a tela de cadastro
        self.frame_register_products.place_forget()

        #Titulo da tela de resultados
        self.lb_title = ctk.CTkLabel(self.frame_ballots_result, text=f"Carrinho de compras R$: {self.valorTot}", font=("Century Gothic bold", 18))
        self.lb_title.grid(row=0, column=0, padx=5, pady=0)

        self.lb_result = ctk.CTkLabel(self.frame_ballots_result, text=f"Quantidade mínima de notas necessárias: {self.qntTotal}", font=("Century Gothic bold", 15))
        self.lb_result.grid(row=2, column=0, padx=5, pady=0, sticky = "w")

        self.lb_result100 = ctk.CTkLabel(self.frame_ballots_result, text=f"Notas de 100: {self.notas100}", font=("Century Gothic bold", 12))
        self.lb_result100.grid(row=3, column=0, padx=5, pady=0, sticky = "w")

        self.lb_result50 = ctk.CTkLabel(self.frame_ballots_result, text=f"Notas de 50: {self.notas50}", font=("Century Gothic bold", 12))
        self.lb_result50.grid(row=4, column=0, padx=5, pady=0, sticky = "w")

        self.lb_result20 = ctk.CTkLabel(self.frame_ballots_result, text=f"Notas de 20: {self.notas20}", font=("Century Gothic bold", 12))
        self.lb_result20.grid(row=5, column=0, padx=5, pady=0, sticky = "w")

        self.lb_result10 = ctk.CTkLabel(self.frame_ballots_result, text=f"Notas de 10: {self.notas10}", font=("Century Gothic bold", 12))
        self.lb_result10.grid(row=6, column=0, padx=5, pady=0, sticky = "w")

        self.lb_result5 = ctk.CTkLabel(self.frame_ballots_result, text=f"Notas de 5: {self.notas5}", font=("Century Gothic bold", 12))
        self.lb_result5.grid(row=7, column=0, padx=5, pady=0, sticky = "w")

        self.lb_result2 = ctk.CTkLabel(self.frame_ballots_result, text=f"Notas de 2: {self.notas2}", font=("Century Gothic bold", 12))
        self.lb_result2.grid(row=8, column=0, padx=5, pady=0, sticky = "w")

        self.lb_result1 = ctk.CTkLabel(self.frame_ballots_result, text=f"Notas de 1: {self.notas1}", font=("Century Gothic bold", 12))
        self.lb_result1.grid(row=9, column=0, padx=5, pady=0, sticky = "w")

        self.btn_login_back = ctk.CTkButton(self.frame_ballots_result, width=300, height=15, text="Continuar cadastrando".upper(),font=("Century Gothic bold", 12), corner_radius=20, command=self.register_products)
        self.btn_login_back.grid(row=10, column=0, padx=10, pady=10)

        self.btn_view_products = ctk.CTkButton(self.frame_ballots_result, width=100, height=15, text="Produtos cadastrados".upper(),font=("Century Gothic bold", 12), corner_radius=20, command=self.registered_products)
        self.btn_view_products.grid(row=11, column=0, padx=10, pady=0, sticky = "w")

        self.btn_login_exit = ctk.CTkButton(self.frame_ballots_result, width=100, height=15, text="Sair".upper(),font=("Century Gothic bold", 12),corner_radius=20, command=self.tela_de_login)
        self.btn_login_exit.grid(row=11, column=0, padx=5, pady=0, sticky = "e")
        
    def registered_products(self):
        #Adiciona frame tela de resultados
        self.frame_registered_products = ctk.CTkFrame(self, width=380, fg_color="#dcdcdc", height=310)
        self.frame_registered_products.place(x=365, y=8)

        #Removendo a tela de cadastro
        self.frame_ballots_result.place_forget()

        #Titulo da tela de resultados
        self.lb_titlee = ctk.CTkLabel(self.frame_registered_products, text="Teste", font=("Century Gothic bold", 18))
        self.lb_titlee.grid(row=0, column=0, padx=5, pady=0)

    def limpa_entrys_cadastro(self):
        self.username_logon_entry.delete(0,END)
        self.usermail_logon_entry.delete(0,END)
        self.password_logon_entry.delete(0,END)
        self.confirm_password_logon_entry.delete(0,END)
    
    def limpa_entrys_login(self):
        self.username_login_entry.delete(0,END)
        self.password_login_entry.delete(0,END)

    def limpa_entrys_products(self):
        self.product_name_entry.delete(0,END)
        self.product_value_entry.delete(0,END)

# inicio do código com a chamada da função Menu()
if __name__=="__main__":
    app = App()
    app.mainloop()