print("welcome to rollercOASTER")
height = int(input("whats your height in cm ?"))

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("what is your age?"))
    if age <= 18:
        print("please pay $7")
    else:
        print("please pay $12")
    
else:
    print("sorry, you have to grow taller to ride ")
