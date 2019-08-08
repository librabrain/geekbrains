# args - peredacha lyubogo kolichestva po poryadku
# kwargs - peredacha lyubogo kolichestva po imeni


# args
print('******************************************************args')
def greeting (say, *args):
    print(say, args)

greeting('hello', 'Denis')
print(type(greeting('teper eto - ', 'Kortezh')))
greeting('hello', 'Denis', 'Pot')
greeting('hello', 'Denis', 'Ron', 'Hok')


# kwargs
print('*****************************************************kwargs')
def get_person(**kwargs):
    for k, v, in kwargs.items():
        print(k, v)

print('teper eto - Slovar')

get_person(name = 'Leo', age = 29, has_car = True)
