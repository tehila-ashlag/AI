applicationExitMode=False
print("Hi user! Lets get started!")
while not applicationExitMode:
    choise=input('''choose operation to execute from below menu:
        1. Connection
        2. Subtraction
        3. Multiplication
        4. Division
        5. Exit ''')
    
    applicationExitMode=int(choise)==5
    if applicationExitMode==False:
        firstNum=int(input("enter first number"))
        secondNum=int(input("enter second number"))
        if int(choise)==3:
            result=firstNum*secondNum
        elif int(choise)==2:
            result=firstNum-secondNum
        elif int(choise)==1:
            result=firstNum+secondNum
        elif int(choise)==4:
            result=firstNum/secondNum

        print("the result is ", result )




    

    
    