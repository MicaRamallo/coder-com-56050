#Clase 5
#Ejercicio calculo de media
#def promedio(args): #args guarda todos los elementos y se convierte en una tupla
#    return sum(args) / len(args) #sum suma elementos adentro de una lista/tupla
    #si pongo *args, esto sera ([1,2,3],) osea una lista adentro de una tupla
    #sum no puede sumar esos valores porque solo reconoce que hay una lista
    #y no valores

#dificil la utilidad de args 

# lista_numeros=[]
# while True:
#     numero=input('Ingrese un valor: ')
#     if numero == 'exit': #si la palabra ingresada es exit, termina el programa 
#         break
#     numero=int(numero)
#     lista_numeros.append(numero)

# print(promedio(lista_numeros))

# def promedio(*args): #con el *, recibe cantidad de numeros indeterminados
#     #si no pongo *, solo le puedo pasar 1 argumento
#     print(args)
#     return sum(args) / len(args)

# resultado=promedio(8,9,14,64)
# print(resultado)

#Ejercicio multiplo
# def es_multiplo (a,b): #recibe dos numeros
#   #resultado = "" #string vacio, no hace falta
#   if a % b == 0: #si a dividido b da resto=0
#       resultado = f"El nro {a} es multiplo de {b}"
#   elif b % a == 0:
#       resultado = f"El nro {b} es multiplo de {a}"
#   else:
#       resultado = f"¡El nro {a} no es multiplo de {b} ni vice versa!"
#   return resultado

# print(es_multiplo(5,4))
# print(es_multiplo(10,2))
# print(es_multiplo(10,20))

#Ejemplo año bisiesto
def anio_bisiesto(anio): #lo pasamos por medio de un argumento
    #anio = input('Ingrese el año: ') #vamos a tener guardado un str (string)
    if type(anio) != int: #si el tipo de anio es distinto de un numero int
        print('El dato ingresado no es valido')
        return False #si encuentra esto, termina la funcion (no se ejecuta +)

    if anio % 400 == 0 or anio %4 == 0 and anio % 100 !=0:
            print(f"El año {anio} es bisiesto")
    else:
         print(f'El año {anio} no es bisiesto')

#no les tengo que poner print porque despues de ejecutar el return del primer
#if, si les pongo print va a devolver un return vacio y aparecera None
anio_bisiesto(2012)
anio_bisiesto(2010)
anio_bisiesto(2000)
anio_bisiesto(1900)


#anio_bisiesto() como hago si quiero ponerlo asi?