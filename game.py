# CMPT 120L 113
# Libby Foley
# 20 Sep 2018
###

##
# In my final commit, I added a class object for the player and the locales
#                     I added and "use item" feature for the candle
#                     I made the candle have "limited uses"
#                     I added the ability for the player to ascend or descend down the stairway
#                     I added print a inventory function that prints the inventory
#                     I set a "win" condition
#                     I gave the user a chance to play again
##

from Player import Player
from Locale import Locale
player = Player("", "", "")

MAP = '''
                  nurse's office
                        |
                        |
                        |
library---stairway---secondFloor---door out---outside
            |           |
            |           |     
            |           |
            |       classroom2
            |
bathroom---------classroom1
            |
            |
            |
         hallway
    '''

title = ("\nRun"
        "\n=======\n")
print(title)
    

intro = (" You suddenly awake. Your heart is racing. You don't know where you are."
            " You look around and calm down. It seems you're still at your high school."
            " But something is different. The classrooms are the same, but everything"
            " is run down and dark. There are cobwebs everywhere, holes in the floors"
            " and walls, and turned over desks. You decide to look around to find a"
            " familiar face. As you walk, you notice the hallway seems too quiet,"
            " and you realize you're the only person in the entire school. Your"
            " heart starts to pound. You question where everyone else is. Despite"
            " your fear, you keep walking through the dark hall. You see something"
            " at the end of the hall. You're suddenly surrounded by a horrible smell."
            " You use you shirt to cover your nose and look down. You jump back, you" 
            " see blood and guts spilled out on the floor, along with a student ID tag. It looks as if someone"
            " was just killed, but you thought you were the only one in the building."
            " Where are you? You keep staring at the decomposing body, you can't look away."
            " Suddenly, you hear something behind you. Maybe an axe dragging on the"
            " floor. There's laughing too. You turn around...")


def showIntro():
    print(title)
    print(intro)
    prompt()

# current locations
hallway = Locale("Hallway", ("You are in the same hallway. You have turned around, but see no one. Everything looks different."
                           "The halls have shifted. You are not where you were before. There are holes in"
                         "the floors everywhere and they seem to be endless. You start walking, everything is dark.") , None)
        
bathroom = Locale("Bathroom", ("You find a bathroom. It is the first room you see in the hallway. You open a stall and see a body"
                            "hanging, swaying above you. You scream, run out of the bathroom, and question where you really are."
                            "Finally, you get out and see an empty classroom."), None)

classroom1 = Locale("Classroom1", ("You walk into the classroom, hoping you escaped. It's dark, but there is one candle lit."
                            "Suddenly, the door slams shut and the candle goes out."
                             "It's now pitch black in the classroom. You start to hear voices circling around you."
                           "You feel as if you are going mad and scream in terror."
                            "You run for the door, stumbling over fallen desks and chairs."
                             "You pull at the door, but it won't open. You hear the same footsteps again and freeze."
                            "You turn around, no one is there."), "candle")

stairway = Locale("Stairway", ("You go out into the hall, still you see no one. However, you come across unfamiliar stairs."
                              "You decide to go up. As you walk, decaying body parts and spilled guts lay there, but you seem to be unphased."
                           "Are you going mad?"), None)

secondFloor = Locale("Second Floor", ("You are in the second floor hallway. This new floor is different"
                                "than the first. It only has one hallway with a door at the end."), None)

doorOut = Locale("Door Out", ("You head for the only door in the hallway, hoping it is a way out."
                           "All the windows and doors out of the school are locked shut. You pull on the handle, it opens."), None)

nurseOffice = Locale("Nurse's Office", ("You see a table on one side of the room and a small bed on the other. There's a broken cabinet"
                               "above the table. It is mostly empty, but you find a bloody syringe and wonder why the blood looks"
                                 "so fresh."), "bloody syringe")

outside = Locale("Outside", ("You finally get outside on the second floor. There's hope for you after all... or is there? You soon realize"
                           "that there is nowhere for you to land if you jump down from the short hallway you are in. Trees surround you"
                           "and cover the floor on the ground below you. There is no way out after all."), None)

classroom2 = Locale("Classroom2", ("You find another classroom, but this one is different than the other one."
                               "You walk towards the teacher's desk in the front of the room and see something in one of the half open"
                              "drawers. It is a pair of scissors."), "scissors")

library = Locale("Library", ("You turn left at the stairway and there is a door. You walk in and see books scattered across the floor."
                           "Most of the books are dirty and torn apart. You then find a map on the floor among the books."), "map")
