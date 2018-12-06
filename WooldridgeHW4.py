'''
Nick Wooldridge
9/5/18
Software Engineering CS4500
Python 3.7.0

Shown below is a pyramid of integers. Think of this pyramid painted on a 
chalk board. You start a “game” by placing your finger at the 1. Then you 
roll a fair dice with exactly 4 sides, labeled UL, UR, DL, and DR. 
(Imagine that you have such a thing.) UL means “up left.” UR means “up 
right.” DL means “down left.” And DR means “down right.” 
               1
            2     3
         4     5     6
      7     8     9    10
   11    12   13    14    15         
16   17    18    19    20    21

Sometimes, you can’t make all the possible moves. For example, if you are 
at 1, you can’t go up. If you are at 19, you can’t go down. If you roll a 
direction you can’t move, you stay where you are in the pyramid, but that 
does count as a “move.” 
There is another aspect to this game. Whenever you make a move, and when 
you start the game on the number 1, you put a dot next to the number where 
you are. You put a new dot on the number even if the “move” forces you to 
stay on the same number. You keep playing this strange “game” until every 
number has at least one dot. At that point, the game is over.

'''

import random #importing random for the "dice roll"
import tkinter as tk #for gui
import sys #for sys.exit
import time #for time.sleep()

root = tk.Tk() #root gui window
root.title("Pyramid Game")
frame = tk.Frame(root, bg='white', height=500, width=500, )
frame.pack()
frame2 = tk.Frame(root, bg='white')
frame2.pack()





class node:
    
    def __init__(self):
        #these 4 values point to other values, if there is a node in that direction
        self.upLeft = None
        self.upRight = None
        self.downLeft = None
        self.downRight = None
        #these 3 values correspond to the row that the node is in and the value and the dots or visits 
        #value is just the index of the node in the array - 1
        #visits is how many "dots" each node has
        #label is for the visual representation
        self.level = 0
        self.value = 0
        self.visits = 0
        self.label = tk.Label(frame)
        

    
        
