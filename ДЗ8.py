def printinfo():
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
    return book

def searchinfo():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('Введите ФИО или номер для поиска: ')
        for i in book:
            if temp in i:
                print(i)

def newinfo():
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите новую строку: '+ '\n') )


while True:
    mode = input('Выберите режим работы справочника' + '\n'
                  +'0-чтение файла, 1-поиск, 2-добавление в файл, 3-выход: ')
    if mode == '0':
        print(printinfo())
    elif mode == '1':
       searchinfo()
    elif mode == '2':
        newinfo()
    elif mode == '3':
        break
    else:
        print('нет режима')
