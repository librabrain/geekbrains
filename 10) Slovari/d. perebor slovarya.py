# Variantiy perebora slovarya
# po klucham
# po znacheniyu
# po parametram kluch, znacheniye

friend = {
    'name': 'Max',
    'age': 23,
    'has_car': True
}

# po klucham
print('---PEREBOR po klucham ')
for key in friend.keys():
    print(key)
    print(friend[key])

# po klucham 2
print('---PEREBOR po klucham 2')
for key in friend:
    print(key)
    print(friend[key])

# po znacheniyam
print('---PEREBOR po znacheniyam')
for val in friend.values():
    print(val)


# perebrat' pariy kluch znacheniya
print('---perebrat paryi kluch znacheniya')
for item in friend.items():
    print(item)

print('---')
for key, val in friend.items():
    print(key)
    print(val)