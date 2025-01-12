from pandas import DataFrame as df
def gerar_xlsx(pessoa):
    titulos=['Nome','Tel','Idade','Email','Genero','Rua','Numero','Complemento','Bairro','Cidade','UF']
    try:
        planilha == "PLANILHA GESTÂO DE PESSOAS": #definição da tabela em excel
        tabela = df(pessoa[0:], columns=titulos)
        documento = sg.popup_get_file("novo_item", save_as=True, default_extension=".xlsx")
        
        if documento:
            with pd.ExcelWriter(documento, engine='openpyxl') as escreve:
                tabela.to_excel(escreve, index=False)        
        sg.popup("Planilha salva")
    Exception as e:
        print(f'Erro{e}')
        

