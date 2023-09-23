def majority2(the_list):
    my_dict = {}
    for el in the_list:
        my_dict[el] = (my_dict[el] + 1 if el in my_dict else 1)
    result = [str(el[0]) for el in filter(lambda x: x[1] == max(my_dict.values()), my_dict.items())]
    return ', '.join(result)


print(majority2([1, 2, 3, 4, 2, 3, 2, 3]))
