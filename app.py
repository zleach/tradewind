import os
import random
from flask import Flask, render_template, send_from_directory, jsonify
from flask import request, url_for

from app import ships
from app import people
from app import characters
from app import names

# initialization
app = Flask(__name__)

# Enable CORS for all origins on all API routes
try:
    from flask_cors import CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})
except ImportError:
    # If flask-cors isn't installed in the runtime environment, the API will still run
    # but CORS headers won't be added. Ensure flask-cors is listed in requirements.txt
    pass

app.config.update(
    DEBUG = True,
)

@app.route('/')
def content():


    if request.args.get('prefix'):
        prefix = request.args.get('prefix');
    else:
        prefix = "USS"

    if request.args.get('type'):
        shipType = int(request.args.get('type'))
    else:
        shipType = 0

    if request.args.get('genderMix'):
        genderMix = int(request.args.get('genderMix'))
    else:
        genderMix = 50

    defaultCrewSize = .25
    if request.args.get('crewSize'):
        crewSize = float(request.args.get('crewSize'))/4
        if crewSize > 5:
            crewSize = defaultCrewSize
    else:
        crewSize = defaultCrewSize
    
      
    ship = ships.Ship(prefix,shipType,crewSize)
    types = ships.ship['type']

    return render_template('base.tpl', types=types,ship=ship,request=request,prefix=prefix,shipType=shipType,genderMix=genderMix,crewSize=crewSize)

def render_person_text(person):
    """Generate the same formatted text as shown in the UI"""
    # First paragraph: personality, age, appearance
    age_text = f"{person.age}-year-old " if hasattr(person, 'age') and person.age else ""
    text = f"{person.personality} {age_text}{person.genderPronoun} has {person.eyecolor} eyes, a {person.skincolor} complexion, and {person.hairtype} {person.haircolor} hair {person.hairstyle}."
    
    # Second paragraph: height, build, origin
    text += f" {person.genderTitle.capitalize()} is {person.height} and {person.build}. {person.genderTitle.capitalize()} {person.birthPlace}."
    
    # Previous service if applicable
    if person.previousService and hasattr(person, 'rank') and not callable(person.rank):
        text += f" {person.rank.title} {person.lastName} previously served aboard the USS {person.previousService}."
    
    return text

def person_to_dict(person):
    """Convert a person object to a dictionary for JSON serialization"""
    result = {
        'firstName': person.firstName,
        'lastName': person.lastName,
        'gender': person.gender,
        'genderTitle': person.genderTitle,
        'genderPronoun': person.genderPronoun,
        'genderPossessive': person.genderPossessive,
        'personality': str(person.personality),
        'eyecolor': person.eyecolor,
        'skincolor': person.skincolor,
        'hairtype': person.hairtype,
        'haircolor': person.haircolor,
        'hairstyle': person.hairstyle,
        'height': person.height,
        'build': person.build,
        'birthPlace': person.birthPlace,
        'age': person.age if hasattr(person, 'age') else None,
        'previousService': person.previousService if person.previousService else None,
        'renderedText': render_person_text(person),
    }
    
    # Add rank information if available
    if hasattr(person, 'rank') and not callable(person.rank):
        result['rank'] = {
            'abbreviation': person.rank.abbrivation,
            'title': person.rank.title,
            'designation': person.rank.designation,
            'order': person.rank.order
        }
    
    # Add callsign for pilots
    if hasattr(person, 'callsign'):
        result['callsign'] = person.callsign
    
    # Add person type
    result['type'] = type(person).__name__
    
    return result

def render_character_text(character):
    """Generate formatted text for character as it would appear in a story context"""
    # Character description focusing on personality and motivation
    age_text = f"{character.age}-year-old " if character.age else ""
    text = f"{character.firstName} {character.lastName} is a {age_text}{character.genderPronoun} who {character.primaryMotivation}. "
    
    # Core personality and flaws
    text += f"{character.genderTitle.capitalize()} is {character.positiveTraits} but {character.coreFlaws}. "
    
    # Key background elements
    text += f"{character.genderTitle.capitalize()} {character.birthPlace} and works as a {character.occupation}. "
    
    # Emotional/relationship core
    text += f"{character.genderTitle.capitalize()} {character.emotionalCore} and {character.relationshipStyle}. "
    
    # Fear and internal conflict
    text += f"Deep down, {character.genderTitle} {character.fears} and {character.internalConflict}."
    
    return text

