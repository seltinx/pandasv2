import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Zadanie 1


a = pd.ExcelFile('imiona.xlsx')
b = pd.read_excel(a, header=0)
print(b)
#
# c = b.groupby(['Rok'])['Liczba'].sum()
# print(c)
# c.plot()
# plt.show()
# Nie mam pojęcia jak zrobić żeby nie było połowy roku

#Zadanie 2

# a = pd.ExcelFile('imiona.xlsx')
# b = pd.read_excel(a, header=0)
# print(b)
#
#
# grupak = b[(b['Plec'] == 'K')]['Liczba'].sum()
# grupam = b[(b['Plec'] == 'M')]['Liczba'].sum()
# title = ['Kobiety', 'Mezczyzni']
# grupa = [grupak, grupam]
# plt.bar(title, grupa, color='blue')
# plt.ylabel('Ilosc narodzin')
# plt.show()

#Zadanie 3

# a = pd.ExcelFile('imiona.xlsx')
# b = pd.read_excel(a, header=0)
# print(b)
#
#
# zad = b[(b['Rok'] >= 2012)].groupby(['Plec']).agg({'Liczba': {'sum'}})
# title = ['Kobieta', 'Mezczyzna']
# wykres = zad.plot.pie(figsize=(5, 5), autopct='%.2f %%', subplots=True, labels=title, startangle=90, shadow=True, wedgeprops={'edgecolor': 'white'}, colors=['y', 'r'])
# plt.title('Liczba urodzen w ciagu 5 lat')
# plt.show()

#Zadanie 4

a = pd.read_csv('zamowienia.csv',header=0, sep=';', decimal='.')
b = a.groupby(['Sprzedawca'])[['idZamowienia']].count().plot(kind='bar', color='pink', legend=None, title='Ilosc zamowien zlozonych przez sprzedawcow')
plt.ylabel('Ilosc zlozonych zamowien')
plt.show()