template  = {
    "start": {
        "text": "",
        "options": {
            "1": "",
        },
        "next": {
            "1": "",
        },
        "events": {
        },
    },
}

mainMenu = {
    "start": {
        "text": "Welcome to Joms Quest IV",
        "options": {
            "1": "New Adventure",
            "2": "Load Game (This doesn't work)",
            "3": "Tutorial",
        },
        "next": {
            "1": "begin",
            "2": "load",
            "3": "tutorial",
        }
    },
    "begin": {
        "text": "",
        "options": {},
        "next": None,
        "events": ["newGame"],
    },
    "load": {
        "text": "I told you this doesn't work.",
        "options": {
            "1": "New Adventure",
            "2": "Load Game (This doesn't work)",
            "3": "Tutorial",
        },
        "next": {
            "1": "begin",
            "2": "load",
            "3": "tutorial",
        }
    },
    "tutorial": {
        "text": "It's a point and click adventure game. You can figure this out yourself.",
        "options": {
            "1": "New Adventure",
            "2": "Load Game (This doesn't work)",
            "3": "Tutorial",
        },
        "next": {
            "1": "begin",
            "2": "load",
            "3": "tutorial",
        }
    },
}

settingsMenu = {
    "start": {
        "text": "",
        "options": {
            "4": "Continue",
            # "5": "New Game", # This doesn't work because it doesnt reset these dicts
            "3": "Exit to Desktop",
        },
        "next": {
            "4": "continue",
            "5": "begin",
            "3": "confirmEnd",
        },
        "events": {
        },
    },
    "exit": {
        "text": "Exiting Game",
        "options": {},
        "next": None,
        "events": ["exitGame"],
    },
    "continue": {
        "text": "",
        "options": {},
        "next": None,
        "events": [],
    },
    "confirmEnd": {
        "text": "Please don't go. The Joms need you. Exit game?",
        "options": {
            "1": "Yes",
            "2": "No",
        },
        "next": {
            "1": "exit",
            "2": "start",
        },
    },
    "begin": {
        "text": "Starting New Game",
        "options": {},
        "next": None,
        "events": ["newGame"],
    },
}

