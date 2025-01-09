

"""Sistema de Gestão de Pessoas com Python e POO"""
#importação de bibliotecas
import customtkinter as ctk
from tkinter import *

# class que define a aparencia
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

# Super class APK
class Janela(ctk.CTk):
    def __init__(self):
        super().__init__()#todas as funcionalidades devem ser chamadas apartir da superclass
        self.layout()
        self.frame_master()
        self.aparencia()
        
    #configuração do layout
    def layout(self):
        self.title('Gesntão de Clientes')
        self.geometry('840x740')
        

    #configuração dos modos de aparencia
    def aparencia(self):
        self.label_modo = ctk.CTkLabel(self, text=('Tema'), bg_color='transparent',text_color=['#000','#fff'],font=('ariel',15)).place(x=90, y=500)
        self.opt_modo = ctk.CTkOptionMenu(self, values=['Light','Dark','Sistem'], command= self.cambiar).place(x=90, y=540)
    

    #frame onde vai rodar o sistema vais receber todos os entrys e labels e botões 
    def frame_master(self):
        frame_titulo = ctk.CTkFrame(self, width=650 , height=50, corner_radius=10,border_width=2 ,border_color= 'yellow', bg_color='teal',fg_color="teal").place(x=90, y=60)
        label_titulo = ctk.CTkLabel(self, text="GESTÃO DE PESSOAS", font=('ariel',30), text_color='#fff',fg_color='transparent').place(x=250, y=70)
        label_nome = ctk.CTkLabel(self,text='Nome Completo', text_color='#fff',font=('ariel',15)).place(x=90, y=150)
        entry_nome = ctk.CTkEntry(self, font=('ariel',20),width=450).place(x=90,y=180)
        label_tel = ctk.CTkLabel(self,text='Tel/Celular', text_color='#fff',font=('ariel',15)).place(x=590, y=150)
        entry_tel = ctk.CTkEntry(self, font=('ariel',20),width=150).place(x=590,y=180)
        label_mail = ctk.CTkLabel(self,text='E-mail', font=('ariel',15),text_color='#fff').place(x=90,y=290)
        label_idade = ctk.CTkLabel(self,text='Idade', text_color='#fff',font=('ariel',15)).place(x=550, y=290)
        label_genero = ctk.CTkLabel(self,text='Genero', text_color='#fff',font=('ariel',15)).place(x=620, y=290)
        entry_mail = ctk.CTkEntry(self, font=('ariel',20),width=430).place(x=90,y=320)
        entry_idade = ctk.CTkEntry(self, font=('ariel',20),width=40).place(x=550,y=320)
        label_nome = ctk.CTkComboBox(self,values=['Masculino','Feminino'], width=120, text_color='#fff',font=('ariel',15)).place(x=620, y=320)
        
        #função para pegar os valores
        def pegar_valores(self):
            pass

        #função para limpa os resultados
        def Limpar_valores(self):
            pass

    #função para alterna a aparencia do sistema
    def cambiar(self,nova_aparencia):
        ctk.set_appearance_mode(nova_aparencia)
    




if __name__=='__main__':
    app=Janela()#app recebe a janela
    app.mainloop()#app inicia o loop


