
# Pide numeros y metelos en una lista, cuando el usuario meta un 0 
# ya dejaremos de insertar. Por ultimo, muestra los numeros ordenados de menor a mayor.

numero = 1
lista = [] 

while numero != 0:
    
    numero = input('Ingrese un numero ')
    
    if numero != 0:
        lista.append(numero)
        
    
print(lista)
print()
lista.sort()
print(lista)
    
