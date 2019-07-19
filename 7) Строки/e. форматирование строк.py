# 1. конкатенация (не рекомендуется) - склеивание строки
# 2. % - это оператор
# 3. format (рекомендуется)

name = 'Leo'
age = 24

# 1. конкатенация
hello_str = 'Hi, ' + name + ' you ' + str(age) + ' old'
print(hello_str)

# 2. % - это оператор
hello_str = 'hi, %s you %d old ' % (name, age)
print(hello_str)

# 3. format
hello_str = 'hi, {} you {} old'.format(name, age)
print(hello_str)

