#password game
import datetime

characters = "A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z a b c d e f g h i j k l m n ñ o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 ! # $ % & ' ( ) * + - . / : ; < = > ? @ [ ] ^ _ ` { | } ~"
month = datetime.datetime.now().strftime("%B").lower()
errors = ""
unlocked = 1
ask_password = True

while True:
    #Input
    if ask_password == True:
        password = input("Ingresa tu contraseña: ")
    #Process
    ask_password = True
    errors = ""
    
    if unlocked >= 1:
        if len(password) < 8:
            errors += "Your password must be at least 8 characters.\n"
        
        valid_chars = characters.split()
        for letra in password:
            if letra not in valid_chars and letra != " ": 
                errors += f"El carácter {letra} no está permitido\n"
                break

    if unlocked >= 2:
        tiene_mayuscula = False
        for letra in password:
            if letra in "QWERTYUIOPASDFGHJKLÑZXCVBNM":
                tiene_mayuscula = True
                break
        if tiene_mayuscula == False:
            errors += "Add at least one uppercase letter.\n"   

    if unlocked >= 3:
        tiene_minuscula = False
        for letra in password:
            if letra in "qwertyuiopasdfghjklñzxcvbnm":
                tiene_minuscula = True
                break
        if tiene_minuscula == False:
            errors += "Add at least one lowercase letter.\n"

    if unlocked >= 4:
        tiene_digito = False
        for digito in password:
            if digito in "0123456789":
                tiene_digito = True
                break
        if tiene_digito == False:
            errors += "Add at least one number.\n"

    if unlocked >= 5:
        tiene_espcaracter = False
        for caracter in password:
            if caracter in "!@#$%^&":
                tiene_espcaracter = True
                break
        if tiene_espcaracter == False:
            errors += "Add at least one special character (!@#$%^&).\n"

    if unlocked >= 6:
        suma = 0
        for letra in password:
            if letra in "0123456789":
                suma += int(letra)
        if suma != 25:
            errors += "The digits in your password must add up to 25.\n"

    if unlocked >= 7:
        longitud = len(password)
        es_primo = True
        
        if longitud < 2:
            es_primo = False
        else:
            divisor = 2
            while divisor < longitud:
                if longitud % divisor == 0:
                    es_primo = False
                    break
                divisor = divisor + 1
                
        if es_primo == False:
            errors += "Your password length must be a prime number.\n"

    if unlocked >= 8:
        tiene_mes = False
        if month in password:
            tiene_mes = True
            
        if tiene_mes == False:
            errors += "Your password must include the current month in lowercase.\n"
 #Output
    if errors == "":
        if unlocked < 8:
            unlocked = unlocked + 1
            ask_password = False
            print("Rule passed, new instruction available")    
        else:
            print("congrats")
            break
    else:
        print("To fix: ")
        print(errors)