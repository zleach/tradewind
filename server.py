from bottle import Bottle, route, run, request, template
from bottle import static_file

from app import ships

app = Bottle()

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')  

@app.route('/')
def content():

    try:
      prefix = request.params['prefix']
    except KeyError:
      prefix = "USS"
    
    try:
      shipType = int(request.params['type'])
    except KeyError:
      shipType = 0
    
    try:
      genderMix = int(request.params['genderMix'])
    except KeyError:
      genderMix = 50

    defaultCrewSize = .25
    try:
        requestedCrewSize = float(request.params['crewSize'])
        if requestedCrewSize > 6:
            print crewSize
            crewSize = defaultCrewSize
        else :
          crewSize = requestedCrewSize/4
    except KeyError:
      crewSize = defaultCrewSize
    
      
    ship = ships.Ship(prefix,shipType,crewSize)
    types = ships.ship['type']

    return template('base', types=types,ship=ship,request=request,prefix=prefix,shipType=shipType,genderMix=genderMix,crewSize=crewSize)
    
run(app, host='localhost', port=8080, debug=True, reloader=True)