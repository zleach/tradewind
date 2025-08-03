# Tradewind Character & People Generator API

Generate names, detailed character profiles for creative writing, and sci-fi military personnel with the Tradewind API.

## Base URL

```
https://tradewindgen.com
```

## Authentication

No authentication required. The API is free to use.

## Endpoints

### Characters API (For Writers & Authors)

#### GET /api/characters

Returns API documentation and available character types for creative writing.

**Response:**

```json
{
  "endpoint": "/api/characters",
  "description": "Generate complex characters for storytelling and creative writing",
  "character_types": {
    "Character": "Base character with full development",
    "Protagonist": "Main character with hero's journey elements",
    "Antagonist": "Opposing character with compelling motivations",
    "SupportingCharacter": "Supporting role with specific relationship function",
    "ComicRelief": "Humorous character with hidden depth",
    "Mentor": "Wise guide character with teaching abilities",
    "LoveInterest": "Romantic character with relationship dynamics"
  }
}
```

#### POST /api/characters

Generate complex characters for creative writing with deep psychological profiles.

**Request Body:**

```json
{
  "count": 2,
  "gender": "female",
  "type": "Protagonist"
}
```

**Response:**

```json
{
  "characters": [
    {
      "firstName": "Sarah",
      "lastName": "Chen",
      "age": 28,
      "primaryMotivation": "seeking to prove their worth to those who doubted them",
      "coreFlaws": "unable to trust anyone completely and chronically late",
      "fears": "being abandoned by everyone they love",
      "secret": "witnessed a crime but never reported it",
      "occupation": "emergency room doctor or nurse",
      "heroicFlaw": "too willing to sacrifice themselves for others",
      "characterArc": "learning to trust others despite past betrayals",
      "renderedText": "Sarah Chen is a 28-year-old woman who seeking to prove their worth...",
      "type": "Protagonist"
    }
  ],
  "count": 1
}
```

### Names API (Simple Name Generation)

#### GET /api/names

Generate simple names with optional parameters. Uses query parameters instead of JSON body.

**Query Parameters:**

- `count` (optional): Number of names to generate (1-100, default: 1)
- `gender` (optional): Gender for names ("male", "female", or omitted for random)

**Examples:**

```bash
# Single random name
GET /api/names

# 5 female names
GET /api/names?count=5&gender=female

# 3 random gender names
GET /api/names?count=3
```

**Response:**

```json
{
  "names": [
    {
      "firstName": "Sarah",
      "lastName": "Johnson",
      "fullName": "Sarah Johnson",
      "gender": "female"
    }
  ],
  "count": 1,
  "parameters": {
    "requested_count": 1,
    "gender": null
  }
}
```

### Military Personnel API (For Sci-Fi & Gaming)

#### GET /api/people

Returns API documentation and available options.

**Response:**

```json
{
  "endpoint": "/api/people",
  "description": "Generate random people with specified parameters",
  "methods": ["POST"],
  "parameters": { ... },
  "person_object_fields": { ... }
}
```

### POST /api/people

Generate people based on specified parameters.

**Request Body:**

```json
{
  "count": 3,
  "gender": "female",
  "type": "Officer"
}
```

**Response:**

```json
{
  "people": [ ... ],
  "count": 3,
  "parameters": {
    "requested_count": 3,
    "gender": "female",
    "type": "Officer"
  }
}
```

## Parameters

### Character API Parameters

| Parameter | Type    | Required | Default     | Description                                                      |
| --------- | ------- | -------- | ----------- | ---------------------------------------------------------------- |
| `count`   | integer | No       | 1           | Number of characters to generate (1-50)                          |
| `gender`  | string  | No       | null        | Gender specification: `"male"`, `"female"`, or `null` for random |
| `type`    | string  | No       | "Character" | Type of character to generate                                    |

### People API Parameters

