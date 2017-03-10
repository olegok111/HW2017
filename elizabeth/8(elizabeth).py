# -*- coding: utf-8 -*-
import elizabeth, openpyxl

wb = openpyxl.load_workbook(filename='1.xlsx')
sheet = wb['List1']
sheet['A1'] = 'Имя'
sheet['B1'] = 'Фамилия'
sheet['C1'] = 'Пол'
sheet['D1'] = 'Возраст'
sheet['E1'] = 'Адрес'
sheet['F1'] = 'Профессия'
sheet['G1'] = 'E-mail'
sheet['H1'] = 'Телефон'
for i in range(2, 1001):
    human = elizabeth.Personal()
    sheet.cell(row=i, column=1).value = human.name()
    sheet.cell(row=i, column=2).value = human.surname()
    sheet.cell(row=i, column=3).value = human.gender()
    sheet.cell(row=i, column=4).value = human.age()
    sheet.cell(row=i, column=6).value = human.occupation()
    sheet.cell(row=i, column=7).value = human.email()
    sheet.cell(row=i, column=8).value = human.telephone()
wb.save('1.xlsx')
'''
names = {}
for i in range(2, 1001):
    a = sheet.cell(row=i, column=1).value
    h = sheet.cell(row=i, column=2).value
    if a not in names.keys():
        names[a] = h
    else:
        names[a] += h
lens = []
names2 = []
for i in names.keys():
    lens.append(len(names[i]))
    names2.append(names[i])
index = lens.index(max(lens))
print(names2[index])
'''