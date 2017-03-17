from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable
import pandas as pd
from pandas import Series, DataFrame

url = 'http://www.unpad.ac.id/fakultas/'

result = requests.get(url)
c = result.content

soup = BeautifulSoup(c, 'lxml')

summary = soup.find("section", {'class' : 'main-content'})

faculties = summary.find_all('a')

tabel = PrettyTable(['No.', 'Fakultas'])
no = 1

for faculty in faculties:
	text = faculty.find(text=True)
	tabel.add_row([no, text])
	no += 1

print("\n\tDaftar Fakultas di Unpad")
print(tabel)