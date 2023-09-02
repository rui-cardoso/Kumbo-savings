import tkinter as tk
from tkinter import ttk
import json
from PIL import ImageTk, Image
from datetime import*
from tkinter import messagebox
from model.Cliente import *
from model.ClientLinkedList import *

class View:
        def __init__(self, master): 
            self.master = master
            self.clientes = ClientLinkedList() #Criação da lista de clientes
            self.tela_login() 
            
            #Frame Login
            #self.master.resizable(True, True)
        def tela_login(self):
                
            # tela Login
            self.master.resizable(True, True)
            self.frame_login = tk.Frame(self.master,width=800, height=700, bg='#DCDCDC')
            self.frame_login.pack()
            
            self.label_login = tk.Label(self.frame_login,text= "FAÇA O LOGIN:", font=("Arial", 23, "bold"), bg='#DCDCDC')
            self.label_login.pack()

                #Imagem
            self.logo = Image.open('makeitrain.png')
            self.resized = self.logo.resize((300,225), Image.ANTIALIAS)
            self.login_image = ImageTk.PhotoImage(self.resized)
                #self.logo = self.logo.subsample(5)
            self.logo_label = tk.Label(self.frame_login, image=self.login_image,bg='#DCDCDC')
            self.logo_label.place(relx=1.0, anchor='ne')
            self.logo_label.pack()

                #Label + Entry para username
            self.nome_label = tk.Label(self.frame_login, text="USERNAME:", font=('Arial', 14), bg='#DCDCDC')
            self.nome_label.pack()
            self.nome_entry = tk.Entry(self.frame_login, font=('Arial', 14))
            self.nome_entry.pack(pady=5)

                #Label + Entry para password
            self.password_label = tk.Label(self.frame_login, text="Password:", font=('Arial', 14), bg='#DCDCDC')
            self.password_label.pack()
            self.password_entry = tk.Entry(self.frame_login, show="*", font=('Arial', 14))
            self.password_entry.pack(pady=5)
                
                # SHOW/HIDE PASSWORD
            self.show_checkbox = tk.Checkbutton(self.frame_login, text= 'SHOW PASSWORD', bg='#DCDCDC', cursor="hand2", bd=0, command= self.show_password)
            self.show_checkbox.pack()
                #Label + Entry para NIF
            """self.nif_label = tk.Label(self.frame , text="NIF:", font=("Arial" , 14), bg="#DCDCDC")
            self.nif_label.pack()
            self.nif_entry = tk.Entry(self.frame,font=("Arial",14))
            self.nif_entry.pack(pady=5)"""

                #Botões de Login + registo
            self.login_button = tk.Button(self.frame_login, text="Login", font=('Arial', 14 , 'bold'),fg='white', bg='#0c84ed', cursor="hand2", command= self.login)
            self.login_button.pack()
                # ainda nao tem conta ?

            self.texto_ainda_nao_tem_conta = tk.Label(self.frame_login,text="Ainda nao tem conta ?", font=("Times 20 italic bold",11), bg="#DCDCDC")
            self.texto_ainda_nao_tem_conta.pack()

            self.registo_button = tk.Button(self.frame_login, text="Registo", font=('Arial', 14), fg='white', bg='#17ed11', cursor="hand2",command= self.tela_registro)
            self.registo_button.pack()

                  
        
        
        
                
        def show_password(self):
            if self.password_entry.cget('show') == "*":
                self.password_entry.config(show="")
            else:
                self.password_entry.config(show="*")
            
                
  

        def check_nif(self):
            if len(self.nif_entry) != 9 and self.nif_entry[0] not in ['1','2','3']:
                return messagebox.showwarning(message= "NIF INVALIDO!")
            else:
                return True
        
        
        
        
        def registar(self):
              #Implementar a função registo()
            nome = self.nome_entry.get()
            password = self.password_entry.get()
            nif = self.nif_entry.get()
            if nome =="" or password == "" or nif == "":
                messagebox.showwarning(title='Erro de Registo', message="Username ou password invalido.")
            elif len(nif) !=9 or nif[0] not in ["1","2","3"]:
                return messagebox.showwarning(message= "NIF INVALIDO!")
            elif self.clientes.find_username(nome) != -1:
                messagebox.showwarning(title = "Erro de registo", message="Username ou NIF existente.")
            else:
                cliente = Cliente(nome,nif,password)
                self.clientes.insert_last(cliente)
                messagebox.showinfo(title="Sucesso",message="Username criado com sucesso!")


        def login(self):
        # Implement the login function
            nome = self.nome_entry.get()
            password = self.password_entry.get()

            if nome == "" or password == "":
                messagebox.showwarning(title="Erro", message="Username ou password inválido")
            elif self.clientes.find_username(nome) > -1:
                messagebox.showinfo(title="Sucesso", message="Login feito com sucesso")
                self.dashboard()  # Call the dashboard method after successful login
            else:
                messagebox.showwarning(title="Erro", message="Username não existente.")

                
        def back(self):
            self.frame_registro.pack_forget()
            self.frame_login.pack()
        
            
        def tela_registro(self):
            
            self.frame_login.pack_forget()
            self.frame_registro = tk.Frame(self.master,width=800, height=700, bg='#DCDCDC')
            self.frame_registro.pack()
            
            self.label_registar = tk.Label(self.frame_registro,text= "FAÇA O SEU REGISTO:", font=("Arial", 23, "bold"), bg='#DCDCDC')
            self.label_registar.pack()
            
            self.imagem_registro = Image.open('makeitrain.png')
            self.resized_r = self.imagem_registro.resize((300,225), Image.ANTIALIAS)
            self.r_image = ImageTk.PhotoImage(self.resized_r)
            #self.logo = self.logo.subsample(5)
            self.i_r_label = tk.Label(self.frame_registro, image= self.r_image, bg='#DCDCDC')
            #logo_label.place(relx=1.0, anchor='ne')
            self.i_r_label.pack(pady=5)
            
            self.nome_label = tk.Label(self.frame_registro , text="USERNAME:", font=('Arial', 14), bg='#DCDCDC')
            self.nome_label.pack()
            self.nome_entry = tk.Entry(self.frame_registro , font=('Arial', 14))
            self.nome_entry.pack(pady=5)

            #Label + Entry para password
            self.password_label = tk.Label(self.frame_registro , text="Password:", font=('Arial', 14), bg='#DCDCDC')
            self.password_label.pack()
            self.password_entry = tk.Entry(self.frame_registro , show="*", font=('Arial', 14))
            self.password_entry.pack(pady=5)
            
            
            self.show_checkbox = tk.Checkbutton(self.frame_registro, text= 'SHOW PASSWORD', bg='#DCDCDC', cursor="hand2", bd=0, command= self.show_password)
            self.show_checkbox.pack()
            
            
            
            self.nif_label = tk.Label(self.frame_registro , text="NIF:", font=("Arial" , 14), bg="#DCDCDC")
            self.nif_label.pack()
            self.nif_entry = tk.Entry(self.frame_registro,font=("Arial",14))
            self.nif_entry.pack(pady=5)
            
            
            
            
            
            self.register_button = tk.Button(self.frame_registro, text="REGISTAR", font=('Arial', 14 , 'bold'),fg='white', bg='#02fa38', cursor="hand2", command= self.registar)
            self.register_button.pack(pady= 5)
            
            self.back_button = tk.Button(self.frame_registro, text="<- VOLTAR", font=('Arial', 14 , 'bold'),fg='white', bg= "grey", cursor="hand2", command=self.back)
            self.back_button.pack(pady= 5)
            
            
        def logout(self):
            self.master.destroy()
            
            
        
        
        
        
            
        def dashboard(self):
            self.frame_login.pack_forget()
            self.master.geometry("1366x768")
            self.master.state("zoomed")
            #==================================HEADER=======================================
            
            self.header = tk.Frame(self.master, bg="#009df4")
            self.header.place(x=300 , y=0, width=1070, height=60)
            self.logout_text = tk.Button(self.master, text="LOGOUT", bg="red", font=("", 13, "bold"), bd="0", fg="white", cursor="pirate",
                                         activebackground="red",command= self.logout)
            self.logout_text.place(x=950,y=15)
            #=========================================================================
            #==================================SIDE BAR=======================================
            self.side_bar = tk.Frame(self.master, bg="#ffffff")
            self.side_bar.place(x=0, y=0, width=300, height=750)
            
            self.resized = self.logo.resize((300,225), Image.ANTIALIAS)
            self.login_image = ImageTk.PhotoImage(self.resized)
            self.userImage = Image.open("user.png")
            self.resized = self.userImage.resize((150,150), Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(self.resized)
            self.logo_image = tk.Label(self.side_bar, image=self.photo, bg="#ffffff")
            self.logo_image.image = self.photo
            self.logo_image.place(x=70, y=80)
            
            # Name of brand/person
            self.brand_name = tk.Label(self.side_bar, text= self.nome_entry.get() , bg= "#ffffff" ,font=("", 15, "bold") )
            self.brand_name.place(x=80, y=200)
            
            #=========================================================================
            #==================================BODY=======================================
            
            self.heading = tk.Label(self.master, text="DASHBOARD",font=("", 13, "bold") , fg="#0064d3", bg="#eff5f6")
            self.heading.place(x=325, y=70)
            #=========================================================================
            #==================================BODY frame 1=======================================
            self.body1 = tk.Frame(self.master, bg="#ffffff")
            self.body1.place(x=328,y=210,width=1040, height=450) 

            self.categorias = tk.Label(self.body1, text = " CATEGORIAS ", font=('Microsoft YaHei UI light',18), bg='#fff')
            self.categorias.place(x=100, y=20)

            self.combo_categorias = ttk.Combobox( self.body1,state="readonly", values=["Alimentacao","Moradia","Transporte","Lazer"])
            self.combo_categorias.place(x=100, y=60)
            
            self.categorias1 = tk.Label(self.body1, text = "Data da despesa", font=('Microsoft YaHei UI light',10), bg='#fff')
            #self.categorias1.place(x=100, y=60)
            
            self.categorias1 = tk.Entry(self.body1, font=('Microsoft YaHei UI', 10), width=50)
            #self.categorias1.place(x=100, y=80)
            self.descrição_da_despesa1 = tk.Label(self.body1, text = "Descriçaõ da despesa", font=('Microsoft YaHei UI light',10), bg='#fff')
            self.descrição_da_despesa1.place(x=100, y=100)
            self.descrição_da_despesa1 = tk.Entry(self.body1, font=('Microsoft YaHei UI', 10), width=50)
            self.descrição_da_despesa1.place(x=100, y=120)
            

            self.categorias2 = tk.Label(self.body1, text = "Valor da despesa:", font=('Microsoft YaHei UI light',10), bg='#fff')
            self.categorias2.place(x=100, y=140)
            
            self.categorias2 = tk.Entry(self.body1, font=('Microsoft YaHei UI', 10), width=50)
            self.categorias2.place(x=100, y=160)
            
            #self.descrição_da_despesa2 = tk.Label(self.body1, text = "Descriçaõ da despesa", font=('Microsoft YaHei UI light',10), bg='#fff')
            #self.descrição_da_despesa2.place(x=100, y=180)
            
            #self.descrição_da_despesa2 = tk.Entry(self.body1, font=('Microsoft YaHei UI', 10), width=50)
            #self.descrição_da_despesa2.place(x=100, y=200)
            


            """self.categorias3 = tk.Label(self.body1, text = "Moradia", font=('Microsoft YaHei UI light',10), bg='#fff')
            self.categorias3.place(x=100, y=220)
            
            self.categorias3 = tk.Entry(self.body1, font=('Microsoft YaHei UI', 10), width=50)
            self.categorias3.place(x=100, y=240)
            
            self.descrição_da_despesa3 = tk.Label(self.body1, text = "Descriçaõ da despesa", font=('Microsoft YaHei UI light',10), bg='#fff')
            self.descrição_da_despesa3.place(x=100, y=260)
            
            self.descrição_da_despesa3 = tk.Entry(self.body1, font=('Microsoft YaHei UI', 10), width=50)
            self.descrição_da_despesa3.place(x=100, y=280)
            

            self.categorias4 = tk.Label(self.body1, text = "Lazer", font=('Microsoft YaHei UI light',10), bg='#fff')
            self.categorias4.place(x=100, y=300)
            
            self.categorias4 = tk.Entry(self.body1, font=('Microsoft YaHei UI', 10), width=50)
            self.categorias4.place(x=100, y=320)
            
            self.descrição_da_despesa4 = tk.Label(self.body1, text = "Descriçaõ da despesa", font=('Microsoft YaHei UI light',10), bg='#fff')
            self.descrição_da_despesa4.place(x=100, y=340)
            
            self.descrição_da_despesa4 = tk.Entry(self.body1, font=('Microsoft YaHei UI', 10), width=50)
            self.descrição_da_despesa4.place(x=100, y=360)"""
              
            
            
            
            
            
            
            



