# len(friend) - длина строки (сколько в ней символов)
# friend.find('a') - ищем символ 'a' в строке
# friend.split() - разбиение строки через пробел
# friend.isdigit() - проверка, что строка состоит только из чисел
# friend.upper() - приводит строку к верхнему регистру
# friend.lower() - приводит строку к нижнему регистру

friends = 'Maxim Leonid'
print(len(friends))

print(friends.find('Leo'), 'результат выведен в индекс')
# метод *.find выводит результат в индексах
# если в методе *.find не удалось найти искомую подстроку, она  возвращает результат "-1". В данном случае
# пример выше: ищем "12Leo" - которой не существует, вместо "Leo" - которое есть в строке "Maxim Leonid"


print('здесь мы получаем список', friends.split())

# friends = 'Maxim;Leonid'
# print(friends.split(';'))

number = '123'
print(number.isdigit())

print(friends.upper())
print(friends.lower())



