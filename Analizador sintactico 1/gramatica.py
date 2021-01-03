# Jose Eduardo Zenteno Monteagudo
# jose.zenteno@ucsp.edu.pe


class Produccion:
    izq = ""
    der = ""

class Gramatica:
    produccion = []
    terminales = []
    noterminales = []
    
    def imprimir(self):
        for i in self.produccion:
            print(i.izq + " -> " + i.der)
            
    def cargar (self,text):
        lista = text.split('\n')
        separador = '->'
        if(':=' in text):
            separador = ':='
        
        # LISTA DE NO TERMINALES
        for nt in lista:
            aux = nt.split(separador)
            if(aux[0].strip() != ''):
                self.noterminales.append(aux[0].strip())
        
        for i in lista:
            
            prod = Produccion()
            aux = i.split(separador)
            if(aux[0].strip() != ''):
                prod.izq = aux[0].strip()
                if('|' in aux[1]):
                    aux2 = aux[1].split('|')
                    for e in aux2:
                        prod2 = Produccion()
                        prod2.izq = prod.izq
                        prod2.der = e.strip()
                        self.produccion.append(prod2)
                        aux3= e.strip().split(' ')
                        for x in aux3:
                            if(x in self.noterminales):
                                x=x
                            else:
                                self.terminales.append(x)
                else:
                    prod.der = aux[1].strip()
                    self.produccion.append(prod)
                    aux3 = aux[1].strip().split(' ')
                    for x in aux3:
                        if(x in self.noterminales):
                            x=x
                        else:
                            self.terminales.append(x)
                            
        #ELIMINAR REPETIDOS
        self.terminales = list(dict.fromkeys(self.terminales))
        self.noterminales = list(dict.fromkeys(self.noterminales))
                

    def getProduccion(self,izq):
        lista = []
        for i in self.produccion:
            if(i.izq == izq):
                lista.append(i.der)
        return lista
            
    
# ===============================================
#         TABLA SINTACTICA DE PRODUCCION
# ===============================================
class TAS:
    tablaSintactica = {}
    
    def llenarEstaticamente(self):
        self.tablaSintactica['E']  = {}
        self.tablaSintactica['Ep'] = {}
        self.tablaSintactica['T']  = {}
        self.tablaSintactica['Tp'] = {}
        self.tablaSintactica['F']  = {}
        
        self.tablaSintactica['E']['(']   = ['T','Ep']
        self.tablaSintactica['E']['num'] = ['T','Ep']
        self.tablaSintactica['E']['id']  = ['T','Ep']
        
        self.tablaSintactica['Ep']['+'] = ['+','T','Ep']
        self.tablaSintactica['Ep']['-'] = ['-','T','Ep']
        self.tablaSintactica['Ep'][')'] = ['lambda']
        self.tablaSintactica['Ep']['$'] = ['lambda']
        
        self.tablaSintactica['T']['(']   = ['F','Tp']
        self.tablaSintactica['T']['num'] = ['F','Tp']
        self.tablaSintactica['T']['id']  = ['F','Tp']
        
        self.tablaSintactica['Tp']['+'] = ['lambda']
        self.tablaSintactica['Tp']['-'] = ['lambda']
        self.tablaSintactica['Tp']['*'] = ['*','F','Tp']
        self.tablaSintactica['Tp']['/'] = ['/','F','Tp']
        self.tablaSintactica['Tp'][')'] = ['lambda']
        self.tablaSintactica['Tp']['$'] = ['lambda']
        
        self.tablaSintactica['F']['(']   = ['(','E', ')']
        self.tablaSintactica['F']['num'] = ['num']
        self.tablaSintactica['F']['id']  = ['id']
    
    def imprimir(self):
        for x in self.tablaSintactica:
            print (x)
            for y in self.tablaSintactica[x]:
                print (y,':',self.tablaSintactica[x][y])
            print('')
        
        
        


    
def main ():
    g = Gramatica()
    g.cargar("""
            E := T Ep
            Ep := + T Ep
            Ep := - T Ep
            Ep := lambda
            T := F Tp
            Tp := * F Tp | / F Tp | lambda
            F := ( E ) | num | id
           """)
           
    g.imprimir()
    print("=====================")
    print(g.terminales)
    print("=====================")
    print(g.noterminales)
    print("=====================")
    print(g.getProduccion('Tp'))
    print('\n\n\n')
    
# ===============================================
#         TABLA SINTACTICA DE PRODUCCION
# ===============================================
    
    t = TAS()
    t.llenarEstaticamente()
    t.imprimir()
    
    
main()