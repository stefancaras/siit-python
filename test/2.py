import re


def majority(the_list):
    new_list = []
    for item in set(the_list):
        new_list.append(re.findall(str(item), str(the_list)))
    new_list = sorted(new_list, key=lambda x: len(x), reverse=True)
    new_list = list(filter(lambda x: len(x) == len(new_list[0]), new_list))
    new_list = [el[0] for el in new_list]
    return ', '.join(new_list)


def majority2(the_list):
    my_dict = {}
    for el in the_list:
        my_dict[el] = (my_dict[el] + 1 if el in my_dict else 1)
    result = [str(el[0]) for el in list(filter(lambda x: x[1] == max(my_dict.values()), my_dict.items()))]
    return ', '.join(result)


print(majority([3, 2, 2, 33]))
