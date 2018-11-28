
#!Python3
import requests
from bs4 import BeautifulSoup
import csv

'''website that user wants to scrape is provided here'''
link = 'https://www.newegg.com/Gaming-Monitors/SubCategory/ID-3743?Tid=898493&cm_sp=CAT_Monitors-_-VisNav_1-_-Gaming-Monitors_2&Order=RATING&PageSize=96'
source = requests.get(link).text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['description', 'price'])

for contents in soup.find_all('div' ,class_='item-container '):
#Item Description
    description = contents.find("a", class_ = "item-title").text
    print(description)

    price = "$" + contents.find("li", class_ ="price-current").text
    print(price)


    print()

    csv_writer.writerow([description, price])

csv_file.close()








#print(first_mon)


#brand = contents.a

#brand = contents.find('div', class_='item-branding'
#description =

#price =s
