# Jose Eduardo Zenteno Monteagudo
# jose.zenteno@ucsp.edu.pe

import re

def main():
    regex = re.compile('[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]')
    text = "299.299.299.299"
    if re.match(regex,text):
        print('“SI ES UNA IP”')
    else:
        print('“NO ES UNA IP”')



main()