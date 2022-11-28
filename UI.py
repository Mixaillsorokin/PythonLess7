def Comp_PhBook ():
    PhBook = []
    Surname = input('Введите фамилию: ')
    PhBook.append(Surname)
    Name = input('Введите имя: ')
    PhBook.append(Name)
    Middle_name=input('Введите отчество: ')
    PhBook.append(Middle_name)
    phone_number = ''
    valid =False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    PhBook.append(phone_number)
    description = input('Введите описание: ')
    PhBook.append(description)
    return PhBook