import pandas

my_list = []

for i in range(1, 6):
    with open(f'./csv/{i}.csv') as file:
        data = pandas.read_csv(file)
        if i == 1:
            my_list.append(data["Nr. crt."].to_list())
            my_list.append(data["Județ"].to_list())
        my_list.append(data["Număr de cazuri confirmate(total)"].to_list())

columns = ['NR. CRT', 'Judet', '01.03', '02.03', '03.03', '04.03', '05.03']
pandas.DataFrame(list(zip(*my_list)), columns=columns).to_excel('x.xlsx', index=False)
