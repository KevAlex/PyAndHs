class Nodo():
    def __init__(self,valor,izq=None,der=None):
        self.valor = valor
        self.izq = izq
        self.der = der


a1 = Nodo (25, Nodo (10), Nodo (50, Nodo (40)))

a2 = Nodo(15,Nodo(6, Nodo(4, Nodo(2), Nodo(3))),Nodo(50,Nodo(25),Nodo(104)))

a3 = Nodo (12, Nodo(8,Nodo(4),Nodo(10,Nodo(9),Nodo(11))), Nodo(25, Nodo(17), Nodo(30, Nodo(28), Nodo(50) ) )   )

#print (a2.der.izq.valor)


class Nario():
    def __init__(self,valor,nodos=[]):
        self.valor = valor
        self.nodos = nodos

an = Nario (2,[ Nario(4,[Nario(12), Nario(24), Nario(40)]), Nario(8,[Nario(16), Nario(32)]), Nario(5,[Nario(25), Nario(50)]) ] )
# problema es como entrar al otro nivel de la lista 
def buscarD(num,arbolN):
    if arbolN == None:
        return False
    else:
        buscarN(num,arbolN)
        arbolN.nodos.pop(0) or buscarD(num,arbolN)

        
def buscarN(num,arbolN):
    if arbolN.nodos == None:
        if num == arbolN.valor:
            return True
        else:
            False
    else:
        if arbolN.valor == num:
            return True
        else:
            buscarN(num,arbolN[0].valor)
            arbolN.nodos.pop(0) or buscarN2(num,arbolN )

            

#print ("a", an.nodos[0].valor,an.nodos.pop(0) )
        

    
def contarNodo(arbol):
    if arbol == None:
        return 0
    return 1 + contarNodo(arbol.der) + contarNodo(arbol.izq)

print ("nodos",contarNodo(a3))


def insertar(a,arbol):
    if arbol == None:
        arbol = Nodo(a)
    
    if  arbol.izq == None and arbol.der == None:
        if a<= arbol.valor:
            arbol.izq = Nodo(a)
        else:
            arbol.der= Nodo(a)
    else:
        if a<= arbol.valor:
            arbol = Nodo(arbol.valor,insertar(a,arbol.izq) )
        else:
            arbol= Nodo(arbol.valor, arbol.izq.valor,insertar(a,arbol.der))

print ("inserto ", insertar(51,a3))

print ("nodos",contarNodo(a3))

def contarHoja(arbol):
    if arbol == None:
        return 0
    elif arbol.izq == None and arbol.der == None:
        return 1
    return contarHoja(arbol.izq) + contarHoja(arbol.der)
    
#print ("hojas",contarHoja(a3))

def contarElementos(arbol):
    if arbol == None:
        return 0
    elif arbol.izq == None and arbol.der == None:
        return 1
    return 1 + contarElementos(arbol.izq) + contarElementos(arbol.der)
#print ("a",contarElementos(a3))
#print ("de ",a3.izq.izq.der.valor)


def buscar_ok(arbol, valor):
    if arbol == None:
        return False
    if arbol.valor == valor:
        return True
    if valor < arbol.valor:
        return buscar_ok(arbol.izq, valor)
    return buscar_ok(arbol.der, valor)

def buscar(ele,arbol):
    #print(arbol.valor, arbol.izq.valor, arbol.der.valor,ele)
    if arbol.izq == None and arbol.der == None:
       # print "error"
        if arbol.valor == ele:
            return True
        else:
            return False
    if (ele == arbol.valor):
        return True
    else:
        if ele < arbol.valor:
            #print ("e",arbol.izq.valor)
            return buscar(ele, arbol.izq)
            
        else:
            return buscar(ele,arbol.der)
           # print "ho"
            
print("corregir",buscar(4,a3))
            
#print("corregir",buscar(4,a3))


def in_orden(arbol):
    if arbol == None:
        return []
    return in_orden(arbol.izq) + [arbol.valor] + in_orden(arbol.der)


def postOrden(arbol):
    if arbol == None:
        return []
    return postOrden(arbol.izq) + postOrden(arbol.der) + [arbol.valor]
    
def preOrden(arbol):
    if arbol == None:
        return []
    return [arbol.valor] + preOrden(arbol.izq) + preOrden(arbol.der)

##print ("En Inorden ",in_orden(a3))
##print ("En PosOrden",postOrden(a3))
##print ("En preOrden" ,preOrden(a3))
