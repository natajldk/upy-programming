grades=[]
while True:
    #input
    grades_input=input("Enter your grades (Or done): ")
    #process
    if grades_input.lower()=="done":
        break
    grades.append(float(grades_input))
    
if len(grades)== 0:
    print ("Enter at least one grade")
else:
    average=sum(grades)/len(grades)
    #output
if average>=7:
    print("You passed")
else:
    print ("You failed")
    