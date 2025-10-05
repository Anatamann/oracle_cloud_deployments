import sqlite3
import random

connection = sqlite3.connect('messages.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

dares = [
    "I'm not saying I hate you, but I would unplug your life support to charge my phone.",
    "You're not lazy, you're just on energy-saving mode.",
    "I'm not a professional, but I can tell you're not one either.",
    "You have a unique way of seeing the world. It's wrong, but it's unique.",
    "I'd agree with you, but then we'd both be wrong.",
    "You're the reason the gene pool needs a lifeguard.",
    "I'm not ignoring you, I'm just prioritizing my sanity.",
    "I'm not saying you're stupid, I'm just saying you have bad luck when it comes to thinking.",
    "I'm not a doctor, but I'm pretty sure you have a case of the Mondays. On a Tuesday.",
    "You're not weird, you're a limited edition.",
    "I'm not saying you're old, but your birth certificate is an ancient scroll.",
    "You're not short, you're just fun-sized.",
    "I'm not saying you're a drama queen, but you could be the star of your own reality show.",
    "You're not a hot mess, you're a spicy disaster.",
    "I'm not saying you're a bad driver, but you could make a GPS cry.",
    "You're not a failure, you're just a work in progress.",
    "I'm not saying you're a control freak, but you could make a dictator take notes.",
    "You're not a know-it-all, you're just a Google search away from being one.",
    "I'm not saying you're a procrastinator, but you could make a sloth look productive.",
    "You're not a mess, you're a masterpiece of chaos.",
    "I'm not saying you're a bad cook, but you could make a fire alarm cheer for you.",
    "You're not a lost cause, you're just a scenic route to success.",
    "I'm not saying you're a bad singer, but you could make a dog howl in tune.",
    "You're not a joke, you're a whole comedy show.",
    "I'm not saying you're a bad dancer, but you could make a scarecrow look graceful.",
    "You're not a problem, you're a challenge.",
    "I'm not saying you're a bad listener, but you could make a wall talk back.",
    "You're not a weirdo, you're a collector of quirks.",
    "I'm not saying you're a bad artist, but you could make a stick figure look like a masterpiece.",
    "You're not a disaster, you're a beautiful catastrophe.",
    "I'm not saying you're a bad writer, but you could make a dictionary cry.",
    "You're not a fool, you're just a student of life.",
    "I'm not saying you're a bad actor, but you could make a tree look expressive.",
    "You're not a mess, you're a work of art in progress.",
    "I'm not saying you're a bad photographer, but you could make a selfie stick run away.",
    "You're not a failure, you're just a beta tester for life.",
    "I'm not saying you're a bad comedian, but you could make a clown cry.",
    "You're not a weirdo, you're a limited edition of yourself.",
    "I'm not saying you're a bad musician, but you could make a piano cry.",
    "You're not a disaster, you're a beautiful storm.",
    "I'm not saying you're a bad poet, but you could make a rose cry.",
    "You're not a fool, you're just a philosopher in training.",
    "I'm not saying you're a bad speaker, but you could make a microphone cry.",
    "You're not a mess, you're a beautiful chaos.",
    "I'm not saying you're a bad designer, but you could make a rainbow cry.",
    "You're not a failure, you're just a work in progress.",
    "I'm not saying you're a bad director, but you could make a movie cry.",
    "You're not a weirdo, you're a collector of eccentricities.",
    "I'm not saying you're a bad sculptor, but you could make a statue cry.",
    "You're not a disaster, you're a beautiful hurricane.",
    "I'm not saying you're a bad painter, but you could make a canvas cry.",
    "You're not a fool, you're just a student of the universe.",
    "I'm not saying you're a bad singer-songwriter, but you could make a guitar cry.",
    "You're not a mess, you're a beautiful whirlwind.",
    "I'm not saying you're a bad animator, but you could make a cartoon cry.",
    "You're not a failure, you're just a work in progress.",
    "I'm not saying you're a bad filmmaker, but you could make a camera cry.",
    "You're not a weirdo, you're a collector of oddities.",
    "I'm not saying you're a bad composer, but you could make an orchestra cry.",
    "You're not a disaster, you're a beautiful tornado.",
    "I'm not saying you're a bad illustrator, but you could make a comic book cry.",
    "You're not a fool, you're just a student of life's mysteries.",
    "I'm not saying you're a bad playwright, but you could make a stage cry.",
    "You're not a mess, you're a beautiful cyclone.",
    "I'm not saying you're a bad choreographer, but you could make a dancer cry.",
    "You're not a failure, you're just a work in progress.",
    "I'm not saying you're a bad fashion designer, but you could make a mannequin cry.",
    "You're not a weirdo, you're a collector of curiosities.",
    "I'm not saying you're a bad architect, but you could make a building cry.",
    "You're not a disaster, you're a beautiful typhoon.",
    "I'm not saying you're a bad interior designer, but you could make a room cry.",
    "You're not a fool, you're just a student of the human condition.",
    "I'm not saying you're a bad landscape architect, but you could make a garden cry.",
    "You're not a mess, you're a beautiful maelstrom.",
    "I'm not saying you're a bad graphic designer, but you could make a logo cry.",
    "You're not a failure, you're just a work in progress.",
    "I'm not saying you're a bad web designer, but you could make a website cry.",
    "You're not a weirdo, you're a collector of anomalies.",
    "I'm not saying you're a bad game designer, but you could make a video game cry.",
    "You're not a disaster, you're a beautiful whirlwind of chaos.",
    "I'm not saying you're a bad product designer, but you could make a product cry.",
    "You're not a fool, you're just a student of the absurd.",
    "I'm not saying you're a bad industrial designer, but you could make a machine cry.",
    "You're not a mess, you're a beautiful storm of confusion.",
    "I'm not saying you're a bad urban planner, but you could make a city cry.",
    "You're not a failure, you're just a work in progress.",
    "I'm not saying you're a bad transportation planner, but you could make a vehicle cry.",
    "You're not a weirdo, you're a collector of irregularities.",
    "I'm not saying you're a bad environmental planner, but you could make the planet cry.",
    "You're not a disaster, you're a beautiful hurricane of mayhem.",
    "I'm not saying you're a bad regional planner, but you could make a region cry.",
    "You're not a fool, you're just a student of the ridiculous.",
    "I'm not saying you're a bad community developer, but you could make a community cry.",
    "You're not a mess, you're a beautiful tornado of turmoil.",
    "I'm not saying you're a bad economic developer, but you could make an economy cry.",
    "You're not a failure, you're just a work in progress.",
    "I'm not saying you're a bad housing developer, but you could make a house cry."
]

random.shuffle(dares)

for dare in dares:
    cur.execute("INSERT INTO messages (text) VALUES (?)", (dare,))

connection.commit()
connection.close()

print("Database initialized successfully with 100 new, sarcastic compliments.")
