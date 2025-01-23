import re
campos_nulos = []

def validar_nome(nome):
    if len(nome) > 10:
        return 
    campos_nulos.append('nome')
    return

def validar_idade(idade):
    try:
        idade=int(idade)
        if idade >0 and idade < 110:
            return 
        
    except ValueError:
        campos_nulos.append('nome')
        return
    
def validar_rua(rua):
    rua_valida = rua
    rua_valida == True if rua!=None else campos_nulos.append('rua')
    return rua_valida

    
def validar_genero(genero):
    try:
        if genero :
            return 
        campos_nulos.append('genero')
        return
    except UnboundLocalError:
        campos_nulos.append('genero')
        return 
    
def validar_numero(numero):
    try:
        numero=int(numero)
        if numero :
            return 
        campos_nulos.append('numero')
        return 
    
    except ValueError:
        campos_nulos.append('numero')
        return 

def validar_cep(cep):
    cep = str(cep).replace('-','')
    if len(cep)==8:
        return 
    campos_nulos.append('cep')
    return 

def validar_email(email):
    email_valido = re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.-]+$', email)
    if email_valido:
        return 
    campos_nulos.append('email')
    return 
    
def validar_bairro(bairro):
    bairro == True if bairro != None else campos_nulos.append('bairro')
    return bairro

def validar_cidade(cidade):
    if cidade != None:
       return 
    campos_nulos.append('cidade')
    return 

def validar_uf(uf):
    if uf != None:
        return True
    campos_nulos.append('uf')
    return False

def validacao(nome,idade,email,genero,cep,rua,numero,bairro,cidade,uf):
    validar_nome(nome)
    validar_idade(idade)
    validar_genero(genero)
    validar_rua(rua)
    validar_numero(numero)
    validar_cep(cep)
    validar_email(email)
    validar_bairro(bairro)
    validar_cidade(cidade)
    validar_uf(uf)

validacao('daniel sp',13, 'masculino', 'rua silva sales',2234, '12345-678', 'sdhasj@gmail.com', 'saldade', ' sao franciasco','sp')
if not campos_nulos:
    print('campos validados')
else:
    print(f'Campos nao validades: {','.join(campos_nulos)}')