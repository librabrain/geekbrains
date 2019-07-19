number = 0
n = int(input('enter the number:'))

while number <= n:
    # если хотим вывести нечётные числа, используем  !=0
    # в случае с чётными числами, используем ==0
    if number % 2 !=0:
        print(number)
    # number = number + 1 - обычный способ.
    # для упрощённого варианта лучше , следуте писат так:
    number += 1