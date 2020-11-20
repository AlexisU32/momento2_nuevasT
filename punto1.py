
# Escribir una funcion que reciba una cadena y devuelva un diccionario con la cantidad 
# de apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Que lindo dia que hace hoy" 
# debe devolver: 'que': 2, 'lindo': 1, 'dia': 1, 'hace': 1, 'hoy': 1


def apariciones(newText):
    diccText = {}
    
    newText = newText.lower()
    palabras = newText.split(" ")
    
    for palabra in palabras:
        if palabra in diccText:
            diccText[palabra] += 1
        else:
            diccText[palabra] = 1    
    
    return diccText        

cadena = 'Que lindo dia que hace hoy'
resultado = apariciones(cadena)

print(resultado)            