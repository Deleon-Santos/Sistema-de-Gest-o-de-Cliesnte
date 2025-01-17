

"""Sistema de Gestão de Pessoas com Python e POO"""

#importação de bibliotecas
import customtkinter as ctk
from tkinter import * 
from tkinter import messagebox
import bd_gestao as bd
import validar_entradas as validar


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
        self.title('Gestão de Clientes')
        self.geometry('840x640')
        

    #configuração dos modos de aparencia
    def aparencia(self):
        self.label_modo = ctk.CTkLabel(self, text=('Tema'), bg_color='transparent',text_color=['#000','#fff'],font=('ariel',15)).place(x=90, y=530)
        self.opt_modo = ctk.CTkOptionMenu(self, values=['Light','Dark','Sistem'], command= self.cambiar).place(x=90, y=560)
    

    #frame onde vai rodar o sistema vais receber todos os entrys e labels e botões 
    def frame_master(self):
        def salvar():
            campos_nulos=[]   

            nome = nome_value.get() 
            confirmar_nome=validar.validar_nome(nome)
            if confirmar_nome != True:
                campos_nulos.append('Nome')

            tel=tel_value.get()

            idade=idade_value.get()
            confirmar_idade=validar.validar_idade(idade)
            if confirmar_idade != True:
                campos_nulos.append('idade')

            email=email_value.get()
            try:
                genero=genero_value.get(genero)
                print(genero)
                confirmar_genero=validar.validar_genero(genero)
                if confirmar_genero != True:
                    genero = 'idefinido'
            except UnboundLocalError:
                genero = 'idefinido'

            cep=cep_value.get()

            rua=rua_value.get()
            confirmar_rua=validar.validar_rua(rua)
            if confirmar_rua != True:
                campos_nulos.append('rua')
            
            numero=numero_value.get()
            confirmar_numero=validar.validar_numero(numero)
            if confirmar_numero != True:
                campos_nulos.append('numero')

            complemento=complemento_value.get()
            bairro=bairro_value.get()
            cidade=cidade_value.get()
            uf=uf_value.get()
            if len(campos_nulos) ==0:

                print(campos_nulos)
                    #metodos para gravar e mostras as informações
                def mostrar_info(pessoa):
                    resposta=bd.criar_tabela_gestao(pessoa)
                    messagebox.showinfo(title='documento salvo',message=f'{resposta}')
                    print(campos_nulos)
                mostrar_info(pessoa=[nome,tel,idade,email,genero,cep,rua,numero,complemento,bairro,cidade,uf])
                return
            
            messagebox.showinfo(title="erro", message=f'Os campos {",".join(campos_nulos)} não foram preenchidos')
            
            
           

        #função para limpa os resultados
        def limpar():
            nome_value.set('')
            tel_value.set('')
            idade_value.set('')
            email_value.set('')
            genero_value.set('')
            cep_value.set('')
            rua_value.set('')
            numero_value.set('')
            complemento_value.set('')
            bairro_value.set('')
            cidade_value.set('')
            uf_value.set('')
            
        #capturando os valos dentro das entrys
        nome_value = StringVar(value='joão P Santos')
        tel_value = StringVar(value='11912345678')
        idade_value = StringVar(value='25')
        email_value = StringVar(value='dsdh@gmm.com.br')
        genero_value = StringVar()
        rua_value = StringVar(value='Mario Veloso Serqueira')
        bairro_value = StringVar(value='Carlos Drummord Andrade')
        cidade_value = StringVar(value='Caracas')
        cep_value = StringVar(value='06666000')
        complemento_value = StringVar(value='b')
        numero_value = StringVar(value='43')
        uf_value = StringVar(value='RN')
        #obs_value = StringVar()
        
        frame_titulo = ctk.CTkFrame(self, width=650 , height=50, corner_radius=10,border_width=2 ,border_color= 'teal', bg_color='teal',fg_color="teal").place(x=90, y=60)
        label_titulo = ctk.CTkLabel(self, text="GESTÃO DE PESSOAS", font=('ariel',30), text_color=['#000','#fff'],bg_color='transparent',fg_color='transparent').place(x=250, y=70)
        label_nome = ctk.CTkLabel(self,text='Nome Completo', text_color=['#000','#fff'],font=('ariel',15)).place(x=90, y=150)
        entry_nome = ctk.CTkEntry(self, textvariable=nome_value,font=('ariel',20),width=480).place(x=90,y=180)
        label_tel = ctk.CTkLabel(self,text='Tel/Celular',text_color=['#000','#fff'],font=('ariel',15)).place(x=590, y=150)
        entry_tel = ctk.CTkEntry(self,textvariable=tel_value, font=('ariel',20),width=150).place(x=590,y=180)
        label_mail = ctk.CTkLabel(self,text='E-mail', font=('ariel',15),text_color=['#000','#fff']).place(x=90,y=220)
        entry_mail = ctk.CTkEntry(self, textvariable=email_value,font=('ariel',20),width=440).place(x=90,y=250)
        label_idade = ctk.CTkLabel(self,text='Idade', text_color=['#000','#fff'],font=('ariel',15)).place(x=550, y=220)
        entry_idade = ctk.CTkEntry(self,textvariable=idade_value, font=('ariel',20),width=50).place(x=550,y=250)
        label_genero = ctk.CTkLabel(self,text='Genero', text_color=['#000','#fff'],font=('ariel',15)).place(x=620, y=220)
        entry_genero = ctk.CTkComboBox(self,values=['Masculino','Feminino'], width=120, text_color=['#000','#fff'],font=('ariel',15)).place(x=620, y=250)
        label_rua = ctk.CTkLabel(self,text='Rua', text_color=['#000','#fff'],font=('ariel',15)).place(x=90, y=290)
        label_numero = ctk.CTkLabel(self,text='N°', text_color=['#000','#fff'],font=('ariel',15)).place(x=610, y=290)
        label_complemento = ctk.CTkLabel(self,text='Compl', text_color=['#000','#fff'],font=('ariel',15)).place(x=690, y=290)
        entry_rua = ctk.CTkEntry(self,textvariable=rua_value, font=('ariel',20),width=500).place(x=90,y=320)
        entry_numero = ctk.CTkEntry(self, textvariable=numero_value,font=('ariel',20),width=60).place(x=610,y=320)
        entry_complemento = ctk.CTkEntry(self, textvariable=complemento_value,font=('ariel',20),width=50).place(x=690,y=320)
        label_cep = ctk.CTkLabel(self,text='CEP', text_color=['#000','#fff'],font=('ariel',15)).place(x=90, y=360)
        label_bairro = ctk.CTkLabel(self,text='Bairro', text_color=['#000','#fff'],font=('ariel',15)).place(x=250, y=360)
        label_cidade = ctk.CTkLabel(self,text='Cidade', text_color=['#000','#fff'],font=('ariel',15)).place(x=500, y=360)
        label_uf = ctk.CTkLabel(self,text='UF', text_color=['#000','#fff'],font=('ariel',15)).place(x=700, y=360) 
        entry_cep = ctk.CTkEntry(self, textvariable=cep_value,font=('ariel',20),width=140).place(x=90,y=390)
        entry_bairro = ctk.CTkEntry(self,textvariable=bairro_value, font=('ariel',20),width=230).place(x=250,y=390)
        entry_cidade = ctk.CTkEntry(self,  textvariable=cidade_value,font=('ariel',20),width=180).place(x=500,y=390)
        entry_uf = ctk.CTkEntry(self,  textvariable=uf_value,font=('ariel',20),width=40).place(x=700,y=390)
        label_obs = ctk.CTkLabel(self,text='Observação', text_color=['#000','#fff'],font=('ariel',15)).place(x=90, y=430)
        entry_obs = ctk.CTkTextbox(self,  font=('ariel',20),width=650, height=60, fg_color='transparent',border_color='#aaa',border_width=1).place(x=90,y=460)
        btn_salvar = ctk.CTkButton(self,text='Salvar'.upper(),command=salvar,text_color=['#000','#fff'],font=('ariel',15),hover_color='teal').place(x=350,y=560)
        btn_salvar = ctk.CTkButton(self,text='Limpar'.upper(),command=limpar,text_color=['#000','#fff'],font=('ariel',15),hover_color='teal').place(x=600,y=560)
        #função para pegar os valores
      

    #função para alterna a aparencia do sistema
    def cambiar(self,nova_aparencia):
        ctk.set_appearance_mode(nova_aparencia)
    

if __name__=='__main__':
    app=Janela()#app recebe a janela
    app.mainloop()#app inicia o loop



