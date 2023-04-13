import pygame

class Entity:
    cur = []

    def __init__(self, name, team):
        self._name = name
        self._team = team
        self._inventory = []
        self._health = 0
        self._pos = (0, 0)
        self._bleed = 0

    def update(self):
        # define for each subclass
        pass

    def isEntAlive(self):
        return self._health > 0

    def isEntCritical(self):
        return self._health <= 12

    def getTeam(self):
        return self._team

    def getName(self):
        return self._name

    def getActiveTexture(self):
        return pygame.Surface()

'''Subclasses:
    -Dog (N)
    -Mutated Dog (H)
    -Scavenger (H)
    -Survivor (N)
    -Ethan Strohm (¿PH?)
    -Crates (P)
    -Dropped Items (P)
    +
    '''
'''
  - position
  - inventory
  - health
  - textures
  - velocity?
  - create function
  - update function
  - on death function
  - interaction
'''
