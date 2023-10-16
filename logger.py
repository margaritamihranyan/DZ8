from data_create import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные?\n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name}; {surname}; {phone}; {adress}\n\n'
                    f'\nВаш выбор: '
                    ))
    if var == 1:
        with open("data_first_variant.csv", "a", encoding="utf-8") as file:
            file.write(f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open("data_second_variant.csv", "a", encoding="utf-8") as file:
            file.write(''f'{name};{surname};{phone};{adress}\n\n')


def print_data():
    print("1 файл: ")
    with open("data_first_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            print(i, end="")

    print("2 файл: ")
    with open("data_second_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            if i != '\n':
                print(i, end="")


def data_delete():
    var = int(input(f'\nВ каком файле хотите удалить данные?\n'))
    if var == 1:
        with open("data_first_variant.csv", "r", encoding="utf-8") as file:
            data = file.readlines()
            for i in data:
                print(i, end="")
        imya = input(f'Напишите имя удаляемого контакта\n')
        index_imya = data.index(imya+"\n")
        del data[index_imya:index_imya + 5]
        with open("data_first_variant.csv", "w", encoding="utf-8") as file:
            for i in data:
                file.write(i)
    if var == 2:
        with open("data_second_variant.csv", "r", encoding="utf-8") as file:
            data = file.readlines()
            for i in data:
                if i != '\n':
                    print(i, end="")
            imya = input(f'Напишите имя удаляемого контакта\n')
            
        def index_containing_substring(the_list, substring):
            for i, s in enumerate(the_list):
                if substring in s:
                    return i
            return -1
        index_imya = index_containing_substring(data, imya)
        del data[index_imya: index_imya + 2]
        with open("data_second_variant.csv", "w", encoding="utf-8") as file:
            for i in data:
                file.write(i)
        

def data_edit():
    var = int(input(f'\nВ каком файле хотите редактировать данные?\n'))
    if var == 1:
        with open("data_first_variant.csv", "r", encoding="utf-8") as file:
            data = file.readlines()
            for i in data:
                print(i, end="")
        imya = input(f'Напишите имя редактируемого контакта\n')
        index_imya = data.index(imya+"\n")
        chislo = int(input(f'Напишите число элемента которое хотите изменить\n'                       
                       f'1: Имя\n'
                       f'2: Фамилие\n'
                       f'3: Телефон\n'
                       f'4: Адрес\n'))
        if chislo == 1:
            novoe_imya = input(f'Напишите новое имя: ')
            data[index_imya] = novoe_imya+"\n"
            with open("data_first_variant.csv", "w", encoding="utf-8") as file:
                for i in data:
                    file.write(i)
        if chislo == 2:
            novoe_familie = input(f'Напишите новое фамилие: ')
            data[index_imya+1] = novoe_familie+"\n"
            with open("data_first_variant.csv", "w", encoding="utf-8") as file:
                for i in data:
                    file.write(i)
        if chislo == 3:
            noviy_telefon = input(f'Напишите новое фамилие: ')
            data[index_imya+1] = noviy_telefon+"\n"
            with open("data_first_variant.csv", "w", encoding="utf-8") as file:
                for i in data:
                    file.write(i)
        if chislo == 4:
            noviy_adres = input(f'Напишите новое фамилие: ')
            data[index_imya+1] = noviy_adres+"\n"
            with open("data_first_variant.csv", "w", encoding="utf-8") as file:
                for i in data:
                    file.write(i)
   
            





        
        










        

         
    
        
    




    
        
        


                    
    
    


