# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

asignaturas = []
notas = []
materias_mas_nota = {}
print("Puedes elegir un máximo de cinco (5) asignaturas:")

def agregar_asignatura():
    
    for i in range(1, 5 + 1):
        
        asignatura_elegida = input(f"Escribe la asignatura número {i} para agregar a la lista:\n")
        asignaturas.append(asignatura_elegida)
        
    return asignaturas


def preguntar_notas():
    
    for materia in asignaturas:
        nota = float(input(f"¿Qué notas sacaste en {materia}?\n"))
        notas.append(nota)
        
    return notas

def mostrar_info():
    materias_mas_nota = dict(zip(asignaturas, notas))


agregar_asignatura()

preguntar_notas()

#materias_mas_nota = dict(zip(asignaturas, notas)) ---> de esta forma creamos un diccionario a partir de dos listas.

mostrar_info()
