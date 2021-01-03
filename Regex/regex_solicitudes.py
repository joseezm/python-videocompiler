# Jose Eduardo Zenteno Monteagudo
# jose.zenteno@ucsp.edu.pe


import re



def main():
    
    regex = re.compile('(me gustaria|le quiero pedir|le pido por favor que)([a-z]|[A-Z]|[0-9]|[äáàëéèíìöóòúùñç]|,|;| )*\.')
    text = "Por ese motivo, me gustaria pedirle más información sobre los temas recientemente tocados. Estaría muy agradecido y en verdad le deseo una bonita tarde. Hasta luego."
    res = re.search(regex,text)
    print( "TEMA: " + text[int(res.start()) : int(res.end())])
    

main()

