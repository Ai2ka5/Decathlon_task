from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://en.wikipedia.org/wiki/Decathlon').text
soup = BeautifulSoup(source, 'html.parser')

tables = soup.find_all(class_='wikitable')
men = tables[6].text
women = tables[7].text

with open("Decathlon - Wikipedia.csv", "w", encoding="UTF-8") as failas:
    csv_writer = csv.writer(failas)
    csv_writer.writerow([men, women])
