while True:
    #Input
    weight_input=input("Enter your weight: ")
    #Process
    if weight_input.lower()=="exit":
        print("Task finished")
        break
    weight = float(weight_input)
    height= float(input("Enter your height: "))
    BIM= weight/(height*height)
    #Output
    if BMI<18.5:
        print("Underweight")
    elif BMI <= 25:
        print("Normal")
    elif BMI <=30:
        print("Overweight")
    else:
        print("Obese")