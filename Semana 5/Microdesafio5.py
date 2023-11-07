#Semana5
def saludar_por_ciudad(): #defino mi funcion que reciba una cadena
    ciudad=input('Escribe tu ciudad: ')
    saludo='¡¡Hola, te damos la bienvenida a {}'.format(ciudad)
    return saludo

print(saludar_por_ciudad())

#otra forma
#def bienvenida_ciudad():
    #nombre_ciudad=input('Escriba el nombre de la ciudad ')
    #saludo=print(f'¡¡Hola, te damos la bienvenida a {nombre_ciudad}!')
    #print(saludo)
    #return saludo
#bienvenida_ciudad()

#errores:
#a la funcion tengo que asignarle una variable
#el print adentro de la funcion
#print no esta hecha para devolverle un valor, esta hecha para imprimir
#print(saludo) me aparece None, piensa que la variable esta vacia

#corregido
#def bienvenida_ciudad(nombre_ciudad):
    #saludo=f'¡¡Hola, te damos la bienvenida a {nombre_ciudad}!'
    #return saludo
#nombre_ciudad=input('Escriba el nombre de la ciudad ')
#print(bienvenida_ciudad(nombre_ciudad))