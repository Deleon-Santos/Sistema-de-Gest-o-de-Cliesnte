

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

    #configuração do layout
    def layout(self):
        self.title('Gesntão de Clientes')
        self.geometry('1080x740')
        

    #configuração dos modos de aparencia
    def aparencia(self):
        pass

    #frame onde vai rodar o sistema vais receber todos os entrys e labels e botões 
    def frame_master(self):
        pass

        #função para pegar os valores
        def pegar_valores(self):
            pass

        #função para limpa os resultados
        def Limpar_valores(self):
            pass

    #função para alterna a aparencia do sistema
    def cambiar_modo(self):
        pass



if __name__=='__main__':
    app=Janela()#app recebe a janela
    app.mainloop()#app inicia o loop