| Parameter | Type    | Required | Default  | Description                                                      |
| --------- | ------- | -------- | -------- | ---------------------------------------------------------------- |
| `count`   | integer | No       | 1        | Number of people to generate (1-100)                             |
| `gender`  | string  | No       | null     | Gender specification: `"male"`, `"female"`, or `null` for random |
| `type`    | string  | No       | "Person" | Type of person to generate                                       |

### Available Character Types

| Type                  | Description                                          |
| --------------------- | ---------------------------------------------------- |
| `Character`           | Base character with full psychological profile       |
| `Protagonist`         | Main character with hero's journey elements          |
| `Antagonist`          | Compelling villain with understandable motives       |
| `SupportingCharacter` | Supporting role with specific relationship function  |
| `ComicRelief`         | Humorous character with hidden emotional depth       |
| `Mentor`              | Wise guide with teaching abilities and past failures |
| `LoveInterest`        | Romantic character with relationship dynamics        |

### Available Person Types (Military)

| Type              | Description                   |
| ----------------- | ----------------------------- |
| `Person`          | Basic civilian character      |
| `Officer`         | Military officer with rank    |
| `Enlisted`        | Enlisted military personnel   |
| `Pilot`           | Military pilot with callsign  |
| `HighRankOfficer` | High-ranking military officer |
| `Commander`       | Military commander            |
| `Marine`          | Marine corps personnel        |

## Response Format

### Character Object Fields

Each character object contains comprehensive psychological and background information:

| Field                     | Type    | Description                                 |
| ------------------------- | ------- | ------------------------------------------- |
| `firstName`               | string  | First name                                  |
| `lastName`                | string  | Last name                                   |
| `age`                     | integer | Age in years (16-85)                        |
| `gender`                  | string  | Gender (`"male"` or `"female"`)             |
| `primaryMotivation`       | string  | Core driving motivation and life goal       |
| `coreFlaws`               | string  | 1-3 character flaws and weaknesses          |
| `fears`                   | string  | Deepest fears and anxieties                 |
| `secret`                  | string  | Hidden secret that could impact their story |
| `moralAlignment`          | string  | Moral philosophy and ethical framework      |
| `emotionalCore`           | string  | Emotional patterns and traits               |
| `socioeconomicBackground` | string  | Economic and social background              |
| `educationLevel`          | string  | Educational background and learning         |
| `occupation`              | string  | Current job or profession                   |
| `familyBackground`        | string  | Family history and dynamics                 |
| `formativeExperience`     | string  | Life-shaping experience or trauma           |
| `primarySkill`            | string  | Main talent or professional ability         |
| `hiddenTalent`            | string  | Secret skill or undiscovered ability        |
| `relationshipStyle`       | string  | How they approach relationships             |
| `trustIssues`             | string  | Trust patterns and relationship barriers    |
| `shortTermGoal`           | string  | Immediate objective or need                 |
| `longTermGoal`            | string  | Life goal or major ambition                 |
| `internalConflict`        | string  | Core internal struggle or contradiction     |
| `positiveTraits`          | string  | 2-4 strengths and virtues                   |
| `quirks`                  | string  | Unique behavioral traits or habits          |
| `birthPlace`              | string  | Place of origin (sci-fi setting)            |
| `renderedText`            | string  | **Full character summary for storytelling** |
| `type`                    | string  | Character archetype                         |

#### Specialized Character Fields

**Protagonist characters also include:**

- `heroicFlaw`: Fatal flaw that creates character growth
- `characterArc`: Character development journey
- `callToAdventure`: Event that starts their story
- `mentalToughness`: Source of inner strength

**Antagonist characters also include:**

- `corruptionSource`: What turned them toward darkness
- `redeemedQuality`: Positive trait that makes them relatable
- `methodOfControl`: How they manipulate or control others

**Supporting characters include relationship dynamics, comic relief characters include humor styles, mentors include wisdom sources, and love interests include romantic qualities.**

### Person Object Fields (Military)

Each person object contains the following fields:

