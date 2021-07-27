# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

# Indicaciones para el usuario
print("Ingrese su temperatura según su número")

# Temperaturas
temperatura_1 = int(input('Temperatura 1\n'))
temperatura_2 = int(input('Temperatura 2\n'))
temperatura_3 = int(input('Temperatura 3\n'))

# Ordenamiento de la mayor temperatura

if temperatura_1 > temperatura_2 and temperatura_3:
    print("La primer temperatura ingresada es la mayor")
elif temperatura_2 > temperatura_3 and temperatura_1:
    print("La segunda temperatura ingresada es la mayor")
elif temperatura_3 > temperatura_1 and temperatura_2:
    print("La tercer temperatura es la mayor de todas")

# Ordenamiento de la menor temperatura

if temperatura_1 < temperatura_2 and temperatura_3:
    print("La primer temperatura ingresada es la menor")
elif temperatura_2 < temperatura_3 and temperatura_1:
    print("La segunda temperatura ingresada es la menor")
elif temperatura_3 < temperatura_1 and temperatura_2:
    print("La tercer temperatura es la menor de todas")

# Promedio - Temperaturas

temp_avg = (temperatura_1 + temperatura_2 + temperatura_3) / 3
print(temp_avg)

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
