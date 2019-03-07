# Player class contains allows the user to customize their "player" within the game

class Player():
    def __init__(self, name, gender, gradeLevel):
        self.name = name
        self.gender = gender
        self.gradeLevel = gradeLevel
        self.score = 0
        self.numberOfMoves = 0
        self.currentLoc = 0
        self.locName = ""
        self.description = ""
        self.map = False
        self.inventory = []
