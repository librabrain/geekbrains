number = 0
n = int(input('enter the number:'))

while number <= n:
    if number % 2 ==0:
        number += 1
        continue
    print(number)