def character_to_dict(character):
    """Convert a character object to a dictionary for JSON serialization"""
    result = {
        'firstName': character.firstName,
        'lastName': character.lastName,
        'age': character.age,
        'gender': character.gender,
        'genderTitle': character.genderTitle,
        'genderPronoun': character.genderPronoun,
        'genderPossessive': character.genderPossessive,
        
        # Physical appearance
        'eyecolor': character.eyecolor,
        'skincolor': character.skincolor,
        'hairtype': character.hairtype,
        'haircolor': character.haircolor,
        'hairstyle': character.hairstyle,
        'height': character.height,
        'build': character.build,
        
        # Character development core
        'primaryMotivation': character.primaryMotivation,
        'coreFlaws': character.coreFlaws,
        'fears': character.fears,
        'secret': character.secret,
        'moralAlignment': character.moralAlignment,
        'emotionalCore': character.emotionalCore,
        
        # Background
        'socioeconomicBackground': character.socioeconomicBackground,
        'educationLevel': character.educationLevel,
        'occupation': character.occupation,
        'familyBackground': character.familyBackground,
        'formativeExperience': character.formativeExperience,
        'birthPlace': character.birthPlace,
        
        # Skills and abilities
        'primarySkill': character.primarySkill,
        'hiddenTalent': character.hiddenTalent,
        
        # Relationships and goals
        'relationshipStyle': character.relationshipStyle,
        'trustIssues': character.trustIssues,
        'shortTermGoal': character.shortTermGoal,
        'longTermGoal': character.longTermGoal,
        'internalConflict': character.internalConflict,
        
        # Personality
        'positiveTraits': character.positiveTraits,
        'quirks': character.quirks,
        
        # Meta information
        'type': type(character).__name__,
        'renderedText': render_character_text(character),
    }
    
    # Add specialized fields based on character type
    if hasattr(character, 'heroicFlaw'):
        result['heroicFlaw'] = character.heroicFlaw
        result['characterArc'] = character.characterArc
        result['callToAdventure'] = character.callToAdventure
        result['mentalToughness'] = character.mentalToughness
    
    if hasattr(character, 'corruptionSource'):
        result['corruptionSource'] = character.corruptionSource
        result['redeemedQuality'] = character.redeemedQuality
        result['methodOfControl'] = character.methodOfControl
    
    if hasattr(character, 'relationshipRole'):
        result['relationshipRole'] = character.relationshipRole
        result['loyaltyLevel'] = character.loyaltyLevel
        result['supportType'] = character.supportType
    
    if hasattr(character, 'humorStyle'):
        result['humorStyle'] = character.humorStyle
        result['comedySource'] = character.comedySource
        result['seriousMoment'] = character.seriousMoment
    
    if hasattr(character, 'wisdomSource'):
        result['wisdomSource'] = character.wisdomSource
        result['teachingStyle'] = character.teachingStyle
        result['pastFailure'] = character.pastFailure
    
    if hasattr(character, 'romanticAppeal'):
        result['romanticAppeal'] = character.romanticAppeal
        result['romanticConflict'] = character.romanticConflict
    
    return result

