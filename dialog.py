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
        "text": "Please enter the hour you wish to set the clocks to.",
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
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}