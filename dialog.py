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
        "image": ("codeGeassShirley",(500,150))
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
        "text": "Welcome to the Maroon Vista Train Line. Please show your ticket before boarding.",
        "options": {
            "2": "I don't have a ticket.",
            "3": "Where does this train line go?",
            "1": "Leave",
        },
        "next": {
            "2": "then",
            "3": "iraq",
            "1": "leave",
        },
    },
    "then": {
        "text": "Then I don't have to let you on the train.",
        "options": {
            "3": "Where does this train line go?",
            "1": "Leave",
        },
        "next": {
            "3": "iraq",
            "1": "leave",
        },
    },
    "iraq": {
        "text": "Iraq",
        "options": {
            "2": "I don't have a ticket.",
            "1": "Leave",
        },
        "next": {
            "2": "then",
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
        "text": "******* PUT IT OUT ****! ****! MOTHER ******* ***** ****! PUT IT OUT!",
        "options": {
            "2": "Remember to stop drop and roll!",
            "1": "Leave",
        },
        "next": {
            "2": "roll",
            "1": "leave",
        },
    },
    "roll": {
        "text": "**** YOU ****!",
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
        "text": "You increase the room's temperature to 75°F. You realize this is too hot and quickly set the temperature back to 74°F.",
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
        "text": "Welcome to Norm's Pizza eh. How can we serve you today, friend?",
        "options": {
            "1": "I would like a large pizza.",
            "2": "Leave",
        },
        "next": {
            "1": "pizza",
            "2": "normalDay",
        },
    },
    "pizza": {
        "text": "What toppings do you want on that?",
        "options": {
            "1": "Cheese",
            "2": "Pepperoni",
            "3": "Olives",
            "4": "Pineapple",
        },
        "next": {
            "1": "pay",
            "2": "pay",
            "3": "olives",
            "4": "pineapple",
        },
    },
    "pay": {
        "text": "That will be 19.99CAD.",
        "options": {
            "1": "I don't have any Monopoly money.",
        },
        "next": {
            "1": "no"
        },
        "events": ["itemsForPizza"],
    },
    "no": {
        "text": "Why would you order a pizza without money eh? Sore-ry bud, no cash, no pizza.",
        "options": {
            "1": "Leave",
        },
        "next": {
            "1": "normalDay",
        },
    },
    "deny": {
        "text": "That's funnier than a moose at a comedy club, that is. Sore-ry bud, no cash, no pizza.",
        "options": {
            "1": "Leave",
        },
        "next": {
            "1": "normalDay",
        },
    },
    "olives": {
        "text": "(Norm Chan looks at you with disgust) Sore-ry eh, we don't serve those types of gross toppings. Olives are more disgusting than a poutine with American cheese.",
        "options": {
            "1": "Cheese",
            "2": "Pepperoni",
            "4": "Pineapple",
        },
        "next": {
            "1": "pay",
            "2": "pay",
            "4": "pineapple",
        },
    },
    "pineapple": {
        "text": "DING DING DING Congratulations, you are the first customer to order the Norm's Pineapple Pizza eh. This one's on the house pal. (You got a Pineapple Pizza)",
        "options": {
            "1": "Thanks!",
        },
        "next": {
            "1": "normalDay",
        },
        "events": ["givePizza"],
        "image": ("confetti", (0,0)),
    },

    "normalDay": {
        "text": "Have a Norm-al D-eh!",
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
        "text": "You check the recent uploads of your favorite Youtuber Joseph Anderson to see if he uploaded the Witcher 3 video yet. It looks like the Witcher 3 video has not been released. Where could it be?",
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
        "options": {"1": "Watch Witcher 3 Video"},
        "next": {"witcher"},
    },
    "witcher": {
        "text": "You settle down to watch the entire video in one sitting. As Joe's calming tone washes over you, you have one final thought \"It was worth the wait\"",
        "options": {"1": "The End"},
        "next": {"1": "end"},
    },
    "end": {
        "text": "The Spongebob Movie really is overrated",
        "options": {"1": "The End"},
        "next": {"1": "leave"},
        "events": ["credits"],
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

pastComputerDialog = {
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
            "5": "Turn off computer",
        },
        "next": {
            "3": "discord",
            "4": "youtube",
            "5": "leave",
        },
    },
    "discord": {
        "text": "You log onto discord and check #dragons-den. It appears there's a vote for what games Joe will steam next Christmas. The choices are between Feliz Navidango and Telltale-mas. Joms Sr has already cast his vote for Telltale-mas, but it's not too late to change it.",
        "options": {
            "1": "Don't change vote.",
            "4": "Vote for Feliz Navidango",
        },
        "next": {
            "1": "leave",
            "4": "voted",
        },
    },
    "voted": {
        "text": "You changed the vote for Feliz Navidango and feel the world shift.",
        "options": {"1": "Turn off computer"},
        "next": {"1": "leave"},
        "events": ["iVoted"],
    },
    "youtube": {
        "text": "You check the recent uploads of your favorite Youtuber Joseph Anderson to see if he uploaded the Witcher 3 video yet. It looks like the Witcher 3 video has not been released. Where could it be?",
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
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}


bagChanDialog = {
    "start": {
        "text": "Ohayo good morning, Joms!",
        "options": {
            "1": "I thought you'd be shorter.",
            "2": "Leave",
        },
        "next": {
            "1": "shorter",
            "2": "leave",
            "eat": "eat",
            "mine": "mine",
        },
    },
    "eat": {
        "text": "I don't even have time to explain how I don't have time to explain.",
        "options": {
            "1": "Leave",
        },
        "next": {
            "1": "leave",
        },
    },
    "mine": {
        "text": "Sorry, I'm just having a rough day. Usually I get my meal from the bar, but they started taking their trash out a day earlier. Times are tough.",
        "options": {
            "eat": "How did you even eat that?",
            "1": "Leave",
        },
        "next": {
            "eat": "eat",
            "1": "leave",
        },
    },
    "shorter" : {
        "text": "...sorry to disappoint?",
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

bagChanStuffedDialog = {
    "start": {
        "text": "The cardboard really adds a nice, chewy texture.",
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

botsephDialog = {
    "start": {
        "text": "Greeting {Patron}, Welcome to {Bar}. What can I get you?",
        "options": {
            "1": "I'd like a drink please.",
            "2": "ur a {Bar}",
            "3": "Leave",
        },
        "next": {
            "1": "drink",
            "2": "pupper",
            "3": "leave",
        },
    },
    "pupper": {
        "text": ":pupper:",
        "options": {"1": "Leave"},
        "next": {"1": "leave"},
    },
    "drink": {
        "text": "{you.age} < {LEGAL_DRINKING_AGE}, cannot process request.",
        "options": {
            "1": "What can I get then?",
            "2": "Leave",
        },
        "next": {
            "1": "juice",
            "2": "leave",
        },
    },
    "juice": {
        "text": "juice.give(). By the time juice.ferment(), {you.age} >= {LEGAL_DRINKING_AGE} will be True.",
        "options": {"1": "Thanks..."},
        "next": {"1": "leave"},
        "events": ["giveJuice"]
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}


falzarDialog = {
    "start": {
        "text": "ID Please",
        "options": {
            "1": "Can you let me in?",
            "2": "Leave",
        },
        "next": {
            "1": "letme",
            "2": "leave",
        },
    },
    "letme": {
        "text": "Sure, show me your ID first",
        "options": {
            "1": "I don't have an ID.",
            "2": "Leave"
        },
        "next": {
            "1": "id",
            "2": "leave",
        },
    },
    "id": {
        "text": "Listen kid, I can't let you in without an ID and it's almost lunch time so get out of here before I become a Hostile Crocodile.",
        "options": {
            "1": "Atleast tell me what's in the bar.",
            "2": "Leave",
        },
        "next": {
            "1": "spoilers",
            "2": "leave",
        },
    },
    "spoilers": {
        "text": "No spoilers.",
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

beacoiDialog = {
    "start": {
        "text": "Welcome to Beacoi's Fight Club.",
        "options": {
            "1": "I want to fight!",
            "2": "Leave",
        },
        "next": {
            "1": "want",
            "2": "leave",
        },
    },
    "want": {
        "text": "I like your spirit, but before we get started let me explain the rules of Beacoi's Fight Club first.",
        "options": {
            "1": "What are the rules of Beacoi's Fight Club?",
            "2": "I already know the rules.",
            "3": "Nevermind I'm too scared."
        },
        "next": {
            "1": "rule1",
            "2": "fight?",
            "3": "leave",
        },
        "events": ["checkGirl"],
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
    "rule1": {
        "text": "The first rule of Beacoi's Fight Club: You do not talk about Beacoi's Fight Club. The second rule of Beacoi's Fight Club: You do NOT talk about Beacoi's Fight Club.",
        "options": {
            "1": "Continue...",
        },
        "next": {
            "1": "rule3",
        },
    },
    "rule3": {
        "text": "The third rule of Beacoi's Fight Club: No girls are allowed to fight",
        "options": {
            "1": "Pretty sexist Beacoi, why can't girls fight?",
            "2": "Continue...",
        },
        "next": {
            "1": "girlExplain",
            "2": "rule4",
        }, 
    },
    "girlExplain": {
        "text": "Beacoi Ofsnoe believes in equal rights (and left in this case), but the Women's league is on Thursdays.",
        "options": {
            "1": "Continue...",
        },
        "next": {
            "1": "rule4",
        },
    },
    "rule4": {
        "text": "The fourth rule of Beacoi's Fight Club: You have the right to the weapon of your choosing. If you do not have a weapon, you may select one from my personal collection.",
        "options": {"1": "Continue..."},
        "next": {"1": "rule5"},
    },
    "rule5": {
        "text": "Final rule of Beacoi's Fight Club: No shirts, no shoes.",
        "options": {
            "1": "But Beacoi, you are wearing a shirt.",
            "2": "I'm ready!",
        },
        "next": {
            "1": "shirt",
            "2": "fight?",
        },
    },
    "shirt": {
        "text": "No I'm not.",
        "options": {"1" : "I'm ready!"},
        "next": {"1": "fight?"},
    },
    "fight?": {
        "text": "So what do you say? Want to fight?",
        "options": {
            "1": "Yes",
            "2": "No",
        },
        "next": {
            "1": "weapon",
            "2": "leave",
        },
    },
    "weapon": {
        "text": "If you didn't bring a weapon with you, select your weapon.",
        "options": {
            "1": "Shot Put Ball",
            "2": "Gun",
            "3": "Katanna",
            "4": "Nevermind I'm scared.",
        },
        "next": {
            "1": "shotput",
            "2": "gun",
            "3": "katanna",
            "4": "leave",
        },
    },
    "urAGirl": {
        "text": "Sorry miss, but girls aren't allowed to fight in Beacoi's Fight Club. Please come back on Thursday for the Women's league.",
        "options":  {"1": "Leave"},
        "next": {"1": "leave"},
    },
    "shotput": {
        "text": "You pick up the Shot Put Ball and stand ready. \"BEGIN!\" Shouted Beacoi as he rushes you. You dropped everything you were holding, but since you didn't create an elaborate Rube Goldberg death trap before hand, it was ineffective.",
        "options": {"1": "Continue..."},
        "next": {"1": "lose"},
    },
    "gun": {
        "text": "You pick up the Gun and stand ready. \"BEGIN!\" Shouted Beacoi as he rusheds you. You take and and fire dead-center on your target. Beacoi effortlessly deflect the bullet with his knife-like talons.",
        "options": {"1": "Continue..."},
        "next": {"1": "lose"},
    },
    "katanna": {
        "text": "You pick up the Katanna and stand ready. \"BEGIN!\" Shouted Beacoi as he rushes you. As you attempt to parry Beacoi's slashes, the Glorious Nippon Steel folded over a thousand times shatters into a thousand pieces.",
        "options": {"1": "Continue..."},
        "next": {"1": "lose"},
    },
    "lose": {
        "text": "You collapsed and all goes black. You wake up back in your room, bruised and bloodied.",
        "options": {"1": "Ow..."},
        "next": {"1": "leave"},
        "events": ["loseFight"],
    },
}

beacoiWinDialog = {
    "start": {
        "text": "You point the bat at Beacoi in challenge and stand ready. \"BEGIN\" Shouted Beacoi as he rushes you. You take a step and put your full force behind a single swing. Due to your advantage in reach and stopping power, you manage to cleanly knock Beacoi out in just one blow.",
        "options": {
            "2": "Continue...",
        },
        "next": {
            "2": "victory",
        },
    },
    "victory": {
        "text": "Not bad kid. No one's ever managed to beat me in a fight. For that, I will give you my most prized possession, a mint condition Space Jam DVD.",
        "options": {"1": "Leave"},
        "next": {"1": "leave"},
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

