# Kortezh (tuple)
# Spisok kotoriy nelzya izmenit
# Zapisiyvaetsya v krugliyh skobkah
# roles = ('user', 'manager', 'admin')
# sluzhit dlya zashitiy ot izmeneniy

print('SOREVNOVANIYA')
count = int(input('Enter the count of human:'))
i = count
members = []
while i > 0:
    name = input('who took {} place'.format(i))
    members.append(name)
    i-=1
print(sorted(members))
members.reverse()
result = members[:3]
result = 'Wiiners:{}. Congratulations!'.format(result)
print(result)