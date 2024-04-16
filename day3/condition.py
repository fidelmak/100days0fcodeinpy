# the function of if statement is to check for boolean . TRUE or False
print("welcome to rollercOASTER")
height = int(input("whats your height in cm ?"))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("what is your age?"))
    if age < 12:
        bill = 12
        print(F"please pay ${bill}")
    elif age <= 18:
        bill = 20
        print(F"please pay ${bill}")
    elif age >= 45 and age <= 55:
        print("everything is fine , you can have your ride ")
    else:
        bill = 72
        print(F"please pay ${bill}")

    want_photo = input("type Y if you want a photo ang N if you dont ")
    if want_photo == "Y":
        
        print(F" your bill is  ${bill + 5}")
    else:
        print(f"your bill is {bill}")
    
else:
    print("sorry, you have to grow taller to ride ")
