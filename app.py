import os
from flask import Flask, render_template, send_from_directory
from flask import request, url_for

from app import ships

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

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)