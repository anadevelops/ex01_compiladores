caracteres = []
tokens = []

def ident(posicao, lista):
    if lista[posicao].isalpha():
        while lista[posicao].isalpha():
            posicao += 1
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
    if not lista[posicao].isalpha() and lista[posicao] != ' ':
        tokens.append('OUTRO')
        posicao += 1
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
        #print(f'LOG [i = {i}, nova_posicao = {nova_posicao}]')
    elif nova_posicao := branco(i, caracteres):
        #print(i, nova_posicao)
        #print(tokens)
        i = nova_posicao
    elif nova_posicao := outro(i, caracteres):
        i = nova_posicao

tokens = [token for token in tokens if token != "BRANCO"]
print(tokens)

        
                


