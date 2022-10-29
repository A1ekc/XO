from questions import info

info = view() 
def writing_scv ():
    file = 'Phonebook.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'{info[0]};{info[1]}\n') # две колонки  Робот - Клиент
