simbolos={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

repeticionesValidas= ('MMM','MM','M','D','C','CC','CCC','L','X','XX','XXX','V','I','II','III')


def num_veces(cadena):    
    if x not in repeticionesValidas:
        return False
    return True

def combinaciones(cadena):#XXXVV  XD
    contador=0
    indice=0
    if x[0] in repeticionesValidas:
        contador= contador.append()
        if x[indice+1] in repeticionesValidas:
            contador= contador.append()
            raise ValueError(f"simbolo {romano} excedido")
            


x=input("introduce romano:   ")
while not num_veces(repeticionesValidas):
    print(f"simbolo {x} ha excedido el maximo permitido")
    x=input("introduce romano correcto:   ")
    


        if x[indice+1] in repeticionesValidas:
            contador= contador.append()
