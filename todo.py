works = []

while True:
    print("\nOption:")
    print("Press 1 for add work")
    print("Press 2 for remove work")
    print("Press 3 for see work")
    print("Press 4 for quit from work")

    ch = input("Enter your choice between (1-4): ")

    if ch == '1':
        work = input("Enter your work: ")
        works.append(work)
        print(f"{work} added to to-do list.")
    elif ch == '2':
        work = input("Enter the work to remove from list: ")
        if work in works:
            works.remove(work)
            print(f"{work} removed from to-do list.")
        else:
            print(f"{work} not found in to-do list.")
    elif ch == '3':
        if works:
            print("To-Do List:")
            for index, work in enumerate(works, start=1):
                print(index, work)
        else:
            print("Your To-Do list is empty.")
    elif ch == '4':
        print("Exiting from your To-Do List. Thank you!")
        break
    else:
        print("Invalid choice.")
