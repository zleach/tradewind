from os.path import abspath, join, dirname
import random


__title__ = 'names'
__version__ = '0.2'
__author__ = 'Trey Hunner'
__license__ = 'MIT'


full_path = lambda filename: abspath(join(dirname(__file__), filename))


FILES = {
    'callsign': full_path('dist.all.callsign'),
    'first:male': full_path('dist.male.first'),
    'first:female': full_path('dist.female.first'),
    'last': full_path('dist.all.last'),
    'ship:prefix': full_path('dist.ship.prefix'),
    'ship:name': full_path('dist.ship.name'),
    'ship:type': full_path('dist.ship.type'),
    'planet:name': full_path('dist.planet.name')
}


def get_name(filename):
    selected = random.random() * 90
    with open(filename) as name_file:
        for line in name_file:
            name, _, cummulative, _ = line.split()
            if float(cummulative) > selected:
                return name

def get_first_name(gender=None):
    if gender not in ('male', 'female'):
        gender = random.choice(('male', 'female'))
    return get_name(FILES['first:%s' % gender]).capitalize()


def get_last_name():
    return get_name(FILES['last']).capitalize()


def get_full_name(gender=None):
    return u"%s %s" % (get_first_name(gender), get_last_name())

def get_ship_name():
    filename = FILES['ship:name']
    with open(filename) as name_file:
      line = next(name_file)
      for num, aline in enumerate(name_file):
        if random.randrange(num + 2): continue
        line = aline
      return line

def get_planet_name():
    filename = FILES['planet:name']
    with open(filename) as name_file:
      line = next(name_file)
      for num, aline in enumerate(name_file):
        if random.randrange(num + 2): continue
        line = aline
      return line

def get_nick_name():
    filename = FILES['callsign']
    with open(filename) as name_file:
      line = next(name_file)
      for num, aline in enumerate(name_file):
        if random.randrange(num + 2): continue
        line = aline
      return line.strip()

def get_ship_type():
    identifier = {}
    identifier['name'] = "Unknown Type"
    identifier['code'] = "??"

    filename = FILES['ship:type']
    with open(filename) as name_file:
      line = next(name_file)
      for num, aline in enumerate(name_file):
        if random.randrange(num + 2): continue
        identifier['name'] = aline.split(",")[0]
        identifier['code'] = aline.split(",")[1]
        identifier['divisions'] = aline.split(",")[2].split(" ")
      return identifier