| Field              | Type          | Description                                       |
| ------------------ | ------------- | ------------------------------------------------- |
| `firstName`        | string        | First name                                        |
| `lastName`         | string        | Last name                                         |
| `gender`           | string        | Gender (`"male"` or `"female"`)                   |
| `genderTitle`      | string        | Gender pronoun (`"he"` or `"she"`)                |
| `genderPronoun`    | string        | Gender noun (`"man"` or `"woman"`)                |
| `genderPossessive` | string        | Possessive pronoun (`"his"` or `"her"`)           |
| `personality`      | string        | Personality trait description                     |
| `age`              | integer\|null | Age (available for military personnel)            |
| `eyecolor`         | string        | Eye color                                         |
| `haircolor`        | string        | Hair color                                        |
| `hairstyle`        | string        | Hair style description                            |
| `hairtype`         | string        | Hair type (straight, curly, etc.)                 |
| `skincolor`        | string        | Skin color/complexion                             |
| `height`           | string        | Height description                                |
| `build`            | string        | Build/body type description                       |
| `birthPlace`       | string        | Place of birth/origin                             |
| `previousService`  | string\|null  | Previous military service                         |
| `rank`             | object\|null  | Military rank information (for military types)    |
| `callsign`         | string\|null  | Pilot callsign (for pilots only)                  |
| `type`             | string        | Person type                                       |
| `renderedText`     | string        | **Full formatted description as displayed in UI** |

### Rank Object (for military personnel)

```json
{
  "abbreviation": "LT",
  "title": "Lieutenant",
  "designation": "O-3",
  "order": 13
}
```

## Examples

### Character Generation Examples

#### Generate a Complex Protagonist

**Request:**

```bash
curl -X POST https://tradewindgen.com/api/characters \
  -H "Content-Type: application/json" \
  -d '{"count": 1, "type": "Protagonist"}'
```

**Response:**

```json
{
  "count": 1,
  "characters": [
    {
      "firstName": "Elena",
      "lastName": "Rodriguez",
      "age": 32,
      "gender": "female",
      "primaryMotivation": "seeking to prove their worth to those who doubted them",
      "coreFlaws": "unable to trust anyone completely and prone to self-destructive behavior",
      "fears": "being abandoned by everyone they love",
      "secret": "was responsible for someone's death",
      "moralAlignment": "believes in redemption for everyone",
      "emotionalCore": "bottles up emotions until they explode",
      "occupation": "detective or private investigator",
      "familyBackground": "raised by a single parent who sacrificed everything",
      "formativeExperience": "witnessed an injustice they couldn't prevent",
      "primarySkill": "exceptional at reading people's motivations",
      "hiddenTalent": "can detect lies with unusual accuracy",
      "shortTermGoal": "find evidence to prove someone's innocence",
      "longTermGoal": "break the cycle of dysfunction in their family",
      "internalConflict": "wants to help others but struggles to help themselves",
      "heroicFlaw": "too willing to sacrifice themselves for others",
      "characterArc": "learning to trust others despite past betrayals",
      "callToAdventure": "finds evidence of a conspiracy that affects everyone",
      "renderedText": "Elena Rodriguez is a 32-year-old woman who seeking to prove their worth to those who doubted them. She is incredibly resilient in the face of adversity and shows exceptional kindness to strangers but unable to trust anyone completely and prone to self-destructive behavior. She was raised by a single parent who sacrificed everything and works as a detective or private investigator. She bottles up emotions until they explode and attracts people who need fixing. Deep down, she being abandoned by everyone they love and wants to help others but struggles to help themselves.",
      "type": "Protagonist"
    }
  ]
}
```

#### Generate a Compelling Antagonist

**Request:**

```bash
curl -X POST https://tradewindgen.com/api/characters \
  -H "Content-Type: application/json" \
  -d '{"count": 1, "type": "Antagonist", "gender": "male"}'
```

**Response:**

