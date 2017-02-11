from csv import*


with open('data-4289-2017-01-25.csv', 'r', encoding='cp1251') as table_debts:
    table_debts_decoded = DictReader(table_debts, delimiter=';')
    sum_of_debts = 0
    number_of_debts = 0
    for row in table_debts_decoded:
        debt = float(row['Sum'])
        sum_of_debts += debt
        number_of_debts += 1
    middle_debt = sum_of_debts / number_of_debts
    print('Средняя задолженность по аренде =', middle_debt, 'рублей')

with open('data-4905-2017-01-27.csv', 'r', encoding='cp1251') as table_parkings:
    table_parkings_decoded = DictReader(table_parkings, delimiter=';')
    sum_all_parkings = 0
    for row in table_parkings_decoded:
        capacity = int(row['CarCapacity'])
        price = int(float(row['Price']))
        full_parking_price = capacity * price
        sum_all_parkings += full_parking_price
    print('Сумма, идущая со всех забитых парковок в час =', sum_all_parkings)

with open('data-408-2016-08-17.csv', 'r', encoding='cp1251') as table_taxi:
    table_taxi_decoded = DictReader(table_taxi, delimiter=';')
    sum_of_places = 0
    for row in table_taxi_decoded:
        if row['AdmArea'] == 'Юго-Западный административный округ':
            sum_of_places += int(row['CarCapacity'])
    print('В Юго-Западном административном округе может припарковаться максимум', sum_of_places, 'такси (на спец.парковках)')