objects = [hallway, bathroom, classroom1, stairway, secondFloor, doorOut, nurseOffice, outside, classroom2, library]

ending = ("You hear footsteps and laughing behind you. You want to turn around, but instead you freeze."
          "You can't move and your heart begins to race. Suddenly, you feel a sharp pain and"
          "blood begin to run down your back. You have been killed.")
credit = ("\nCopyright (c) 2016-2018 Matthew A Johnson, Matt.Johnson@marist.edu")

maxMoves = 25

def prompt():
    input("\n<Press Enter to continue...>")

def earnPoints(pts):
    player.score += pts

def take(locale):
    print("You found: " + str(locale.item))
    if locale.item !=None:
        temp = True
    else:
        print("There are no items here")
        temp = False
    while temp:
        taking = input("Do you want to take this item? 'yes' or 'no' ")
        if taking.lower().strip() == "yes":
            player.inventory.append(locale.item)
            if locale.item == "map":
                player.map = True
            locale.item = None
            temp = False
        elif taking.lower().strip() == "no":
            break
        else:
            print("You must enter 'yes' or 'no'")
            

# Locales  
def goHallway():
    player.description = hallway.description
    player.locName = hallway.name
    player.currentLoc = 0
    player.numberOfMoves +=1
    take(hallway)
    if not hallway.visited:
        earnPoints(5)
        hallway.visited = True

def goBathroom():
    player.description = bathroom.description
    player.locName = bathroom.name
    player.currentLoc = 1
    player.numberOfMoves +=1
    take(bathroom)
    if not bathroom.visited:
        earnPoints(5)
        bathroom.visited = True
        

def goClassroom1():
    player.description = classroom1.description
    player.locName = classroom1.name
    player.currentLoc = 2
    player.numberOfMoves +=1
    take(classroom1)
    if not classroom1.visited:
        earnPoints(5)
        classroom1.visited = True
        
    
def goStairway():
    player.description = stairway.description
    player.locName = stairway.name
    player.currentLoc = 3
    player.numberOfMoves +=1
    take(stairway)
    if not stairway.visited:
        earnPoints(5)
        stairway.visited = True
    

def goSecondFloor():
    player.description = secondFloor.description
    player.locName = secondFloor.name
    player.currentLoc = 4
    player.numberOfMoves +=1
    take(secondFloor)
    if not secondFloor.visited:
        earnPoints(5)
        secondFloor.visited = True
        

def goDoorOut():
    player.description = doorOut.description
    player.locName = doorOut.name
    player.currentLoc = 5
    player.numberOfMoves +=1
    take(doorOut)
    if not doorOut.visited:
        earnPoints(5)
        doorOut.visited = True
       

def goNurseOffice():
    player.description = nurseOffice.description
    player.locName = nurseOffice.name
    player.currentLoc = 6
    player.numberOfMoves +=1
    take(nurseOffice)
    if not nurseOffice.visited:
        earnPoints(5)
        nurseOffice.visited = True
        

def goOutside():
    player.description = outside.description
    player.locName = outside.name
    player.currentLoc = 7
    player.numberOfMoves +=1
    take(outside)
    if not outside.visited:
        earnPoints(5)
        outside.visited = True
    

def goClassroom2():
    player.description = classroom2.description
    player.locName = classroom2.name
    player.currentLoc = 8
    player.numberOfMoves +=1
    take(classroom2)
    if not classroom2.visited:
        earnPoints(5)
        classroom2.visited = True
        

def goLibrary():
    player.description = library.description
    player.locName = library.name
    player.currentLoc = 9
    player.numberOfMoves +=1
    take(library)
    if not library.visited:
        earnPoints(5)
        library.visited = True
        
        
# Create Student ID
def setupPlayer():
    print("Create your character. What is your high school student ID?")
    name = input("Enter your name: ")
    gender = input("Girl or Boy: ")
    gradeLevel = input("What year of highschool are you in? (9th, 10th, 11th, 12th)? ")
    player.name = name
    player.gender = gender
    player.gradeLevel = gradeLevel
    print("Your student ID: " , player.name , " " , "Gender: " , player.gender , "Grade Level: " , player.gradeLevel)
    prompt()
    goHallway()

def showOutro():
    if player.score == 50:
        print("You have escaped.")
    else:
        print(ending)
    print(credit)

