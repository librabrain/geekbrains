# вложение if - то есть, внутри if-elif-else можеть быть другой if

age = int(input('введите свой возраст:'))

if age < 18:
    print('Доступ запрещён')
elif age == 18:
    print('Вам 18','Что с вами делать?')
elif age > 18 and age < 25:
    print('Отдельная категория пользоватлеей')
else:
    print('доступ разрешён')

print('end')