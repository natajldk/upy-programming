total = 0
while True:
    # Input
    weight_input = input("Enter package weight (kg) or exit: ")
    if weight_input.lower() == "exit":
        break

    weight = float(weight_input)
    distance = float(input("Enter distance (km): "))
    # Process
    if distance <= 100:
        if weight <= 5:
            cost = 50
        else:
            cost = 80
    else:
        if weight <= 5:
            cost = 120
        else:
            cost = 200
    # Output
    print("Shipping cost: $",cost)
    total += cost

print("Total accumulated shipping cost: $",cost)
