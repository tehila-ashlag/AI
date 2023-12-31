
gameDashboard=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

movesCounter=0
currentUser="X"

def printGameDashboard():
    for i in range(3):
        for j in range(3):
            if j<2:
                print(gameDashboard[i][j],end=' | ')
            else:
                print(gameDashboard[i][j])
        if i<2:
            print("- + - + -")
    print()

def oneMove():
    global currentUser, row, col,movesCounter
    movesCounter+=1
    placementDone=False
    while placementDone==False:
        row=int(input("Hey User "+ currentUser +"! its your turn - which row u choose?"))
        col=int(input("and which column u choose?"))
        isValidRowAndCol=row>-1 and row<3 and col>-1 and col<3
        if isValidRowAndCol and gameDashboard[row][col]==" ":
            gameDashboard[row][col]=currentUser
            placementDone=True
        else:
            print("this is not valid square! it is already full or not exist pls choose different one!")
        
    if currentUser=="X":
        currentUser="O"
    else:
        currentUser="X"

    printGameDashboard()

def isDashboardFull():
    isDashboardFull=True
    for i in range(3):
        j=0
        while j<3 and isDashboardFull:
            if gameDashboard[i][j]==" ":
                isDashboardFull=False
            j+=1
    
    return isDashboardFull

def checkDashboard():
    lastUser=gameDashboard[row][col]
    foundFixedRow=True
    foundFixedCol=True
    foundFixedSlant=True
    foundFixedBackSlant=True
    checkAlsoSlant=row==col or row+col==2
    for i in range(3):
        if gameDashboard[row][i]!=lastUser:
            foundFixedRow=False
        if gameDashboard[i][col]!=lastUser:
            foundFixedCol=False
        if checkAlsoSlant:
            if row==col:
                if gameDashboard[i][i]!=lastUser:
                    foundFixedSlant=False
            elif gameDashboard[i][2-i]!=lastUser:
                    foundFixedBackSlant=False

    if foundFixedCol==True or foundFixedRow==True or (checkAlsoSlant and ((row==col and foundFixedSlant==True) or ( row!=col and foundFixedBackSlant==True))):
        return "The Winner is "+lastUser+" !!"
    elif isDashboardFull()==True:
        return "Teko!!"
    else:
        return "dashboard is still getting filled..."

def playing():
    endOfGame=False
    while endOfGame==False:
        oneMove()
        if(movesCounter>=5):
            currentMode=checkDashboard()
            if currentMode=="dashboard is still getting filled...":
                endOfGame=False
            else:
                endOfGame=True
                print(currentMode)

print('''Hi! Lest start play together!
      
      ''')
playing()




                
