from UI import Comp_PhBook

PhBook = Comp_PhBook()
def writing_scv ():
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {PhBook[0]}\n\nИмя: {PhBook[1]}\n\nОтчество: {PhBook[2]}\n\nНомер телефона: {PhBook[3]}\n\nОписание: {PhBook[4]}\n\n\n')

def writing_txt ():
    file = 'Phonebook.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {PhBook[0]}\n\nИмя: {PhBook[1]}\n\nОтчество: {PhBook[2]}\n\nНомер телефона: {PhBook[3]}\n\nОписание: {PhBook[4]}\n\n\n')