```json
{
  "count": 1,
  "characters": [
    {
      "firstName": "Victor",
      "lastName": "Sterling",
      "age": 45,
      "primaryMotivation": "convinced their harsh methods serve the greater good",
      "coreFlaws": "manipulative and controlling in relationships",
      "corruptionSource": "believes the world is fundamentally unfair and cruel",
      "redeemedQuality": "demonstrates remarkable courage when needed",
      "methodOfControl": "uses others' guilt and shame against them",
      "occupation": "therapist helping trauma victims",
      "renderedText": "Victor Sterling is a 45-year-old man who convinced their harsh methods serve the greater good. He demonstrates remarkable courage when needed but manipulative and controlling in relationships. He was abandoned as a child and never told anyone and works as a therapist helping trauma victims...",
      "type": "Antagonist"
    }
  ]
}
```

### Military Personnel Examples

#### Generate a Single Random Person

**Request:**

```bash
curl -X POST https://tradewindgen.com/api/people \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Response:**

```json
{
  "count": 1,
  "parameters": {
    "requested_count": 1,
    "gender": null,
    "type": "Person"
  },
  "people": [
    {
      "firstName": "Mark",
      "lastName": "Ault",
      "gender": "male",
      "personality": "confident and maternal but shy",
      "eyecolor": "brown",
      "haircolor": "brown",
      "hairstyle": "in a military standard cut",
      "hairtype": "thick",
      "skincolor": "rosy",
      "height": "short",
      "build": "skinny",
      "birthPlace": "was born on a frontier colony on Ara V",
      "age": null,
      "previousService": null,
      "type": "Person",
      "renderedText": "confident and maternal but shy man has brown eyes, a rosy complexion, and thick brown hair in a military standard cut. He is short and skinny. He was born on a frontier colony on Ara V."
    }
  ]
}
```

### Generate Multiple Female Officers

**Request:**

```bash
curl -X POST https://tradewindgen.com/api/people \
  -H "Content-Type: application/json" \
  -d '{"count": 2, "gender": "female", "type": "Officer"}'
```

**Response:**

```json
{
  "count": 2,
  "parameters": {
    "requested_count": 2,
    "gender": "female",
    "type": "Officer"
  },
  "people": [
    {
      "firstName": "Sofia",
      "lastName": "Marroguin",
      "gender": "female",
      "age": 49,
      "rank": {
        "abbreviation": "LT",
        "title": "Lieutenant",
        "designation": "O-3",
        "order": 13
      },
      "personality": "reverential",
      "eyecolor": "hazel",
      "haircolor": "strawberry blonde",
      "hairstyle": "worn loose about the shoulders",
      "hairtype": "curly",
      "skincolor": "freckled",
      "height": "tall",
      "build": "of average weight",
      "birthPlace": "is originally from the isolated city of Uskilia VII",
      "previousService": null,
      "type": "Officer",
      "renderedText": "reverential 49-year-old woman has hazel eyes, a freckled complexion, and curly strawberry blonde hair worn loose about the shoulders. She is tall and of average weight. She is originally from the isolated city of Uskilia VII."
    }
  ]
}
```

### Generate Pilots with Callsigns

**Request:**

```bash
curl -X POST https://tradewindgen.com/api/people \
  -H "Content-Type: application/json" \
  -d '{"count": 2, "type": "Pilot"}'
