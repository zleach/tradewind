import names
import random
import math
import data

from ships import *
from astronomy import *

class Personallity(object):
    def __init__(self,gender):
        self.description = {
            '1': data.parse('<personality.trait.neutral>'),
            '2': data.parse('<personality.trait.positive>'),
            '3': data.parse('<personality.trait.positive> and <personality.trait.neutral>'),
            '4': data.parse('<personality.trait.positive> and <personality.trait.neutral> but <personality.trait.negitive>'),
            '5': data.parse('<personality.trait.positive> but <personality.trait.negitive>')  
        }[str(random.randint(1,5))];
    
    def __str__(self):
      return self.description;
        
class Person(object):
    def __init__(self):
        # Gender
        self.gender = self.gender()
        self.genderTitle = self.genderTitle()
        self.genderPronoun = self.genderPronoun()
        self.genderPossessive = self.genderPossessive()

        # Basics
        self.firstName = names.get_first_name(self.gender)
        self.lastName = names.get_last_name()
        self.personality = self.personality(self.gender)

        # Appearance
        self.eyecolor = data.pick('appearance.eyes.color')
        self.skincolor = data.pick('appearance.skin.color')
        self.hairtype = data.pick('appearance.hair.type')
        self.haircolor = data.pick('appearance.hair.color')
        self.hairstyle = data.pick('appearance.hair.style.'+self.gender)
        self.height = data.pick('appearance.height')
        self.build = data.pick('appearance.build.'+self.gender)
        
        # Other
        self.minimumAge = 18
        self.previousService = self.previousService()
        self.birthPlace = data.pick('places.birthplaces')

    def previousService(self):
        # Only about 5% of people have previous service.
        if(random.randint(0,100) > 94):
            designation = data.pick('ship.type')['designation']
            return names.get_ship_name() + "(" + designation + "-" + str(random.randint(0,127)) +")" 
        else:
            return False
        
    def rank(self,grade):
        return Rank(grade)      
    
    def personality(self,gender):
        return Personallity(gender)
    
    def gender(self):
        if(random.randint(0,99) > 50):
            return 'female'
        else:
            return 'male'

    def genderTitle(self):
        if(self.gender == 'male'): return 'he'
        if(self.gender == 'female'): return 'she'

    def genderPossessive(self):
        if(self.gender == 'male'): return 'his'
        if(self.gender == 'female'): return 'her'

    def genderPronoun(self):
        if(self.gender == 'male'): return 'man'
        if(self.gender == 'female'): return 'woman'
    
    def __str__(self):
        return '%s %s' % (self.firstName,self.lastName)
      
class Officer(Person):
    def __init__(self):
        Person.__init__(self)
        self.rank = self.rank('officer');
        self.age = '%g' % round(random.randint(22,40)*(self.rank.order*.10)+0,0);

class Enlisted(Person):
    def __init__(self):
        Person.__init__(self)
        self.rank = self.rank('enlisted');
        self.age = '%g' % round(random.randint(22,30)*(self.rank.order*.10)+13,0);
        if(self.age <= self.minimumAge): self.age = self.minimumAge;
      
class Pilot(Officer):
    def __init__(self):
        Officer.__init__(self);
        self.callsign = self.callsign();
        self.age = '%g' % round(random.randint(15,25)*(self.rank.order*.10),0);

    def callsign(self):
        return names.get_nick_name()

    def __str__(self):
        return '%s "%s" %s' % (self.firstName,self.callsign,self.lastName)

class HighRankOfficer(Officer):
    def __init__(self):
        Person.__init__(self);
        self.rank = self.rank('high ranking officer');
        self.age = '%g' % round(random.randint(20,30)*(self.rank.order*.10)+13,0);

class Commander(Officer):
    def __init__(self):
        Person.__init__(self);
        self.rank = self.rank('commander');
        self.age = '%g' % round(random.randint(20,30)*(self.rank.order*.10)+13,0);

class Marine(Enlisted):
    def __init__(self):
        Person.__init__(self);
        self.rank = self.rank('marine');
        self.age = '%g' % round(random.randint(20,40)*(self.rank.order*.10)+14,0);
      
class Rank(object):
    def __init__(self,grade):
        rank = data.roll(data.ranks[grade])
        self.abbrivation = rank['abbrivation']
        self.title = rank['title']
        self.designation = rank['designation']
        self.order = int(rank['designation'][2])

        if rank['designation'][0] == 'O':
            self.order = self.order + 10

    def __str__(self):
        return self.abbrivation