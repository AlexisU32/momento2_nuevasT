# Hacer una actividad que pida al usuario escribir una cantidad X de nombres de personas 
# (puede hacerlo con el ciclo que considere). Despues el sistema debera demostrar cuales son los nombres 
# que empiezan con la letra "C" sea minuscula o mayuscula.

nombre = "no"
lista = []
lista2 = []

while nombre != 'si':
    
    nombre = raw_input('Escribe un nombre y si quiere salir escriba (si) ')
    
    if nombre != 'si':
        lista.append(nombre)
        
        letra = nombre[0]
        
        if letra == "c" or letra == "C":
            lista2.append(nombre)
            
            
    
print(lista)
print()
print(lista2)




