import re

def validar_nome(nome):
    if len(nome) > 10:
        return True
    return

def validar_idade(idade):
    try:
        idade=int(idade)
        if idade >0 and idade < 110:
                return True
        return
    except ValueError:
        return False
    
def validar_rua(rua):
    rua == True if rua!=None else False
    return rua
    

def validar_genero(genero):
    try:
        if genero in ("Masculino, Feminino"):
            return True
        return
    except UnboundLocalError:
        return
    
def validar_numero(numero):
    try:
        numero=int(numero)
        if numero is not None:
            return True
        return
    
    except ValueError:
        return False