def main():

    #Explanation print statement
    print("There is a pyramid of integers. You are rolling a 4-sided dice that can either be")
    print("up-left, up-right, down-left, and dow-right. Each roll corresponds with that diagonal")
    print("movement. Dots are amount of time each integer was visited.\n")

    #reads from file and assigns values
    file = open("HWinfile.txt", 'r')
    text = file.readlines()
    
    z = 0
    while z < 4:
        maxLevel = ""
        simulations = ""
        space = False
        count = 0
        for char in text[z]:
            if text[z][count] == " ":
                space = True
            elif not space:
                maxLevel += text[z][count]
            elif space:
                simulations += text[z][count]
            count += 1
                
        maxLevel = int(maxLevel)
        simulations = int(simulations)
        

    
        

        #lists to keep track of total number of moves and max moves for each iteration
        totalMoves = []
        
        y = 0
        while y != simulations:
            
            #For loop to create list for gameboard
            gameBoard = []
            count = 0
            
            while count < maxLevel:
                for i in range(count + 1):
                    gameBoard.append(node())
                
                count += 1
                
            

            #assign values to each object in list
            value = 1
            for x in gameBoard:
                x.value = value
                value += 1

            

            #assign level to each object in list
            #value is the amount of times both for loops run
            value = 0
            #loop amount increases by 1 each iteration of the first for loop
            loopAmt = 1
            #finding level or row of each node
            #in the scenario of max level being 6, the for loop is ranged from (1,7) which runs 6 times
            for level in range(1, maxLevel + 1):
                #inner for loop runs amount of nodes on each level or row 
                for obj in range(loopAmt):
                    gameBoard[value].level = level
                    value += 1
                loopAmt += 1

            #Assign each "pointer" to another value i.e: upLeft, upRight
            #x is each node
            for x in gameBoard:
                #if object is in last level, then no down movement
                if x.level == maxLevel:
                    x.downLeft = None
                    x.downRight = None
                #otherwise, down values are set
                else:
                    #values are derived from downLeft is the value - the level it is on
                    x.downLeft = x.value + x.level
                    x.downRight = x.value + x.level + 1

                #level 1 has no up movements
                if x.level == 1:
                    x.upRight = None
                    x.upLeft = None
                #when value is 2, up values are set because of out of range complications
                elif x.value == 2:
                    x.upLeft = None
                    x.upRight = 1
                #assign up values
                else:
                    #up values are tricky because you need to check whether the value is possible to get to
                    resultValue = x.value - x.level
                    #if no up left movement
                    #if the difference between the current location and the resulting location is 2, move is invalid
                    
                    if x.level - gameBoard[resultValue - 1].level == 2:
                        x.upLeft = None
                    #otherwise assign up left value
                    else:
                        x.upLeft = resultValue

                    resultValue = x.value - x.level + 1
                    #if no up right movement
                    if x.level == gameBoard[resultValue - 1].level:
                        x.upRight = None
                    #otherwise assign up right value
                    else:
                        x.upRight = resultValue
                    
            #Call interactive game
            
            if y == 0 and z == 0:
                part3(gameBoard, 6)
                
            #current location is the node we are on
            currentLocation = 0
            #set initial spot visits to 1
            gameBoard[currentLocation].visits += 1

            #while loop will continue to run until all nodes have been visited
            while True:
                #total roll count
                rollCount = 0
                rollCount += 1
                #dice roll is based on pseudo-random number generator
                diceRoll = random.randint(0,3)
                #dice roll 0 is up left
                if diceRoll == 0:
                    #if move is not possible, stay in same spot and add 1 to visits
                    if gameBoard[currentLocation].upLeft == None:
                        gameBoard[currentLocation].visits += 1
                    #otherwise move to new location and increment visits
                    else:
                        currentLocation = gameBoard[currentLocation].upLeft - 1
                        gameBoard[currentLocation].visits += 1
                    #same as all other dice roll possibilities

                #dice roll 1 is up right
                elif diceRoll == 1:
                    if gameBoard[currentLocation].upRight == None:
                        gameBoard[currentLocation].visits += 1
                    else:
                        currentLocation = gameBoard[currentLocation].upRight - 1
                        gameBoard[currentLocation].visits += 1
                #dice roll 2 is down left       
                elif diceRoll == 2:
                    if gameBoard[currentLocation].downLeft == None:
                        gameBoard[currentLocation].visits += 1
                    else:
                        currentLocation = gameBoard[currentLocation].downLeft - 1
                        gameBoard[currentLocation].visits += 1
                #dice roll 3 is down right
                else:
                    if gameBoard[currentLocation].downRight == None:
                        gameBoard[currentLocation].visits += 1
                    else:
                        currentLocation = gameBoard[currentLocation].downRight - 1
                        gameBoard[currentLocation].visits += 1

               
                
                #while loop ends if loop terminator is true              
                loopTerminator = True
                #searches through array for 0's and sets loop terminator to false if 0 is found
                for x in gameBoard:
                    if x.visits == 0:
                        loopTerminator = False
                if loopTerminator:
                    break; #stops while loop
                
                
            #total number of rolls
            totalDots = 0
            #adds up all rolls or dots
            for x in gameBoard:
                totalDots += x.visits
            totalMoves.append(totalDots)

            
            

                
            #assign values to arrays for later processing
            y += 1
        total = 0
        for g in totalMoves:
            total += g
        M = int(total / len(totalMoves))

        largestDots = 0
        for g in totalMoves:
            if g > largestDots:
                largestDots = g

        
            
        z += 1
        print(maxLevel, simulations, M, largestDots)
    file.close()
    return;


