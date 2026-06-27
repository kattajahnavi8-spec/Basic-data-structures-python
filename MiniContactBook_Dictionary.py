contacts = {}
while True:
    print("\n1.Add Contact")
    print("2.View Contacts")
    print("3.Search Contact")
    print("4.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:  
        name = input("Name: ")  
        phone = input("Phone: ")  
        contacts[name] = phone  
    elif choice == 2:  
        print(contacts)   
    elif choice == 3:  
        name = input("Enter name: ")  
        if name in contacts:  
            print("Phone:", contacts[name])  
        else:  
            print("Contact not found")  
    elif choice==4:
        break               