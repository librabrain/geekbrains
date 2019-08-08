global_var = 1

def my_f():
    # localnaya peremennya inside function
    local_var = 100
    print('Inside of function', local_var)
    # globalnaya peremennya obyavlennya v module
    print('Global function', global_var)
    # global_var = 999 - no etu globalnuyu peremennyu nelzya izmenit

my_f()
print('Global function in module', global_var)