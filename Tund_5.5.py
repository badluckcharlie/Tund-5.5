import module1

print("Employee data")
print("-" * 20)

while True:
    start = input("Please type '1' to start or '0' to exit: ")

    if start == "1":
        print("-" * 20)
        module1.show_workers()

        choice = input("Press '1' to start entering data or '0' to skip: ")
        if choice == "1":
            try:
                amount = int(input("How many workers do you want to add? "))
                module1.add_workers(amount)
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            print("Options:")
            print("1. Show employee data")
            print("2. Find average employee age")
            print("3. Show 10 youngest/oldest workers")
            print("4. Find employee by age")
            print("5. Remove employee from the list")
            print("0. Exit program")

            try:
                choice_def = int(input("Please select an option: "))
            except ValueError:
                print("Invalid input. Use numbers from 0 to 5.")
                continue

            if choice_def == 1:
                module1.show_workers()
            elif choice_def == 2:
                module1.average_age()
            elif choice_def == 3:
                module1.list_oldest_youngest()
            elif choice_def == 4:
                try:
                    age = int(input("Enter age to find: "))
                    module1.find_by_age(age)
                except ValueError:
                    print("Invalid age input.")
            elif choice_def == 5:
                name = input("Enter the name of the worker to remove: ")
                module1.remove_worker(name)
            elif choice_def == 0:
                print("Exiting program.")
                exit()
            else:
                print("Please select a valid option from 0 to 5.")

    elif start == "0":
        print("Exit selected.")
        break
    else:
        print("Invalid input. Please enter '1' or '0'.")