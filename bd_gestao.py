from sqlite3 import connect

def conexao_bd():
    try:
        conexao=connect('BD_Gestao')
        cursor= conexao.cursor()
        return conexao , cursor
    except:
        print('erro em conexao')

def criar_tabela_gestao():
    try:
        conexao, cursor = conexao_bd()
        cursor.execute( """create table if not exists pessoa:
                        nome text,
                    tel text,
                    idade integer,
                    email taxt,
                    genero text,
                    rua text,
                    numero integer,
                    complemento text,
                    bairro text,
                    cidade text,
                    uf text""")
        print('tablela foi criada com sucesso')

        verificar_tabela()
    except:
        print('Erro de conexao')

def verificar_tabela():
    try:
        conexao, cursor = conexao_bd()
        cursor.execute("""SELECT count(*) from pessoa""")
        resultado = cursor.fetchone()

        if resultado:
            print(f"A tabela existe.")
            return True
    except :
        criar_tabela_gestao()
        print('tablela foi criada com sucesso')
    """finally:
        if conexao:
            conexao.close()
            cursor.close()
"""
    