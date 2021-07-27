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
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

numero_1 = float(input('Ingresá acá tu primer número:\n'))
numero_2 = float(input('Ingresá acá tu segundo número:\n'))

resta = numero_1 - numero_2
print(resta)

if numero_1 > numero_2:
    print('{} > {}'.format(numero_1, numero_2))
elif numero_1 < numero_2:
    print('{} < {}'.format(numero_1, numero_2))
else:
    print('{} = {}'.format(numero_1, numero_2))