@app.route('/api/characters', methods=['GET'])
def api_characters_info():
    """Provide API documentation for character generation"""
    return jsonify({
        'endpoint': '/api/characters',
        'description': 'Generate complex characters for storytelling and creative writing',
        'methods': ['POST'],
        'parameters': {
            'count': {
                'type': 'integer',
                'description': 'Number of characters to generate (1-50)',
                'default': 1,
                'required': False
            },
            'gender': {
                'type': 'string',
                'description': 'Gender of generated characters',
                'options': ['male', 'female', None],
                'default': None,
                'note': 'null means random gender',
                'required': False
            },
            'type': {
                'type': 'string', 
                'description': 'Type of character to generate',
                'options': ['Character', 'Protagonist', 'Antagonist', 'SupportingCharacter', 'ComicRelief', 'Mentor', 'LoveInterest'],
                'default': 'Character',
                'required': False
            }
        },
        'example_request': {
            'count': 2,
            'gender': 'female',
            'type': 'Protagonist'
        },
        'response_format': {
            'characters': 'array of character objects',
            'count': 'number of characters generated',
            'parameters': 'parameters used for generation'
        },
        'character_object_fields': {
            'firstName': 'First name',
            'lastName': 'Last name',
            'age': 'Age in years',
            'gender': 'Gender (male/female)',
            'primaryMotivation': 'Core driving motivation',
            'coreFlaws': 'Character flaws and weaknesses',
            'fears': 'Deepest fears',
            'secret': 'Hidden secret',
            'moralAlignment': 'Moral philosophy and values',
            'emotionalCore': 'Emotional patterns and traits',
            'socioeconomicBackground': 'Economic and social background',
            'educationLevel': 'Educational background',
            'occupation': 'Current job or profession',
            'familyBackground': 'Family history and dynamics',
            'formativeExperience': 'Life-shaping experience',
            'primarySkill': 'Main talent or ability',
            'hiddenTalent': 'Secret skill or ability',
            'relationshipStyle': 'How they approach relationships',
            'trustIssues': 'Trust patterns and issues',
            'shortTermGoal': 'Immediate objective',
            'longTermGoal': 'Life goal or ambition',
            'internalConflict': 'Core internal struggle',
            'positiveTraits': 'Strengths and virtues',
            'quirks': 'Unique behavioral traits',
            'birthPlace': 'Place of origin',
            'renderedText': 'Full character summary for storytelling',
            'type': 'Character archetype'
        },
        'character_types': {
            'Character': 'Base character with full development',
            'Protagonist': 'Main character with hero\'s journey elements',
            'Antagonist': 'Opposing character with compelling motivations',
            'SupportingCharacter': 'Supporting role with specific relationship function',
            'ComicRelief': 'Humorous character with hidden depth',
            'Mentor': 'Wise guide character with teaching abilities',
            'LoveInterest': 'Romantic character with relationship dynamics'
        },
        'use_cases': [
            'Novel and short story character development',
            'Screenplay and script writing',
            'Tabletop RPG character creation',
            'Creative writing exercises',
            'Character-driven story planning',
            'Writing workshop prompts'
        ]
    })

@app.route('/api/characters', methods=['POST'])
def api_characters():
    """Generate characters for creative writing based on JSON parameters"""
    try:
        # Get JSON data from request
        data = request.get_json()
        if not data:
            data = {}
        
        # Parse parameters with defaults
        count = data.get('count', 1)
        gender = data.get('gender', None)  # None means random
        character_type = data.get('type', 'Character')  # Default to basic Character
        
        # Validate count (lower limit for characters since they're more complex)
        if not isinstance(count, int) or count < 1 or count > 50:
            return jsonify({'error': 'Count must be an integer between 1 and 50'}), 400
        
        # Validate gender
        if gender and gender not in ['male', 'female']:
            return jsonify({'error': 'Gender must be "male", "female", or null for random'}), 400
        
        # Validate character type
        valid_types = ['Character', 'Protagonist', 'Antagonist', 'SupportingCharacter', 'ComicRelief', 'Mentor', 'LoveInterest']
        if character_type not in valid_types:
            return jsonify({'error': f'Type must be one of: {", ".join(valid_types)}'}), 400
        
        # Generate characters
        generated_characters = []
        for _ in range(count):
            # Get the appropriate class
            character_class = getattr(characters, character_type)
            
            # Create character instance with specified gender
            character = character_class(gender=gender)
            
            # Convert to dictionary and add to results
            generated_characters.append(character_to_dict(character))
        
        return jsonify({
            'characters': generated_characters,
            'count': len(generated_characters),
            'parameters': {
                'requested_count': count,
                'gender': gender,
                'type': character_type
            }
        })
        
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/people', methods=['GET'])
def api_people_info():
    """Provide API documentation and available options"""
    return jsonify({
        'endpoint': '/api/people',
        'description': 'Generate random people with specified parameters',
        'methods': ['POST'],
        'parameters': {
            'count': {
                'type': 'integer',
                'description': 'Number of people to generate (1-100)',
                'default': 1,
                'required': False
            },
            'gender': {
                'type': 'string',
                'description': 'Gender of generated people',
                'options': ['male', 'female', None],
                'default': None,
                'note': 'null means random gender',
                'required': False
            },
            'type': {
                'type': 'string', 
                'description': 'Type of person to generate',
                'options': ['Person', 'Officer', 'Enlisted', 'Pilot', 'HighRankOfficer', 'Commander', 'Marine'],
                'default': 'Person',
                'required': False
            }
        },
        'example_request': {
            'count': 3,
            'gender': 'female',
            'type': 'Officer'
        },
        'response_format': {
            'people': 'array of person objects',
            'count': 'number of people generated',
            'parameters': 'parameters used for generation'
        },
        'person_object_fields': {
            'firstName': 'First name',
            'lastName': 'Last name', 
            'gender': 'Gender (male/female)',
            'personality': 'Personality description',
            'age': 'Age (for military personnel)',
            'rank': 'Military rank object (for military personnel)',
            'callsign': 'Pilot callsign (for pilots)',
            'eyecolor': 'Eye color',
            'haircolor': 'Hair color',
            'hairstyle': 'Hair style',
            'hairtype': 'Hair type',
            'skincolor': 'Skin color',
            'height': 'Height description',
            'build': 'Build description',
            'birthPlace': 'Place of birth/origin',
            'previousService': 'Previous military service',
            'renderedText': 'Full formatted description as shown in UI',
            'type': 'Person type (Person, Officer, Pilot, etc.)'
        }
    })

