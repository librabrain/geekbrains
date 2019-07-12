# and - и (ИСТИНА когда всё ИСТИНА иначе ЛОЖЬ)
# or - или (ЛОЖЬ когда ЛОЖЬ иначе ИСТИНА)
# not - нет (ИСТИНА когда ЛОЖЬ, ЛОЖЬ когда ИСТИНА)

ale = 71
age = int(input('Cколько Вам лет?:'))

print('U vas yubiley', age % 5 == 0)

#  not and or
print('Ne yubiley', age % 5 != 0)
print('Ne yubiley', not age % 5 == 0)

# and
print('U vas ubiley i vash vozrast menshe sredney prodolzhitelnosti zhizni', age % 5 == 0 and age < ale)

# or
print('U vas ubiley ili vash vozrast menshe sredney prodolzhitelnosti zhizni', age % 5 == 0 or age < ale)

# Приоритет в логических выражениях
print((1 > 2 and (0 < 5 or 0 < 2)) and 0 == 0)