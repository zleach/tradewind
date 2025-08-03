import os
from flask import Flask, render_template, send_from_directory, jsonify
from flask import request, url_for

from app import ships
from app import people

# initialization
app = Flask(__name__)
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

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)