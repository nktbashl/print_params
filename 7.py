def print_params(a =  1, b = 'строка', c = True):
    print(a, b, c)

values_list = [3, 4, 5]
values_dict = {'a':1, 'b':'строка', 'c':True }
values_list_2 = [1, "two"]

print_params(b = 25, c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
