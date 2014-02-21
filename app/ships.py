import random
import math
import names
from data import *

from people import *
from astronomy import *

class Ship(object):
    def __init__(self,prefix,shipType,crewSize):

        # Name
        self.name = names.get_ship_name()
        self.hasCommandElement = False
        
        # Type
        if shipType == 0:
            shipType = pick('ship.type')
        else:
            shipType = ship['type'][shipType-1]
                
        self.prefix = prefix
        self.typeName = shipType['name']
        self.typeCode = shipType['designation']
        self.idNumber = random.randint(1,177)
        
        # Characteristics
        self.activeServiceDuration = random.randint(0,60)
        self.commissionedDate = pickDate()
        self.activeServiceDate = addYears(self.commissionedDate,self.activeServiceDuration)
        self.homesystem = Starsytem()
        self.homeport = random.choice(self.homesystem.planets)

        # Divisions
        self.divisions = []
        for i in range(0, len(shipType['divisions'])):
            divisionCode = shipType['divisions'][i]
            self.divisions.append(Division(divisionCode))
        
        for division in self.divisions:
            mulitplier = random.random()
            divisionSize = int(round(division.size*crewSize,0))
            
            # One person minimum.
            if divisionSize == 0:
                divisionSize = 1
            
            for i in range(0, divisionSize):                        
                if random.random() < division.rank: person = Officer()
                else: person = Enlisted()
                
                if(division.hasCallsigns): person = Pilot()                
                if(division.marines): person = Marine()
        
                division.crew.append(person)        
            
            division.crew = sorted(division.crew, key = lambda person: (person.rank.order))
            division.crew.reverse()

        if len(self.divisions) > 2:
            self.hasCommandElement = True
            self.co = HighRankOfficer()
            self.xo = Commander()          


class Division(object):
    def __init__(self,code):
        self.crew = []
        self.code = code
        self.name = ship['division'][code]['name']
        self.size = ship['division'][code]['size']
        self.rank = ship['division'][code]['rank']

        try:
            self.hasCallsigns = ship['division'][code]['callsigns']
        except KeyError:    
            self.hasCallsigns = False
        
        try:
            self.marines = ship['division'][code]['marines']
        except KeyError:
            self.marines = False