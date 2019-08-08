# The FIRST example
def my_f(my_var):
    my_var = 999
    print('Inside of function', my_var)

a = 0
my_f(a)
print('Outside of function', a)



# The SECOND example
def some_f():
    a = 9
    print('Inside of function', a)

a = 3
some_f()
print('Outside of function', a)