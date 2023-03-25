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

numProdutos = 0
vetPreco = []
vetProduto = []
valorTot = 0

#numProdutos = i = j = op = 0
#numProdutos=0

class BackEnd(): #A classe backend herda os componentes da classe principal App, por isso está dentro de App
    #def __init__(self):
        #self.numProdutos()
        
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
                    messagebox.showwarning(title="Sistema de Cadastro de Produtos", message="produto cad")
                    self.limpa_entrys_products()
                    for valor in (vetPreco): #verifica os valroes adicionados às posições
                        print(valor)
                    for nome in (vetProduto): #Verifica os produtos adicionados às posições
                        print(nome)

        except:
            
            traceback.print_exc()   

    def finish_registers(self):
        valorTot = sum(vetPreco)
        print(valorTot)
        

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

        self.password_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Senha..",font=("Century Gothic bold", 16), corner_radius=20, show="*", border_color="#490077")
        self.password_login_entry.grid(row=2, column=0, padx=10, pady=10)

        #self.ver_password_login_entry = ctk.CTkCheckBox(self.frame_login, text="Clique para ver a senha ", font=("Century Gothic bold", 12),corner_radius=25, border_color="#490077")
        #self.ver_password_login_entry.grid(row=3, column=0, padx=10,pady=5)

        self.btn_login = ctk.CTkButton(self.frame_login, width=300, fg_color="#490077", text="Login",font=("Century Gothic bold", 16),corner_radius=20, command=self.verify_login)
        self.btn_login.grid(row=4, column=0, padx=10, pady=10)

        self.span = ctk.CTkLabel(self.frame_login, text="Não possui cadastro?", font=("Century Gothic", 10))
        self.span.grid(row=5, column=0, padx=10)

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
        self.btn_login_back.grid(row=10, column=0, padx=10, pady=50)
        '''
    def ballots_result(self):
        #Adiciona frame tela de resultados
        self.frame_results = ctk.CTk(self, width=380, fg_color="#dcdcdc", height=310)
        self.frame_results.place(x=365, y=8)

        #Removendo a tela de cadastro
        self.frame_register_produtcs.place_forget()
        
        #Titulo da tela de resultados
        self.lb_title = ctk.CTkLabel(self.frame_results, text="Resultado da quantidade de notas", font=("Century Gothic bold", 22))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        #Widgets frame de resultados
        '''

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


'''
if op == 1:

    #Carrinho()

    while numProdutos < 10:
        vetProduto[numProdutos] = input("Produto a ser cadastrado: ")
        vetPreco[numProdutos] = int(input("Preco do produto em R$: "))
        numProdutos += 1
        valorTot += vetPreco[numProdutos-1]
        opc = input("Deseja continuar as compras? [Sim/Nao]: ")

        #Carrinho()

        if opc == "Nao" or numProdutos == 10:
            Carrinho()
            valorRestante = valorTot

            for j in range(0, numProdutos):
                if vetProduto[j] != "" and vetPreco[j] != 0:
                    print("Produto n.", j+1, ": ",
                          vetProduto[j], ". No valor de R$", vetPreco[j])

            for i in range(6, -1, -1):
                qtdNotas[i] = valorRestante // notas[i]
                qtdTotalNotas += qtdNotas[i]
                valorRestante %= notas[i]

            for i in range(7):
                if qtdNotas[i] > 0:
                    print(qtdNotas[i], " nota(s) de R$ ", notas[i])
                    print("A quantidade mínima de notas é: ", qtdTotalNotas, " notas")
                    print("Obrigado por comprar conosco!")
            break

if op == 2:
    print("Nada foi adicionado ao carrinho. Obrigado e volte sempre!")
    '''