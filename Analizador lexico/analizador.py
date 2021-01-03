# Jose Eduardo Zenteno Monteagudo
# jose.zenteno@ucsp.edu.pe

class Token:
    palabra = ""
    indice = -1
    tipo = ""
    # def __init__(self, p, t, i):
    #     palabra=p
    #     tipo=t
    #     indice=i
    def toString(self):
        return "Token[" + self.palabra + "]: pos = " + str(self.indice) + ", tipo = " + self.tipo
        


def reconoceNumero(linea,idx):
    token = Token()
    numero = ""
    token.indice = idx
    while(idx < len(linea) and linea[idx].isdigit()):
        numero += linea[idx]
        idx += 1
    token.palabra = numero
    token.tipo = "E"
    return token,idx

def reconoceVariable(linea,idx):
    token = Token()
    var = ""
    token.indice = idx
    while(idx < len(linea) and (linea[idx].isalpha() or linea[idx].isdigit())):
        var += linea[idx]
        idx += 1
    token.palabra = var
    token.tipo = "V"
    return token,idx

def reconoceSimbolo(linea,idx):
    token = Token()
    symbol = ""   
    token.indice = idx
    while(idx < len(linea) and not(linea[idx].isdigit()) and not(linea[idx].isalpha()) and not(linea[idx].isspace())):
        symbol += linea[idx]
        idx +=1
    token.palabra = symbol
    token.tipo = "O"
    return token,idx


def analizadorLexico(linea):
    tokens = []
    idx = 0
    while idx < len(linea):
        if linea[idx].isdigit():
            token,idx = reconoceNumero(linea, idx)
            tokens.append(token)
        elif linea[idx].isalpha():
            token,idx = reconoceVariable(linea,idx)
            tokens.append(token)
        elif linea[idx].isspace():
            idx=idx
        else:
            token,idx = reconoceSimbolo(linea,idx)
            tokens.append(token)
        idx += 1
            
    return tokens


def main():
    linea = "variable1 = tmp0 + 20 )"
    tokens = analizadorLexico(linea)
    for token in tokens:
        print(token.toString())
    

main()