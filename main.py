# Создаем генератор паролей

import random

alph = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM~!@#$%&*()_1234567890'

number = int( input('Какое количество паролей необходимо? '))
lenght = int( input('Какая нужна длина пароля? '))

for x in range( number ):
    password = ''

    for i in range (lenght):
        password+=random.choice( alph )
    print(password)