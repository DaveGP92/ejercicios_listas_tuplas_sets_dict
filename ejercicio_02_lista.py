# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

numeros = []

def invertir_lista(lista):
    for num in range(1, 10 + 1):
        lista.append(num)
    
    lista.reverse()
    return lista

num_reves = invertir_lista(numeros)

print(num_reves)