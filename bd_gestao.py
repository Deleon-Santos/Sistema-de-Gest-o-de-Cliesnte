from sqlite3 import connect

def conexao_bd():
    try:
        conexao=connect('BD_Gestao')
        cursor= conexao.cursor()
        return conexao , cursor
    except:
        print('erro em conexao')

def criar_tabela_gestao(conexao, cursor):
    try:
        
        cursor.execute( """create table if not exists pessoa
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
                    uf text""")
        print('tablela foi criada com sucesso')
        conexao.commit()
        
        return True
    except Exception as e:
        print(f'Erro de conexao {e}')

def salvar_dados(pessoa, conexao, cursor):
    cursor.execute("""insert into pessoa (nome,tel,idade,email,genero,rua,numero,complemento,bairro,cidade,uf)
                   values(?,?,?,?,?,?,?,?,?,?,?)"""
                   ,pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],pessoa[5],pessoa[6],pessoa[7],pessoa[8],pessoa[9],pessoa[10])
    conexao.commit()
    
    if conexao:
        conexao.close()
        cursor.close()

def verificar_tabela(pessoa):
    try:
        conexao, cursor = conexao_bd()
        tabela=criar_tabela_gestao(conexao, cursor)
        if tabela:
        
            salvar_dados(pessoa, conexao, cursor)
            return True
    except :
        print('tablela nao existia')
        
         
    
    