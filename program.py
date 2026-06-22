from book import cBook


class Main:
    book = cBook()
    try:
        book.Load()
    except FileNotFoundError:
        book.Save()
    menu = {"1": "Display", "2": "Add", "3": "Remove", "4": "Search", "5": "Exit",}
    inMenu = True
    while inMenu == True:
        print("Contacts Book\n MENU")
        for key, value in menu.items():
            print(f"{key}: {value}")
        choice = input("Please input no. or type menu option: ").lower().title()
        print(choice)
        for key, value in menu.items():
            if choice == key or choice == value:
                choice = value
                break
        else:
            print("Not an option")
        if choice == "Display":
            book.Display()
        elif choice == "Add":
            book.AddC()
        elif choice == "Remove":
            book.RemoveC()
        elif choice == "Search":
            book.Search()
        elif choice == "Exit":
            book.Save()
            print("Exiting Contacts")
            break