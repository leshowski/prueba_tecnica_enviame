def fibonacci(n):
    
    if (n>1):
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        if (n==1):
            return 1
        else:
            if (n==0):
                return 0
            else:
                return -1

def cantidad_divisores(n):
    contador = 0
	
    for i in range(1,n+1):
        if(n%i == 0):
            contador = contador+1

    return contador

i = 1
#Se deja en 100 ya que el cálculo para 1000 toma mucho tiempo
n_divisores_esperado = 101

while  n_divisores_esperado > 100:
    n_divisores_esperado = int(input("Ingrese la cantidad de divisores: ")) 

while True:
    secuencia = (fibonacci(i))
    cant_divisores = cantidad_divisores(secuencia) 

    if cant_divisores >= n_divisores_esperado:
	    break
    else:
	    i = i+1

print("Encontrado: "+format(secuencia))