@app.route('/api/people', methods=['POST'])
def api_people():
    """Generate people based on JSON parameters"""
    try:
        # Get JSON data from request
        data = request.get_json()
        if not data:
            data = {}
        
        # Parse parameters with defaults
        count = data.get('count', 1)
        gender = data.get('gender', None)  # None means random
        person_type = data.get('type', 'Person')  # Default to basic Person
        
        # Validate count
        if not isinstance(count, int) or count < 1 or count > 100:
            return jsonify({'error': 'Count must be an integer between 1 and 100'}), 400
        
        # Validate gender
        if gender and gender not in ['male', 'female']:
            return jsonify({'error': 'Gender must be "male", "female", or null for random'}), 400
        
        # Validate person type
        valid_types = ['Person', 'Officer', 'Enlisted', 'Pilot', 'HighRankOfficer', 'Commander', 'Marine']
        if person_type not in valid_types:
            return jsonify({'error': f'Type must be one of: {", ".join(valid_types)}'}), 400
        
        # Generate people
        generated_people = []
        for _ in range(count):
            # Get the appropriate class
            person_class = getattr(people, person_type)
            
            # Create person instance with specified gender
            person = person_class(gender=gender)
            
            # Convert to dictionary and add to results
            generated_people.append(person_to_dict(person))
        
        return jsonify({
            'people': generated_people,
            'count': len(generated_people),
            'parameters': {
                'requested_count': count,
                'gender': gender,
                'type': person_type
            }
        })
        
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/names', methods=['GET'])
def api_names():
    """Generate simple names with optional count and gender"""
    try:
        # Get query parameters
        count = request.args.get('count', 1, type=int)
        gender = request.args.get('gender')
        
        # Validate count
        if count < 1 or count > 100:
            return jsonify({'error': 'Count must be between 1 and 100'}), 400
        
        # Validate gender
        if gender and gender not in ['male', 'female']:
            return jsonify({'error': 'Gender must be "male", "female", or omitted for random'}), 400
        
        # Generate names
        generated_names = []
        for _ in range(count):
            # If no gender specified, pick one randomly for this name
            name_gender = gender if gender else ('male' if random.randint(0, 1) else 'female')
            first_name = names.get_first_name(name_gender)
            last_name = names.get_last_name()
            generated_names.append({
                'firstName': first_name,
                'lastName': last_name,
                'fullName': f"{first_name} {last_name}",
                'gender': name_gender
            })
        
        return jsonify({
            'names': generated_names,
            'count': len(generated_names),
            'parameters': {
                'requested_count': count,
                'gender': gender
            }
        })
        
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)