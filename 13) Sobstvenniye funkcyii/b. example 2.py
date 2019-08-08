# funkciya
def get_sep(sep, sep_len):
    # return pozvolyaet vipolnyat  vozvroshaemoe znacheniye
    return sep * sep_len

print(get_sep('+', 10))
print(get_sep('*-', 50))

sep = get_sep(')*_*(', 1)
sep2 = get_sep('0_0', 1)
text = 'Hello! You are {}, mmmm {}'.format(sep2, sep)
print(text)

