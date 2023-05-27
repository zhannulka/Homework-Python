def printinfo():
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
    return book

def searchinfo():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('ведите ФИО или номер для поиска: ')
        for i in book:
            if temp in i:
                print(i)

def newinfo():
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите новую строку: '+ '\n') )

def deleteinfo(name):
    persons = printinfo()
    with open("phonebook.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if name != person:
                file.write(person)

def changeinfo(new_name, old_name):
    persons = printinfo()          
    with open("phonebook.tx", "w", encoding="utf8" ) as file:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")



while True:
    mode = input('Выберите режим работы справочника' + '\n'
                  +'0-чтение файла, 1-поиск, 2-добавление в файл, 3-удаление, 4-замена, 5-выход: ')
    if mode == '0':
        print(printinfo())
    elif mode == '1':
       searchinfo()
    elif mode == '2':
        newinfo()
    elif mode == '3':
        name = input('Выберите строку для удаления: ')
        deleteinfo(name)
    elif mode == '4':
        old_name = input('Введите ФИО или номер для изменения: ')
        new_name = input('Введите новую инфо: ')
        changeinfo(new_name,old_name)
    elif mode == '5':
        break
    else:
        print('нет режима')

