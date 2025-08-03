import names
import random
import data

class Character(object):
    def __init__(self, gender=None):
        # Basic identity
        self.gender = gender if gender else self.gender()
        self.genderTitle = self.genderTitle()
        self.genderPronoun = self.genderPronoun()
        self.genderPossessive = self.genderPossessive()
        
        # Names and age
        self.firstName = names.get_first_name(self.gender)
        self.lastName = names.get_last_name()
        self.age = random.randint(16, 85)
        
        # Physical appearance
        self.eyecolor = data.pick('appearance.eyes.color')
        self.skincolor = data.pick('appearance.skin.color')
        self.hairtype = data.pick('appearance.hair.type')
        self.haircolor = data.pick('appearance.hair.color')
        self.hairstyle = data.pick('appearance.hair.style.'+self.gender)
        self.height = data.pick('appearance.height')
        self.build = data.pick('appearance.build.'+self.gender)
        
        # Character development core
        self.primaryMotivation = data.pick('character.motivations.primary')
        self.coreFlaws = self.generateFlaws()
        self.fears = data.pick('character.fears')
        self.secret = data.pick('character.secrets')
        self.moralAlignment = data.pick('character.morality')
        self.emotionalCore = data.pick('character.emotional_traits')
        
        # Background and context
        self.socioeconomicBackground = data.pick('character.background.socioeconomic')
        self.educationLevel = data.pick('character.background.education')
        self.occupation = data.pick('character.occupations')
        self.familyBackground = data.pick('character.family_background')
        self.formativeExperience = data.pick('character.formative_experiences')
        
        # Skills and talents
        self.primarySkill = data.pick('character.skills.primary')
        self.hiddenTalent = data.pick('character.skills.hidden')
        
        # Relationship patterns
        self.relationshipStyle = data.pick('character.relationship_patterns')
        self.trustIssues = data.pick('character.trust_patterns')
        
        # Goals and conflicts
        self.shortTermGoal = data.pick('character.goals.short_term')
        self.longTermGoal = data.pick('character.goals.long_term')
        self.internalConflict = data.pick('character.internal_conflicts')
        
        # Origin and setting
        self.birthPlace = data.pick('places.birthplaces')
        
        # Personality beyond flaws
        self.positiveTraits = self.generatePositiveTraits()
        self.quirks = data.pick('character.quirks')
        
    def generateFlaws(self):
        """Generate 1-3 character flaws"""
        flaw_count = random.randint(1, 3)
        flaws = []
        available_flaws = data.character['flaws']['major'] + data.character['flaws']['minor']
        
        for _ in range(flaw_count):
            flaw = random.choice(available_flaws)
            if flaw not in flaws:
                flaws.append(flaw)
        
        if len(flaws) == 1:
            return flaws[0]
        elif len(flaws) == 2:
            return f"{flaws[0]} and {flaws[1]}"
        else:
            return f"{flaws[0]}, {flaws[1]}, and {flaws[2]}"
    
    def generatePositiveTraits(self):
        """Generate 2-4 positive character traits"""
        trait_count = random.randint(2, 4)
        traits = []
        available_traits = data.character['positive_traits']
        
        for _ in range(trait_count):
            trait = random.choice(available_traits)
            if trait not in traits:
                traits.append(trait)
        
        if len(traits) == 2:
            return f"{traits[0]} and {traits[1]}"
        elif len(traits) == 3:
            return f"{traits[0]}, {traits[1]}, and {traits[2]}"
        else:
            return f"{traits[0]}, {traits[1]}, {traits[2]}, and {traits[3]}"
    
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
        return '%s %s' % (self.firstName, self.lastName)

class Protagonist(Character):
    """A main character with stronger motivations and more complex backstory"""
    def __init__(self, gender=None):
        Character.__init__(self, gender)
        # Protagonists get additional depth
        self.heroicFlaw = data.pick('character.flaws.heroic')
        self.characterArc = data.pick('character.arcs.protagonist')
        self.callToAdventure = data.pick('character.call_to_adventure')
        self.mentalToughness = data.pick('character.mental_strength')

class Antagonist(Character):
    """An opposing character with compelling but misguided motivations"""
    def __init__(self, gender=None):
        Character.__init__(self, gender)
        # Antagonists have twisted motivations
        self.primaryMotivation = data.pick('character.motivations.antagonist')
        self.corruptionSource = data.pick('character.corruption_sources')
        self.redeemedQuality = data.pick('character.positive_traits')  # Even villains have good qualities
        self.methodOfControl = data.pick('character.control_methods')

class SupportingCharacter(Character):
    """A supporting character with specific relationship to protagonists"""
    def __init__(self, gender=None):
        Character.__init__(self, gender)
        # Supporting characters defined by their relationship role
        self.relationshipRole = data.pick('character.supporting_roles')
        self.loyaltyLevel = data.pick('character.loyalty_levels')
        self.supportType = data.pick('character.support_types')

class ComicRelief(Character):
    """A character designed to provide humor and levity"""
    def __init__(self, gender=None):
        Character.__init__(self, gender)
        # Comic relief characters
        self.humorStyle = data.pick('character.humor_styles')
        self.comedySource = data.pick('character.comedy_sources')
        self.seriousMoment = data.pick('character.serious_depth')  # Every funny character needs depth

class Mentor(Character):
    """A wise character who guides others"""
    def __init__(self, gender=None):
        Character.__init__(self, gender)
        # Mentors are typically older and wiser
        self.age = random.randint(45, 80)
        self.wisdomSource = data.pick('character.wisdom_sources')
        self.teachingStyle = data.pick('character.teaching_methods')
        self.pastFailure = data.pick('character.mentor_failures')  # What they learned from

class LoveInterest(Character):
    """A character designed for romantic relationships"""
    def __init__(self, gender=None):
        Character.__init__(self, gender)
        # Love interests have specific romantic qualities
        self.romanticAppeal = data.pick('character.romantic_qualities')
        self.relationshipStyle = data.pick('character.romantic_styles')
        self.romanticConflict = data.pick('character.romantic_conflicts')