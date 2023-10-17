from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import pandas

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
for i in range(1, 6):
    driver.get(f'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{i}-martie-ora-13-00{["","-2","-2","-2","-3",""][i]}/')
    table = driver.find_element(by=By.TAG_NAME, value='table')
    with open(f'{i}.csv', 'w', newline='') as csvfile:
        wr = csv.writer(csvfile)
        for row in table.find_elements(by=By.TAG_NAME, value='tr'):
            my_list = []
            for d in row.find_elements(by=By.TAG_NAME, value='td'):
                my_list.append(d.text)
                if d.text == ' TOTAL':
                    my_list.append('')
            wr.writerow(my_list)

my_list = []

for i in range(1, 6):
    with open(f'{i}.csv') as file:
        data = pandas.read_csv(file)
        if i == 1:
            my_list.append(data["Nr. crt."].to_list())
            my_list.append(data["Județ"].to_list())
        my_list.append(data["Număr de cazuri confirmate(total)"].to_list())

columns = ['NR. CRT', 'Judet', '01.03', '02.03', '03.03', '04.03', '05.03']
pandas.DataFrame(list(zip(*my_list)), columns=columns).to_excel('x.xlsx', index=False)
