friend_name = 'max'
friends = ['Def', 'Kuska', 'Ferdo']
roles = ('admin', 'guest', 'user')
# example
if 'Kuska' in friends:
    print('EST this friend')
# example
if 'm' in friend_name:
    print('est bukva M')

# example cycle while
i = 0
while i < len(friends):
    friending = friends[i]
    print(friending)
    i += 1

# cycle for in
for friend in friends:
    print(friend)

for letter in friend_name:
    print("pishmat - :" + letter)

for role in roles:
    print(role)