```

**Response:**

```json
{
  "count": 2,
  "people": [
    {
      "firstName": "Robert",
      "lastName": "Williams",
      "gender": "male",
      "callsign": "Dong",
      "rank": {
        "abbreviation": "LCDR",
        "title": "Lieutenant Commander",
        "designation": "O-4",
        "order": 14
      },
      "age": 22,
      "personality": "dramatic but opinionated",
      "renderedText": "dramatic but opinionated 22-year-old man has brown eyes, a freckled complexion, and thick jet black hair cut regular. He is very short and well-built. He is from Ildecia Colony on Canes.",
      "type": "Pilot"
    }
  ]
}
```

## Error Handling

The API returns appropriate HTTP status codes and error messages:

### 400 Bad Request

**Invalid count:**

```json
{
  "error": "Count must be an integer between 1 and 100"
}
```

**Invalid gender:**

```json
{
  "error": "Gender must be \"male\", \"female\", or null for random"
}
```

**Invalid type:**

```json
{
  "error": "Type must be one of: Person, Officer, Enlisted, Pilot, HighRankOfficer, Commander, Marine"
}
```

### 500 Internal Server Error

```json
{
  "error": "Internal server error: [error description]"
}
```

## Rate Limiting

Currently no rate limiting is enforced, but please use the API responsibly.

## Use Cases

### Character API Use Cases

- **Novel Writing**: Generate complex protagonists, antagonists, and supporting characters
- **Screenwriting**: Create compelling characters with clear motivations and arcs
- **Creative Writing Workshops**: Generate character prompts and development exercises
- **Tabletop RPGs**: Create NPCs with deep psychological profiles
- **Character Development**: Explore personality traits, flaws, and growth potential
- **Writing Exercises**: Generate characters for short stories and creative prompts

### People API Use Cases

- **Sci-Fi Game Development**: Generate military NPCs with ranks and backgrounds
- **Military Fiction**: Create authentic-feeling military personnel
- **Space Opera Writing**: Generate ship crews and military characters
- **Gaming Applications**: Populate sci-fi universes with detailed personnel
- **Testing & Development**: Generate realistic character data for applications

## Integration Examples

### JavaScript/Node.js

#### Simple Names Generation

```javascript
async function generateNames(count = 1, gender = null) {
  const params = new URLSearchParams();
  if (count > 1) params.append("count", count);
  if (gender) params.append("gender", gender);

  const url = `https://tradewindgen.com/api/names${
    params.toString() ? "?" + params.toString() : ""
  }`;
  const response = await fetch(url);
  const data = await response.json();
  return data.names;
}

// Usage examples
generateNames().then((names) => {
  console.log(`Random name: ${names[0].fullName}`);
});

generateNames(5, "female").then((names) => {
  names.forEach((name) => {
    console.log(`${name.firstName} ${name.lastName}`);
  });
});
```

#### Character Generation for Writers

```javascript
async function generateCharacters(count = 1, type = "Character") {
  const response = await fetch("https://tradewindgen.com/api/characters", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      count: count,
      type: type,
    }),
  });

  const data = await response.json();
  return data.characters;
}

// Generate a protagonist for your story
generateCharacters(1, "Protagonist").then((characters) => {
  const protagonist = characters[0];
  console.log(`${protagonist.firstName} ${protagonist.lastName}`);
  console.log(`Motivation: ${protagonist.primaryMotivation}`);
  console.log(`Flaws: ${protagonist.coreFlaws}`);
  console.log(`Character Arc: ${protagonist.characterArc}`);
  console.log(`\nFull Description:\n${protagonist.renderedText}`);
});

// Generate supporting cast
generateCharacters(3, "SupportingCharacter").then((characters) => {
  characters.forEach((character) => {
    console.log(`${character.firstName}: ${character.relationshipRole}`);
  });
});
```

#### Military Personnel Generation

```javascript
async function generateOfficers(count = 3) {
  const response = await fetch("https://tradewindgen.com/api/people", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      count: count,
      type: "Officer",
    }),
  });

  const data = await response.json();
  return data.people;
}

// Usage
generateOfficers(5).then((officers) => {
  officers.forEach((officer) => {
    console.log(
      `${officer.rank.abbreviation} ${officer.firstName} ${officer.lastName}`
    );
    console.log(officer.renderedText);
  });
});
```

### Python

#### Simple Names Generation

```python
import requests

def generate_names(count=1, gender=None):
    url = 'https://tradewindgen.com/api/names'
    params = {}
    if count > 1:
        params['count'] = count
    if gender:
        params['gender'] = gender

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()['names']

# Usage examples
names = generate_names()
print(f"Random name: {names[0]['fullName']}")