def part3(gameBoard, MAX_LEVEL): #part3 does the visualization with the function revisualize
    
    for i in gameBoard:
        i.label.config(text=str(i.value), height=2, width=5, bg='white')

    statLabel = tk.Label(frame2)
    statLabel.pack()
        
        
    count = 0 #count corresponds to node in gameBoard
    r = 0 #r is row
    c = MAX_LEVEL - 1 #c is column
    
    for x in range(MAX_LEVEL):


        c = MAX_LEVEL - x - 1
        #stay in bounds
        '''
        if count > 20 or r > 5 or c > 10:
            print("Out of bounds error")
            break;
        '''
        
        for y in range(x + 1):
            gameBoard[count].label.grid(row=r, column=c)
            c += 2
            count += 1
        r += 1

    
        
    currentLocation = 0
    previousLocation = 0
    gameBoard[currentLocation].visits += 1
    gameBoard[0].label.configure(bg="#f5f5f5")
    
    
    #while loop will continue to run until all nodes have been visited
    while True:
        #total roll count
        rollCount = 0
        rollCount += 1
        #dice roll is based on pseudo-random number generator
        diceRoll = random.randint(0,3)
        #keep track of previous location
        previousLocation = currentLocation
        #dice roll 0 is up left
        if diceRoll == 0:
            #if move is not possible, stay in same spot and add 1 to visits
            if gameBoard[currentLocation].upLeft == None:
                gameBoard[currentLocation].visits += 1
            #otherwise move to new location and increment visits
            else:
                currentLocation = gameBoard[currentLocation].upLeft - 1
                gameBoard[currentLocation].visits += 1
            #same as all other dice roll possibilities

        #dice roll 1 is up right
        elif diceRoll == 1:
            if gameBoard[currentLocation].upRight == None:
                gameBoard[currentLocation].visits += 1
            else:
                currentLocation = gameBoard[currentLocation].upRight - 1
                gameBoard[currentLocation].visits += 1
        #dice roll 2 is down left       
        elif diceRoll == 2:
            if gameBoard[currentLocation].downLeft == None:
                gameBoard[currentLocation].visits += 1
            else:
                currentLocation = gameBoard[currentLocation].downLeft - 1
                gameBoard[currentLocation].visits += 1
        #dice roll 3 is down right
        else:
            if gameBoard[currentLocation].downRight == None:
                gameBoard[currentLocation].visits += 1
            else:
                currentLocation = gameBoard[currentLocation].downRight - 1
                gameBoard[currentLocation].visits += 1

        #action for animating the visual representation
        root.after(100, revisualize(previousLocation, currentLocation, gameBoard))
        #root.mainloop()
        root.update()
        #while loop ends if loop terminator is true              
        loopTerminator = True
        #searches through array for 0's and sets loop terminator to false if 0 is found
        for x in gameBoard:
            if x.visits == 0:
                loopTerminator = False
        if loopTerminator:
            break; #stops while loop

    #largest dot amount
    largestDots= 0
    smallestDots = 10000
    numMoves = 0
    #for loop finds largest dot amount
    for x in gameBoard:
        if x.visits > largestDots:
            largestDots = x.visits
        if x.visits < smallestDots:
            smallestDots = x.visits
        numMoves += x.visits

    statLabel.config(text="Largest Dots: " + str(largestDots) + "\nAverage Dots: " + str(int(numMoves / len(gameBoard))) + "\nNumber of moves: " + str(numMoves))
    
    

    
    
    
    return;

#responsible for making the current location visible in the visual representation and adding the heat map functionality
def revisualize(previousLocation, currentLocation, gameBoard):
   
    visits = gameBoard[currentLocation].visits
    rgbValue = 255
    if visits > 25:
        rgbHex = "#000000"
    else:
        rgbHex = "#" + "{:02x}{:02x}{:02x}".format(rgbValue - visits * 10, rgbValue - visits * 10, rgbValue - visits * 10)
    
    
    
    #if the current location didn't change
    if previousLocation == currentLocation:
        gameBoard[currentLocation].label.configure(text="***\n***\n***")
        gameBoard[currentLocation].label.configure(bg=rgbHex)
        
        
    else:
        gameBoard[currentLocation].label.configure(text="***\n***\n***")
        gameBoard[previousLocation].label.configure(text=str(gameBoard[previousLocation].value))
        gameBoard[currentLocation].label.configure(bg=rgbHex)
    
    

    return;

 
main()

