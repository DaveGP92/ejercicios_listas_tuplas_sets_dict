# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

from string import ascii_lowercase

abc = list(ascii_lowercase)
nueva_lista = []



for i in range(0, len(abc)):
        if (i + 1) % 3 != 0:
            nueva_lista.append(abc[i])

        else:
            continue



print(f"nueva lista {nueva_lista}")
            
    








        
        


