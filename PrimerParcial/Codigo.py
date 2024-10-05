# 1- Crear una lista con enteros y flotantes e imprimirla:

lista = [1, 2.5, 3, 4.75, 5]
print(lista)

# 2- Crear una tupla con algunos Strings e imprimirla:

tupla = ('manzana', 'banana', 'cereza')
print(tupla)

# 3- Crear un diccionario con claves de la tupla y valores de la lista e imprimirlo:

diccionario = {
    'manzana': 1,
    'banana': 2.5,
    'cereza': 3
}
print(diccionario)

# 4- Ecuacion que da como resultado 150.75 utilizando operaciones matematicas: 

resultado = (10 * 15) / (2 + 1) + (5 ** 2) - (25) + 100.75
print(resultado)  # Esto debe imprimir 150.75

# 5- Añadir un numero al listado creado en el punto 1:

lista.append(6.25)
print(lista)

# 6- Convertir la lista en un set e imprimirlo:

conjunto = set(lista)
print(conjunto)

# 7- Acceder e imprimir "hola" desde el siguiente diccionario:

d = {'c1': [4, 1, {'c2': ["es otro listado", {'0': [3, 1, ['hola']]}]}]}
print(d['c1'][2]['c2'][1]['0'][2][0])

# 8- Evaluar la expresión:

d = {'c1': [4, 1, {'c2': ["es otro listado", {'0': [3, 1, ['hola']]}]}]}
resultado = d['c1'][0] > d['c1'][2]['c2'][1]['0'][0]
print(resultado)  # Resultado: True
