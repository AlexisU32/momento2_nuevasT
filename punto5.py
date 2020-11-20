
# Realice una FUNCION en Python que calcule el indice de masa corporal de una persona 
# y diga el estado en que se encuentre. Debe recibir los parametros necesarios.

def imc(peso, altura):
    form = round(peso / pow(altura,2), 2)
    
    if form <= 18.5:
        clasificacion = "Peso insuficiente"
    elif form > 18.5 and form <= 24.9: 
        clasificacion = "Normopeso"
    elif form >= 25 and form <= 26.9:
        clasificacion = "Sobrepeso grado I" 
    elif form >= 27 and form <= 29.9:
        clasificacion = "Sobrepeso grado II (preobesidad)"
    elif form >= 30 and form <= 34.9:
        clasificacion = "Obesidad de tipo I"   
    elif form >= 35 and form <= 39.9:
        clasificacion = "Obesidad de tipo II"  
    elif form >= 40 and form <= 49.9:
        clasificacion = "Obesidad de tipo III (morbida)"   
    elif form >= 50:
        clasificacion = "Obesidad de tipo IV (extrema)"   
        
 
    return clasificacion
    

print('')
pes = float(input('Ingrese su peso '))
alt = float(input('Ingrese su altura '))

print('')

result = imc(pes,alt)
print('Usted se encuentra en el grupo: ' + str(result))
print('')
print('')