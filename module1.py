def Add_employee(e:list,y:list):
    """Функция для добавления работника и его зарплаты. Добавляет имя и зарплату в существующий список.
    :type: str name - имя работника
    :type: int year - год рождения
    """
    while True:
        try:
            name=input("Name: ")
            if name.isalpha():
                try:
                    year=int(input("Birth year YYYY: "))
                except:
                    print("Only numbers!")
                y.append(year)
                e.append(name)
                print(f"Data is added. Name is {name} and his birthyear is: {year}")
                break
        except:
            print("Only letters!")
    y.append(year)
    e.append(name)