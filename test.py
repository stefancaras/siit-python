# 1
# x = {'a':1,'b':2,'c':3,'a':4,'d':5}
# print(x['a'])

# 2
# x = list(range(1,20))
# x = [i for i in x if i % 2 == 0]
# print(x)

# 3
# __str__ = 1
# _a = 1
# __a = 1

# 4
# def a(d):
#     d[4] = 'd'
#     return d
#
#
# x = {1: 'a', 2: 'b', 3: 'c'}
# y = a(x)
# print(x is y)

# 5
# def functie1(lista_cuvinte):
#     lista = []
#     for n in lista_cuvinte:
#         lista.append((len(n), n))
#     lista.sort()
#     return lista[-1][0], lista[-1][1]
#
#
# rezultat = functie1(['pip', 'Exercitiu', 'Python'])
# print(rezultat[1], rezultat[0])


# 6
# class Clasa:
#     def __init__(self):
#         self.s = ''
#
#     def metoda1(self):
#         self.s = 'test'
#
#     def metoda2(self):
#         print(self.s.upper())
#
#
# strObj = Clasa()
# strObj.metoda1()
# strObj.metoda2()


# 7
# def functie(lista):
#     item = 1
#     for x, y in enumerate(lista):
#         item *= x
#         return lista[y + 1]
#
#
# lista = [1, 2, 3]
# print(functie(lista))

# 8
# my_tuple = (1, 10, 100)
# t2 = my_tuple * 3
# print(len(t2))


# 9
# def functie1():
#     print('Variabila este definita?', var)
#
#
# var = 30
# functie1()
# print(var)

# 10
# x = 10
# while x > 1:
#     x -= 1
#     continue
# print(x)

# 11
# my_var = ['a', 'b', {'x': 1, 'z': {'key': 30}, 'w': 2}, 10]
# print(my_var[2]['z']['key'])

# 12
# x = ['ab', 'cd', 'ed']
# for i in x:
#     i.title()
# print(x)

# 13
# i = 2
# while True:
#     if i // 3:
#         break
#     print(i)
#     i += 3

# 14
# students = [{
#     'name': 'A',
#     'grade': 5.0
# }, {
#     'name': 'B',
#     'grade': 3.5
# }, {
#     'name': 'C',
#     'grade': 8.75
# }, {
#     'name': 'D',
#     'grade': 6.25
# }]
# students = list(filter(lambda x: x['grade'] >= 5.0, students))
# students = [x['name'] for x in sorted(students, key=lambda x: x['grade'], reverse=True)]
# print(students)

# 15
# try:
#     i = int('Hello!')
# except Exception as e:
#     print(e)

# 16
# lista = [10 ** ex for ex in range(6)]
# print(lista)

# 17
# lista1 = list(set([1, 3, 2, 3, 4, 5, 6]))
# del lista1[1:5]
# print(*lista1)

# 18
# test_dict = {'element1': 1, 'element2': 3, 'element3': 2}
# res = list(test_dict.keys()) + list(test_dict.values())
# print(str(res))

# 19
# cuvant = "cu'va\\'nt"
# print(cuvant[::-1])

# 20 identic cu # 7

# 21
# def functie():
#     l = list()
#     for i in range(1, 3):
#         l.append(i ** 2)
#     print(l)
#
#
# functie()

# 22 identic cu # 10

# 23
# print(set(list("pythonysta")))

# 24
# def functie1(n):
#     if n % 2 == 0:
#         print(True)
#
#
# print(functie1(2))

# 25
# class Clasa:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 2
#
#
# obiect = Clasa(1)
# print(obiect.a)

# 26
# class Clasa:
#     def __init__(self, nume, prenume):
#         self.nume = nume
#         self.prenume = prenume
#
#     def __str__(self):
#         return f'{self.nume} - {self.prenume}'
#
#
# student = Clasa('Ion', 'Popescu')
# print(student)

# 27
# class SuperClasa:
#     def __init__(self, name):
#         self.nume = name
#
#     def __str__(self):
#         return 'Numele meu este ' + self.nume + '.'
#
#
# class SubClasa(SuperClasa):
#     def __init__(self, name):
#         SuperClasa.__init__(self, name)
#
#
# obj = SubClasa('Alexandra')
# print(obj)

# 28
# class SuperClasa:
#     supVar = 1
#
#
# class SubClasa(SuperClasa):
#     subVar = 2
#
#
# obj = SubClasa()
# print(obj.supVar)

# 29
# class SuperClasa:
#     def __init__(self):
#         self.supVar = 11
#
#
# class SubClasa(SuperClasa):
#     def __init__(self):
#         self.supVar = 12
#         super().__init__()
#
#
# obj = SubClasa()
# print(obj.subVar)

# 30
# class Joc:
#     def __init__(self):
#         self.name = 'john'
#
#
# class Jucator(Joc):
#     def __init__(self):
#         self.name = 'ss'
#         super().__init__()
#
#
# obj = Jucator()
# print(obj.name)
