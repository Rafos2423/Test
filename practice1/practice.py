import random

agree = 0
not_agree = 0

for i in range(100000):
    a = [0, 0, 1]

    choice = random.randint(0, 2) #выбор игрока
    a.pop(choice) #карта игрока открывается
    a.remove(0) #ведущий открывает карту

    if a[0] == 1: #если последняя карта верная, то игрок походил бы правильно если бы поменял свое решение
        agree += 1
    else: #иначе ему надо было оставить свою карту
        not_agree += 1

print(f'agree: {agree/1000}\nnot agree: {not_agree/1000}')



