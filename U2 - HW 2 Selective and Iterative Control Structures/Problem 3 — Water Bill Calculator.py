total=0
while True:
    #Input
    m3_input=input("Enter your consumption: ")
    #Process
    if m3_input.lower()=="exit":
        break
    m3 = float(m3_input)
    
    if m3<=10:
        charge=m3*8
        print ("Month charge: ",charge)
    elif m3>20:
        charge=m3*18
        print ("Month charge: ",charge)
    else:
        charge=m3*12
        print ("Month charge: ",charge)
        
    total+=charge
    #Output
print("$: ", total)