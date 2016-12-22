
# coding: utf-8

# In[8]:

# Ejercicio 1.

lista_num = [0, 1, 1, 1, 3, 4, 3, 2, 1, 3, 21, 1, 1, 1, 1, 23, 1, 1, 1, 1, 23, 4, 4, 6, 7]

numero = input("Introduzca un número: ")

# El contador se iniciliza en 0. Con el bucle, se recorren los elementos de la lista con números y, cada vez que 
# aparezca dicho número, el contador suma 1. 

contador_numero = 0

for item in lista_num :
    if item == numero :
        contador_numero += 1

# Finalmente se imprime el contador para saber el número de veces que aparece un elemento determinado en la lista.         

print "El número" , numero , "aparece" , contador_numero , "veces en la lista."



# In[75]:

# Ejercicio 2.

Producto = ['arroz', 'harina', 'leche', 'garbanzos']

Cantidad = [4, 5, 3, 65]

Precio = [10, 15, 20, 21]

# Creamos un diccionario vacío en el que se irán incluyendo las claves y los valores gracias al bucle for posterior.

dicc = {}

# Con este bucle se recorren los elementos de las tres listas existentes y se van incorporando al diccionario, 
# especificando que el elemento de 'Producto' es la clave y la multiplicación de los elementos de 'Cantidad' y 
# 'Precio' son el valor. Podría valer para listas de cualquier longitud porque utilizamos las funciones range y len.

for i in range(len(Producto)) :
    dicc[Producto[i]] = (Cantidad[i]*Precio[i])
    
print dicc



# In[74]:

# Ejercicio 3.

import re

fecha = raw_input ("Introduzca una fecha con el formato indicado: ")


# Definimos una expresión regular que reconozca el rango de números 1-31 (día), los meses del año y los años que tengan
# 2 y 0 como primeros dígitos y después cualquier número entre 0 y 9 repetido dos veces. 


exp_reg = re.compile('([1-31])( de )(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)( de )(20[0-9]{2})', re.IGNORECASE)


# Con este condicional se comprueba que la fecha introducida tenga el formato correcto.

if exp_reg.search(fecha) :
    print "El formato es correcto"
else :
    print "El formato es incorrecto"


# Se imprime el mensaje pedido en el enunciado recurriendo a los grupos del MatchObject que se genera. 
    
    
print "Estamos en", exp_reg.search(fecha).group(3) , exp_reg.search(fecha).group(4) , exp_reg.search(fecha).group(5) , "y es el día" , exp_reg.search(fecha).group(1) , "."



# In[82]:

# Ejercicio 4.

def potencia (exponente) :
    base = 2
    if exponente == 0 :
        return 1
    else : 
        return base ** exponente
  
        
potencia(3)