testManDialog = {
    "start": {
        "text": "Hello Joms!",
        "options": {
            "1": "Give me a wrench!",
            "2": "Leave"
        },
        "next": {
            "1": "awkward",
            "2": "Leave",
        },
    },
    "awkward": {
        "text": "Ok here you go. (You got a Wrench!)",
        "options": {
            "1": "Leave"
        },
        "next": {
            "1": "Leave"
        },
        "events": ["giveWrench", "wrenchTaken"],
    },
    "Leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

quizDialog = {
    "start": {
        "text": "Oh wonderful, Joms decided to grace us with their prescence. You do realize this is the final exam, right? The one that determines whether you get to go on the school trip?",
        "options": {
            "1": "Continue...",
        },
        "next": {
            "1": "sit",
        },
    },
    "sit": {
        "text": "Take whatever seat you can find when you're ready. Just remember you need to get a perfect score to pass this exam.",
        "options": {
            "1": "Start Exam",
            "2": "I'm not ready.",
        },
        "next": {
            "1": "naruto",
            "2": "leave",
        },
        "events": ["resetQuizScore"],
    },
    "naruto": {
        "text": "First subject English. Naruto said, \"I used one of my clones to transform into a shuriken.\" Who or what transformed into the shuriken?",
        "options": {
            "1": "Naruto",
            "2": "Naruto's Clone",
            "3": "Nothing transformed",
            "4": "It's ambiguous",
        },
        "next": {
            "1": "wrongNaruto",
            "2": "rightNaruto",
            "3": "wrongNaruto",
            "4": "rightNaruto",
        },
        "events": ["flagStartedQuiz"]
    },
    "wrongNaruto": {
        "text": "...",
        "options": {
            "1": "Continue..."
        },
        "next": {
            "1": "beef"
        },
    },
    "rightNaruto": {
        "text": "...",
        "options": {
            "1": "Continue..."
        },
        "next": {
            "1": "beef"
        },
        "events": ["correctAnswer"]
    },
    "beef": {
        "text": "Next Math. Joseph has 5lbs of ground beef. How many pounds of extra lean ground beef does he need to add to get lean beef?",
        "options": {
            "1": "5lbs",
            "2": "10lbs",
            "3": "It's impossible to get lean beef.",
            "4": "None of the above",
        },
        "next": {
            "1": "wrongBeef",
            "2": "rightBeef",
            "3": "wrongBeef",
            "4": "wrongBeef",
        },
    },
    "wrongBeef": {
        "text": "...",
        "options": {
            "1": "Continue..."
        },
        "next": {
            "1": "hair"
        },
    },
    "rightBeef": {
        "text": "...",
        "options": {
            "1": "Continue..."
        },
        "next": {
            "1": "hair"
        },
        "events": ["correctAnswer"]
    },
    "hair": {
        "text": "Now onto Biology: What color hair does this girl have?",
        "options": {
            "1": "Brown",
            "2": "Orange",
            "3": "Red",
            "4": "Blonde",
        },
        "next": {
            "1": "wrongHair",
            "2": "wrongHair",
            "3": "rightHair",
            "4": "wrongHair",
        },
        "image": "codeGeassShirley"
    },
    "wrongHair": {
        "text": "...",
        "options": {
            "1": "Continue..."
        },
        "next": {
            "1": "persona"
        },
    },
    "rightHair": {
        "text": "...",
        "options": {
            "1": "Continue..."
        },
        "next": {
            "1": "persona"
        },
        "events": ["correctAnswer"]
    },
    "persona": {
        "text": "Next topic Literature. What is the worst Persona game?",
        "options": {
            "1": "Persona 3",
            "2": "Persona 4",
            "3": "Persona 5",
            "4": "All of the above",
        },
        "next": {
            "1": "rightPersona",
            "2": "wrongPersona",
            "3": "wrongPersona",
            "4": "wrongPersona",
        },
    },
    "wrongPersona": {
        "text": "...",
        "options": {
            "1": "Continue..."
        },
        "next": {
            "1": "chicken"
        },
    },
    "rightPersona": {
        "text": "...",
        "options": {
            "1": "Continue..."
        },
        "next": {
            "1": "chicken"
        },
        "events": ["correctAnswer"]
    },
    "chicken": {
        "text": "Culinary Arts is up next. You are at a resteraunt. You are full, but there is a single chicken wing left. What should you do?",
        "options": {
            "1": "Leave the wing there",
            "2": "Take the wing home",
            "3": "Eat the wing anyway",
        },
        "next": {
            "1": "wrongChicken",
            "2": "wrongChicken",
            "3": "rightChicken",
        },
    },
    "wrongChicken": {
        "text": "",
        "options": {
            "1": "Continue..."
        },
        "next": {
            "1": "essay"
        },
    },
    "rightChicken": {
        "text": "",
        "options": {
            "1": "Continue..."
        },
        "next": {
            "1": "essay"
        },
        "events": ["correctAnswer"]
    },
    "essay": {
        "text": "Final question: Define a slur.",
        "options": {
            "1": "Finish Exam",
        },
        "next": {
            "1": "results",
        },
        "events": ["essayQuestion", "scoreQuiz"]
    },
    "results": {
        "text": "You did not pass the exam. Maybe try applying youself next time.",
        "options": {
            "1": "Leave",
        },
        "next": {
            "1": "leave"
        },
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

phoneWaveDialog = {
    "start": {
        "text": "Welcome to the PhoneWave (Name Subject To Change).",
        "options": {
            "1": "Enter Date",
            "2": "Leave",
        },
        "next": {
            "1": "...",
            "2": "leave",
        },
    },
    "...": {
        "text":  "...",
        "options": {
            "1": "Leave",
        },
        "next": {
            "1": "leave",
        },
        "events": ["phoneWaveInput"],

    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

keypadDialog = {
    "start": {
        "text": "As you use approach the keypad, a voice sounds from the school's PA system. \"This is the school-wide clock override system.\"",
        "options": {
            "1": "Continue..."
        },
        "next": {
            "1": "explain",
        },
    },
    "explain": {
        "text": "Please enter the time you wish to set the clocks to.",
        "options": {
            "1": "Continue...",
        },
        "next": {
            "1": "nothing",
        },
        "events": ["setTime"],
    },
    "nothing": {
        "text": "You set the time, but nothing happens.",
        "options": { 
            "1": "Continue...",
        },
        "next": {
            "1": "leave"
        },
    },
    "730": {
        "text" : "Well you see, you actually needed to contradict what time the sprinklers were supposed to come on, so in reality you SHOULD have entered 10:00 not 7:30.",
        "options": {
            "1" : "Continue..."
        },
        "next": {
            "1" : "nothing",
        },
    },
    "sprinklers": {
        "text": "You hear a rush of water coming from the girl's bathroom.",
        "options": {
            "1": "Continue..."
        },
        "next": {
            "1": "leave"
        },
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

momsDialog = {
    "start": {
        "text": "How are you doing honey?",
        "options": {
            "2": "Leave",
        },
        "next": {
            "2": "leave",
        },
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

jomsSrDialog = {
    "start": {
        "text": "How are you doing sport?",
        "options": {
            "2": "Leave",
        },
        "next": {
            "2": "leave",
        },
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

inventorDialog = {
    "start": {
        "text": "Hello",
        "options": {
            "1": "Leave",
        },
        "next": {
            "1": "leave",
        },
    },
    "freeze": {
        "text": "I have just the thing. It's the Portable Heater (Fuel not Included)! Just fill it up with some low-octain fuel and flip the switch.",
        "options": {
            "1": "Where am I supposed to get fuel?",
            "2": "Thanks!",
        },
        "next": {
            "1": "explainFuel",
            "2": "leave",
        },
        "events": ["giveHeater"],
    },
    "explainFuel": {
        "text": "It's the Portable Heater (Fuel not Included) not the Portable Heater (Fuel Included). Figure it out youself.",
        "options": {
            "1": "Leave",
        },
        "next": {
            "1": "leave",
        },
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

trainDialog = {
    "start": {
        "text": "Hello",
        "options": {
            "1": "Leave",
        },
        "next": {
            "1": "leave",
        },
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

karuDialog = {
    "start": {
        "text": "Hello",
        "options": {
            "1": "Leave",
        },
        "next": {
            "1": "leave",
        },
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

frozenKaruDialog = {
    "start": {
        "text": "So... C-C-Cold... Please... Help...",
        "options": {
            "1": "Leave",
        },
        "next": {
            "1": "leave",
        },
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

fireKaruDialog = {
    "start": {
        "text": "Hello",
        "options": {
            "1": "Leave",
        },
        "next": {
            "1": "leave",
        },
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

thermostatDialog = {
    "start": {
        "text": "There's a thermostat on the wall. It says the current temperature is 74°F.",
        "options": {
            "1": "Increase Temperature",
            "2": "Decrease Temperature",
            "3": "Leave",
        },
        "next": {
            "1": "increase",
            "2": "decrease",
            "3": "leave",
        },
    },
    "increase": {
        "text": "You increase the room's temperature to 75°F. You quickly realize this is too hot and quickly set the temperature back to 74°F.",
        "options": {
            "2": "Decrease Temperature",
            "3": "Leave",
        },
        "next": {
            "2": "decrease",
            "3": "leave",
        },
    },
    "decrease": {
        "text": "You set the room's temperature to 73°F. The sudden arctic gust freezes the thermostat control mechanism solid, rendering it inoperable.",
        "options": {
            "1": "leave",
        },
        "next": {
            "1": "leave",
        },
        "events": ["freezeRoom"]
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

normDialog = {
    "start": {
        "text": "Hello",
        "options": {
            "1": "Leave",
        },
        "next": {
            "1": "leave",
        },
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

computerDialog = {
    "start": {
        "text": "You log onto the computer.",
        "options": {
            "1": "Twitch",
            "3": "Discord",
            "4": "Youtube",
            "5": "Turn off computer",
        },
        "next": {
            "1": "twitch",
            "3": "discord",
            "4": "youtube",
            "5": "leave",
        },
    },
    "twitch": {
        "text": "You navigate to twitch.tv/andersonjph. Joe is currently streaming some weeb game and making confused 'OOO??'ing noises. You'll catch the VOD later.",
        "options": {
            "3": "Discord",
            "4": "Youtube",
            "5": "Turn off Computer",
        },
        "next": {
            "3": "discord",
            "4": "youtube",
            "5": "leave",
        },
    },
    "discord": {
        "text": "You log onto discord and check #dragons-den. Somehow Piss-course returned. You make the wise decision and not get involved.",
        "options": {
            "1": "Twitch",
            "4": "Youtube",
            "5": "Turn off computer",
        },
        "next": {
            "1": "twitch",
            "4": "youtube",
            "5": "leave",
        },
    },
    "youtube": {
        "text": "You check the recent uploads of your favorite Youtuber Joseph Anderson to see if he uploaded the Witcher 3 video yet. It looks like the Witcher 3 video isn't out yet. Where could it be?",
        "options": {
            "1": "Twitch",
            "3": "Discord",
            "5": "Turn off computer",
        },
        "next": {
            "1": "twitch",
            "3": "discord",
            "5": "leave",
        },
    },
    "victory": {
        "text": "You check Youtube, and there you see it. The Witcher 3 - Worse Than Breaking Bad by Joeseph Anderson. Total runtime 239 Hours and 53 Minutes.",
    }, # TODO fix this
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}
