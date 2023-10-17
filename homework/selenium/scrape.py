from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv

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
