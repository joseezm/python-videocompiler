# Jose Eduardo Zenteno Monteagudo
# jose.zenteno@ucsp.edu.pe


import re

def main():
    regex = re.compile('([a-z]|[A-Z]|_|-)+.*')
    text = "-1hola"
    if re.match(regex,text):
        print('“SI ES UNA VARIABLE”')
    else:
        print('“NO ES UNA VARIABLE”')


    

main()
