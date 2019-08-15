# цифра 1988 преобразовалась в строку за счёт ковычек! была int, стала str
birthday_year = '1988'
print(type(birthday_year))

period = 20
print(type(period))

# преобразовали переменную "birthday_year" в цифру
age = int(birthday_year) + period
print(age)

# складывание двух строк является - конкатенацией. пример, но сначала преобразовываем число "period" в строку
some_str = birthday_year + str(period)
print(some_str)
