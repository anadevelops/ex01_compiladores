caracteres = []
tokens = []
palavras_reservadas = {'def': 'DEF', 'int': 'INT', 'return':'RETURN'}


def ident(posicao, lista):
    palavra = ''
    if lista[posicao].isalpha():
        while lista[posicao].isalpha():
            palavra += lista[posicao]
            posicao += 1

        if palavra in palavras_reservadas.keys():
            tokens.append(palavras_reservadas.get(palavra))
        else:
            tokens.append('IDENT')
        return posicao
    return False

def branco(posicao, lista):
    if lista[posicao] == ' ' or lista[posicao] == '\n':
        tokens.append('BRANCO')
        posicao += 1
        return posicao
    return False

def outro(posicao, lista):
    if not lista[posicao].isalpha() and lista[posicao] != ' ' and not lista[posicao].isdigit():
        tokens.append('OUTRO')
        posicao += 1
        return posicao
    return False

def numero(posicao, lista):
    if posicao < len(lista) and lista[posicao].isdigit():
        pf = False
        
        while posicao < len(lista) and (lista[posicao].isdigit() or lista[posicao] == '.'):
            if lista[posicao] == '.' and lista[posicao+1].isdigit():
                if pf:
                    break 
                pf = True
            elif lista[posicao] == '.' and not lista[posicao+1].isdigit():
                break
            posicao += 1
            
        if pf:
            tokens.append('NPF')
        else:
            tokens.append('NI')
            
        return posicao
    return False


with open('entrada.txt', 'r', encoding='utf-8') as entrada:
    conteudo = entrada.read()
    for caractere in conteudo:
        if caractere:
            caracteres.append(caractere)
        else:
            break

i = 0
while i < len(caracteres):
    if nova_posicao := ident(i, caracteres):
        i = nova_posicao
    elif nova_posicao := branco(i, caracteres):
        i = nova_posicao
    elif nova_posicao := outro(i, caracteres):
        i = nova_posicao
    elif nova_posicao := numero(i, caracteres):
        i = nova_posicao

tokens = [token for token in tokens if token != "BRANCO"]
print(tokens)