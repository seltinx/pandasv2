import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Zadanie 1


# a = pd.ExcelFile('imiona.xlsx')
# b = pd.read_excel(a, header=0)
# print(b)
#
# c = b.groupby(['Rok'])['Liczba'].sum()
# print(c)
# c.plot()
# plt.show()

#Zadanie 2

a = pd.ExcelFile('imiona.xlsx')
b = pd.read_excel(a, header=0)
print(b)
# df = pd.DataFrame(a)
# print(df)

grupa = b.groupby(['Plec']).agg({'Plec':['sum']})
print(grupa)
wykres = grupa.plot.bar()
wykres.set_xlabel('Plec')
wykres.set_ylabel('Ilosc')
wykres.legend()
plt.title("Urodzenie chlopcy i dziewczeta")
plt.xticks(rotation=0)
plt.show()
