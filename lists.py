from lib2to3.pgen2.token import COLON
import numbers
from turtle import color


demo_list=[1,'hi', 3.14,True,[1, 2, 3]]
colors = ['red','green', 'blue','orange']

#como pasar cuatro argumentos en python
#pasamos argumentos  mediante tuplas
#y al momento de imprimir mostrara la tabla con los números.

numbers_list = list((1, 2, 3, 4))
# print(numbers_list)
# para crear una lista basada en un rango
# en python existe una función llamada range.

# r_num =list (range(1, 999))
# print(r_num)
# print(len(colors))
# esta liea de codigo permite obtner la
# pocición de un dato especifico ||.
# print(colors[0])
# esta codigo nos permite saber si  dicho objeto esta dentro de 
# la variable.
# print('black' in colors)
# Este frsgmento de codigo Para alterar los datos de una lista
# modificar o actualizarlos


# print(colors)
# colors[3] = 'aguamarina'
# print(colors)

# Metodo append para agregar elementos


colors.extend(['violet','yelot'])
colors.extend(['green','black'])
colors.extend(['red','skip'])
print(colors)