def processInput():
    global com
    pass
    com = input("Enter a command: ")

def updateGame():
    print("updating the game")
updateGame()

def getCommand():
    global cmd
    cmd = input("\nWhat do you want to do next? ").strip().lower()
    return cmd

def renderGame():
    print("\nLocation: " , player.locName, "  Score: ", player.score, "  Moves: " , player.numberOfMoves)
    print(player.description)

# play again
def playAgain():
    again = input("Do you want to play again? 'yes' or 'no'")
    if again.strip().lower() == "yes":
        player.numberOfMoves = 0
        player.score = 0
        player.map = False
        player.inventory = []
        uses = 1
        for x in objects:
            x.visited = False
        main()
    else:
        pass
        
def printInventory():
    print("You have: ")
    for x in player.inventory:
        print(x)
        

# candle uses
uses = 1   
def containsItem(inventory, item):
    for x in inventory:
        if x == item:
            return True
    return False

# Game Loop
def gameLoop():
    global cmd, uses
    while player.numberOfMoves < maxMoves and player.score < 50:
        renderGame()
        getCommand()
        
        if cmd == "quit" or player.numberOfMoves >= maxMoves:
            break
        elif cmd == "help":
            print("\nValid commands are: 'North' , 'South' , 'East' , 'West' , 'help' , 'quit' , 'inventory' , 'use candle (if found)'")
        elif cmd == "map":
            if player.map:
                print(MAP)
            else:
                print("You haven't found the map yet.")
        elif cmd == "inventory":
            printInventory()
        # use item: candle
        elif cmd == "use candle":
            if containsItem(player.inventory, "candle") and uses <= 3:
                print("You light the candle")
                uses += 1
            elif not containsItem(player.inventory, "candle"):
                print("You do not have a candle")
            elif containsItem(player.inventory, "candle") and uses > 3:
                print("You don't have any more candle uses")
        elif cmd == "north":
            if player.currentLoc == 0: #hallway
                answer = input("Would you like to go up the stairs? 'yes'or 'no'")
                if answer.lower().strip() == "yes":
                    goStairway()
                elif answer.lower().strip() == "no":
                    print("You stay in the hallway")
                    goHallway()
            elif player.currentLoc == 4: #secondFloor
                goNurseOffice()
            elif player.currentLoc == 8: #classroom 2
                goSecondFloor()
            else:
                print("You can't go further North from here.")
        elif cmd == "south":
            if player.currentLoc == 1: #bathroom
                goHallway()
            elif player.currentLoc == 6: #nurse's office
                goSecondFloor()
            elif player.currentLoc == 3: #stairway
                goHallway()
            elif player.currentLoc == 2: #classroom1
                goHallway()
            elif player.currentLoc == 4: #second floor
                goClassroom2()
            else:
                print("You can't go furhter South from here.")
        elif cmd == "east":
            if player.currentLoc == 0: #hallway
                goClassroom1()
            elif player.currentLoc == 3: #stairway
                goSecondFloor()
            elif player.currentLoc == 1: #bathroom
                goHallway()
            elif player.currentLoc == 4: #seconfloor
                goDoorOut()
            elif player.currentLoc == 5: #doorOut
                goOutside()
            elif player.currentLoc == 9: #library
                answer = input("Would you like to go down the stairs? 'yes'or 'no'")
                if answer.lower().strip() == "yes":
                    hallway()
                elif answer.lower().strip() == "no":
                    print("You stay on the second floor")
                    goSecondFloor()
            else:
                print("You can't go further East from here.")
        elif cmd == "west":
            if player.currentLoc == 0: #hallway
                goBathroom()
            elif player.currentLoc == 2: #classroom1
                goHallway()
            elif player.currentLoc == 5: #doorout
                goSecondFloor()
            elif player.currentLoc == 4: #secondfloor
                answer = input("Would you like to go down the stairs? 'yes'or 'no'")
                if answer.lower().strip() == "yes":
                    goHallway()
                elif answer.lower().strip() == "no":
                    print("You stay on the second floor")
                    goLibrary()
            elif player.currentLoc == 7: #outside
                goDoorOut()
            elif player.currentLoc == 3: #stairway
                goLibrary()
            else:
                print("You can't go further West from here.")
        else:
            print("\nThis is not a valid command.")
        if player.score == 50 or player.numberOfMoves == maxMoves:
            showOutro()
    
            
def main():
    showIntro()
    setupPlayer()
    gameLoop()
    playAgain()

main()
