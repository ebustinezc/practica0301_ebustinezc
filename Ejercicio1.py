# Escribir dos funciones, una función que reciba un número entero positivo n y calcule el número de fibonacci 
# asociado a ese número de manera recursiva y otra función que haga la misma operación pero con bucles.
# Con ambas funciones, calcular y comparar el tiempo de ejecución para n = (1, 10, 20, 30 y 40) por fuerza bruta.

import datetime

def Fibonacci_bucles(n):
    a, b = 0, 1
    for i in range (n):
        a, b = b, a + b
   
    return(a)

st = datetime.datetime.now()    
print(Fibonacci_bucles(6))
et = datetime.datetime.now()
print(et-st)

def Fibonacci_recursiva(n):
    if n <= 1:
        return n
    else:
        return Fibonacci_recursiva(n-1) + Fibonacci_recursiva(n-2)

st = datetime.datetime.now()
print(Fibonacci_recursiva(40))
et = datetime.datetime.now()
print(et-st)