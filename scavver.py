from entity import Entity

class Scavver(Entity):
    def __init__(self):
        self._health = 85
        #max of 100?
        self._stamina = 100
        self._hunger = 15
        #probably max of fifty
        #if hunger is <= 0 then OW!.... but dont go neg, make sure it stays posi
        #still 50/50 on thirst self._thirst
        #self._sleep  ^
        ra = self._rarm = 0
        la = self._larm = 0
        ll = self._lleg = 0
        rl = self._rleg = 0
        self._0damlimb = [ra,rl,ll,la]
        self._1damlimb = []
        # ^ sprain
        self._2damlimb = []
        # ^ broke
        #Any damage taken while in critical state could have like... a 60% chance to sprain or break a limb, restricting certian activitys, 7dtd.
        self._exp = 0
        #decide weather i want a 6
        self._mag = 0
        #loaded Bullets
        self._bleed = 0
        self._rads = 5
        #max of fifty? each point could be equal to 2 health points?

    def update(self):
        pass

    def isAlive(self):
        #originally had a isCrit funciton but that can probably be handled in here pretty well
        return self._health

    def rads(self):
        return self._rads

    def isStarving(self):
        return self._hunger
        if self._hunger >= 12:
            print("your stomache rumbles....")
            #find a way to write this
        if self._hunger <= 0:
            print("you are starving")
            #-1 heath every second
#can probably handle all the food functions