#traffic lights
color=input("ingresa un color: ").lower ()
if color == "red":
    print ("stop")
elif color=="yellow":
    print("warning")
elif color == "green":
    print("go")
else:
    print("invalid")