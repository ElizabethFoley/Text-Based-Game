# Class for all the locations of the game

class Locale():

    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = item
        self.visited = False
