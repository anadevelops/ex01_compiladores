caracteres = []
tokens = []
tabela_simbolos = {}
palavras_reservadas = ('def', 'int', 'if', 'return')
linha_atual = 1

with open('entrada.txt', 'r', encoding='utf-8') as entrada:
    conteudo = entrada.read()
    for caractere in conteudo:
        if caractere:
            caracteres.append(caractere)
        else:
            break

def ident(posicao, lista):
    global linha_atual
    palavra = ''
    if lista[posicao].isalpha():
        while posicao <len(lista) and (lista[posicao].isalnum() or lista[posicao] == '_'):
            palavra += lista[posicao]
            posicao += 1

        tokens.append(palavra)

        if palavra not in tabela_simbolos:
            tabela_simbolos[palavra] = []

        if linha_atual not in tabela_simbolos[palavra]:
            tabela_simbolos[palavra].append(linha_atual)

        return posicao
    return False

def branco(posicao, lista):
    global linha_atual
    if lista[posicao] == ' ' or lista[posicao] == '\n':
        if lista[posicao] == '\n':
            linha_atual += 1
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

saida = ''
for token in sorted(tabela_simbolos.keys()):
    linhas_str = ', '.join(map(str, tabela_simbolos[token]))
    saida += f'{token}[{linhas_str}]'

print(saida)