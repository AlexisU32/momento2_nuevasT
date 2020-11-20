
from collections import Counter

# Escribir una funcion que cuente la cantidad de apariciones 
# de cada caracter en una cadena de texto, y los devuelva en un diccionario.


def apariciones(nameText):
    contador = Counter(nameText)
    
    return contador


txt = 'Hola mundo'

print(apariciones(txt))