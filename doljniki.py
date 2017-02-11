from csv import*


with open('data-4289-2017-01-25.csv', 'r', encoding='cp1251') as table:
    table_decoded = DictReader(table, delimiter=';')
    sum_of_debts = 0
    number_of_debts = 0
    for row in table_decoded:
        debt = float(row['Sum'])
        sum_of_debts += debt
        number_of_debts += 1
    middle_debt = sum_of_debts / number_of_debts
    print(middle_debt)
