import sqlite3
from sqlite3 import connect

def conexao_bd():
    try:
        conexao=connect('BD_Gestao')
        cursor= conexao.cursor()
        return conexao , cursor
    except sqlite3.Error:
        print('erro em conexao')
        return None, None

def salvar_dados(pessoa, conexao, cursor):
    cursor.execute("""insert into pessoa (nome,tel,idade,email,genero,rua,numero,complemento,bairro,cidade,uf)
                   values(?,?,?,?,?,?,?,?,?,?,?)"""
                   ,pessoa)
    conexao.commit()
    return


def mostrar_dados(cursor):
    pessoas= []
    cursor.execute("""select * from pessoa""")
    pessoa = cursor.fetchall()
    for pessoa_salva in pessoa:
        pessoas.append(pessoa_salva)
        print(f'id :{pessoa_salva[0]}\nnome :{pessoa_salva[1]}\nidade :{pessoa_salva[2]}\ntelefone :{pessoa_salva[3]}\nemail :{pessoa_salva[4]}\ngenro :{pessoa_salva[5]}\nrua :{pessoa_salva[6]}\nnumero :{pessoa_salva[7]}\ncomplemento :{pessoa_salva[8]}nbairro :{pessoa_salva[9]}\ncidade :{pessoa_salva[10]}\nuf :{pessoa_salva[11]}\n\n')
    return pessoas

def criar_tabela_gestao(pessoa):
    try:
        conexao, cursor = conexao_bd()
        if conexao:
            cursor.execute( """create table if not exists pessoa (
                        id integer primary key autoincrement,
                        nome text,
                        tel text,
                        idade integer,
                        email text,
                        genero text,
                        rua text,
                        numero integer,
                        complemento text,
                        bairro text,
                        cidade text,
                        uf text)""")
            
            conexao.commit()
            salvar_dados(pessoa,conexao,cursor)
            pessoas=mostrar_dados(cursor)
            conexao.close()
            return pessoas
        
        return 'A tabela pessoa não existe'
    except sqlite3.Error as e:
        return e





    
    