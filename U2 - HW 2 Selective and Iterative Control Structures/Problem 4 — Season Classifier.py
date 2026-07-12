while True:
    #input
    mes_input = input("Enter month number (1-12) or 'exit': ")
    #Process
    if mes_input.lower() == "exit":
        break

    mes = int(mes_input)
    #output
    if mes < 1 or mes > 12:
        print("Invalid month. Please enter a number between 1 and 12.")
    elif mes in [12, 1, 2]:
        print("Winter")
    elif mes in [3, 4, 5]:
        print("Spring")
    elif mes in [6, 7, 8]:
        print("Summer")
    else:
        print("Fall")