female_names = generate_names(count=3, gender='female')
for name in female_names:
    print(f"{name['firstName']} {name['lastName']}")
```

#### Character Generation for Writers

```python
import requests

def generate_characters(count=1, gender=None, character_type='Character'):
    url = 'https://tradewindgen.com/api/characters'
    payload = {
        'count': count,
        'type': character_type
    }
    if gender:
        payload['gender'] = gender

    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()['characters']

# Generate a complex antagonist
antagonists = generate_characters(count=1, character_type='Antagonist')
for villain in antagonists:
    print(f"Name: {villain['firstName']} {villain['lastName']}")
    print(f"Motivation: {villain['primaryMotivation']}")
    print(f"Corruption: {villain['corruptionSource']}")
    print(f"Control Method: {villain['methodOfControl']}")
    print(f"\nFull Profile:\n{villain['renderedText']}")

# Generate a complete supporting cast
cast_types = ['Protagonist', 'Antagonist', 'SupportingCharacter', 'Mentor', 'LoveInterest']
for cast_type in cast_types:
    character = generate_characters(count=1, character_type=cast_type)[0]
    print(f"{cast_type}: {character['firstName']} {character['lastName']}")
```

#### Military Personnel Generation

```python
import requests

def generate_people(count=1, gender=None, person_type='Person'):
    url = 'https://tradewindgen.com/api/people'
    payload = {
        'count': count,
        'type': person_type
    }
    if gender:
        payload['gender'] = gender

    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()['people']

# Usage
pilots = generate_people(count=3, person_type='Pilot')
for pilot in pilots:
    print(f"{pilot['rank']['abbreviation']} {pilot['firstName']} \"{pilot['callsign']}\" {pilot['lastName']}")
    print(pilot['renderedText'])
```

### cURL

#### Names Generation

```bash
# Get a single random name
curl https://tradewindgen.com/api/names

# Get 5 female names
curl "https://tradewindgen.com/api/names?count=5&gender=female"

# Get 10 random names
curl "https://tradewindgen.com/api/names?count=10"
```

#### Character Generation

```bash
# Generate a protagonist with character arc
curl -X POST https://tradewindgen.com/api/characters \
  -H "Content-Type: application/json" \
  -d '{"count": 1, "type": "Protagonist"}' \
  | jq '.characters[0] | {name: (.firstName + " " + .lastName), motivation: .primaryMotivation, arc: .characterArc}'

# Generate a complex antagonist
curl -X POST https://tradewindgen.com/api/characters \
  -H "Content-Type: application/json" \
  -d '{"count": 1, "type": "Antagonist"}' \
  | jq '.characters[0] | {name: (.firstName + " " + .lastName), corruption: .corruptionSource, method: .methodOfControl}'

# Generate multiple supporting characters
curl -X POST https://tradewindgen.com/api/characters \
  -H "Content-Type: application/json" \
  -d '{"count": 3, "type": "SupportingCharacter"}' \
  | jq '.characters[] | {name: (.firstName + " " + .lastName), role: .relationshipRole}'
```

#### Military Personnel Generation

```bash
# Generate 5 random marines
curl -X POST https://tradewindgen.com/api/people \
  -H "Content-Type: application/json" \
  -d '{"count": 5, "type": "Marine"}' \
  | jq '.people[].renderedText'

# Generate 1 female pilot
curl -X POST https://tradewindgen.com/api/people \
  -H "Content-Type: application/json" \
  -d '{"count": 1, "gender": "female", "type": "Pilot"}' \
  | jq '.people[0]'
```

## Support

For questions, issues, or feature requests, please visit [tradewindgen.com](https://tradewindgen.com).

---

_The Tradewind API provides three generation services: **Names API** for simple name generation, **Characters API** for complex literary character development with psychological depth, motivations, and flaws perfect for writers and authors, and **People API** for detailed military personnel generation ideal for sci-fi applications and gaming. The character and people APIs include comprehensive background information, personality traits, and formatted narrative text._
