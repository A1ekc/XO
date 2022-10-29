def creating ():
    file = 'Robotmagazine.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Робот;Клиент\n')