# len(friends) - dlina spiska (skolko v nem elementov)
# friends.append('Ron') - dobavleniey new elementa
# friends.pop() - udalyaem posledniy element i vosvrashaem ego
# friends.clear() - ochishaem ves spisok
# friends.remove('Ron') - udaleniey ob'ekta iz spiska
# del friends[0] - udaleniye elementa po indeksu

friends = ['Max', 'Leo', 'Kate']

print(friends)
print(len(friends))

friends.append('Ron')
print(friends)
print(len(friends))

print(friends.pop())
print(friends)
print(len(friends))

friends.clear()
print(friends)

friends = ['Max', 'Leo', 'Kate']

friends.remove('Kate')

print(friends)

del friends[0]
print(friends)