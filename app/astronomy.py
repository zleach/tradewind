import names
import random
import data

from ships import *
from people import *

class AstronomicalObject(object):
    def __init__(self):
        self.name = ""

class Starsytem(AstronomicalObject):
    def __init__(self):
        AstronomicalObject.__init__(self)
        self.planets = data.generate(Planet,1,7)
        
        for i in range(0, len(self.planets)):
            self.planets[i].suffix = data.romanNumeral(i+1)

class PlanetaryBody(AstronomicalObject):
    def __init__(self):
        AstronomicalObject.__init__(self)
        self.name = data.pick('astronomy.planet.name')

class Planet(PlanetaryBody):
    def __init__(self):
        PlanetaryBody.__init__(self)
        self.moons = data.generate(Moon,0,10)

    def __str__(self):
        return "%s %s" % (self.name,self.suffix)

class Moon(PlanetaryBody):
    def __init__(self):
        PlanetaryBody.__init__(self)

# Places
class Place(object):
    def __init__(self):
        self.name = ""

class Shipyard(Place):
    def __init__(self):
        Place.__init__(self)