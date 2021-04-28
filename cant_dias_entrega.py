import random

def cant_dias_entrega(rango):
    
    if rango < 1:
	    return 0
    elif rango < 3 :
        return 1
    elif rango < 4:
        return 2
    elif rango < 5:
        return 3
    else:
        return cant_dias_entrega(rango-1)+cant_dias_entrega(rango-2)

def determina_rango(kil):
    return int(kil/100)

def entrega_cant_dias_entrega(kilometros):
    rango = int(kilometros/100)
    return cant_dias_entrega(rango)

#Main
kilometros = random.randrange(0,2000)
print("kilometros: ",kilometros)
print("dias de entrega: ", entrega_cant_dias_entrega(kilometros))