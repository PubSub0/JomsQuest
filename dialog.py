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
            "3": "Tutorial",
        },
        "next": {
            "1": "begin",
            "3": "tutorial",
        }
    },
    "begin": {
        "text": "",
        "options": {},
        "next": None,
        "events": ["newGame"],
    },

    "tutorial": {
        "text": "It's a point and click adventure game. Left Click to use, Right Click to examine. You could have figured this out yourself.",
        "options": {
            "1": "New Adventure",
            "3": "Tutorial",
        },
        "next": {
            "1": "begin",
            "3": "tutorial",
        }
    },
}

settingsMenu = {
    "start": {
        "text": "",
        "options": {
            "4": "Continue",
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
        "text": "Take whatever seat you can find when you're ready. Just remember: you need to get a perfect score to pass this exam.",
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
        "text": "Culinary Arts is up next. You are at a restaurant. You are full, but there is a single chicken wing left. What should you do?",
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
        "text": "You did not pass the exam. Maybe try applying youself next time?",
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
        "sound": "mayuri",
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
        "sound": "sprinklerSound",
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
            "1": "Hi Moms",
            "2": "Leave",
        },
        "next": {
            "1": "hi",
            "2": "leave",
        },
    },
    "hi": {
        "text": "You better hurry to school before you're late. You have a big quiz today. Also while you're out can you go get the microwave fixed?",
        "options": {
            "1": "Leave",
        },
        "next": {"1": "leave"},
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

momsFutureDialog = {
    "start": {
        "text": "Oh, there you are! Thanks for getting that microwave fixed, sweetie. I made a big batch of Cookies to celebrate. They should be done in just a minute, so go on and wait in your room - I'll call you when they're done.",
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

momsPastDialog = {
    "start": {
        "text": "Hey there gorgeous.",
        "options": {
            "3": "Hi Moms, I'm your son from the future.",
            "1": "How do I get Joms Sr off the computer?",
            "2": "Leave",
        },
        "next": {
            "3": "son",
            "1": "computer",
            "2": "leave",
        },
    },
    "son": {
        "text": "Oh you're into roleplay huh? You can call me \"Mommy\" then *wink*.",
        "options": {
            "1": "How do I get Joms Sr off the computer?",
            "2": "Leave",
        },
        "next": {
            "1": "computer",
            "2": "leave",
        },
    },
    "computer": {
        "text": "*Sigh* All he does all day is read JADS and watch anime. Doesn't he know I need \"Entertainment\" too?",
        "options": {
            "1": "What kind of entertainment?",
            "2": "Leave",
        },
        "next": {
            "1": "entertainment",
            "2": "leave",
        },
    },
    "entertainment": {
        "text": "Oh, you know the kind where you [DIALOG PENDING ESRB APPROVAL] with ketchup. Maybe you'd be interested? *wink*",
        "options": {
            "1": "No",
            "2": "NO",
            "3": "Nonononooononoononoo",
            "4": "NOOOOOOOOOOOOOOOOOOOOOOOOOOO",
        },
        "next": {
            "1": "no",
            "2": "no",
            "3": "no",
            "4": "no",
        },
    },
    "no": {
        "text": "What a shame. Let me know if you change your mind.",
        "options": {"1": "Leave"},
        "next": {"1": "leave"},
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

momsPastLivingDialog = {
    "start": {
        "text": "He finally came out of his room! Now's my chance...",
        "options": {"1": "Leave"},
        "next": {"1": "leave"},
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
            "1": "witcher",
            "4": "spaceJam",
            "2": "leave",
        },
    },
    "spaceJam": {
        "text": "Well, Sport, I'm not sure! I've been so busy watching this Space Jam DVD that I haven't had the time to check.",
        "options": {"1": "Leave"},
        "next": {"1": "leave"},
    },
    "witcher": {
        "text": "Ah yes, the Witcher 3 video. I remember a long time ago, Joseph Anderson was just about to release the video, but something regrettable happened.",
        "options": {"1": "Continue..."},
        "next": {"1": "witcher2"},
    },
    "witcher2": {
        "text": "It was a day a lot like this one. I even remember the exact date, July 3rd 2011. In JADS we were all voting for which game Joe should stream that Christmas. It was an exciting time.",
        "options": {"1": "Continue..."},
        "next": {"1": "witcher3"},
    },
    "witcher3": {
        "text": "You see, I had cast the deciding vote for Telltale-mas, narrowly beating Feliz Navi-dango (A Lucas Arts Adventure Game Holiday Celebration).",
        "options": {"1": ":HeinzGate:"},
        "next": {"1": "witcher4"},
    },
    "witcher4": {
        "text":  "Who knows what would have happened had I voted differently. Maybe the Witcher 3 video would be out now. I will always live with regret for my choice that day.",
        "options": {"1": "Leave"},
        "next": {"1": "leave"},
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

jomsSrPastDialog = {
    "start": {
        "text": "Can't talk now, someone in JADS just said Dark Souls 2 was the worst Soulslike.",
        "options": {
            "1": "I'm your son from the future.",
            "2": "Can I get on the computer?",
            "3": "Leave",
        },
        "next": {
            "1": "son",
            "2": "computer",
            "3": "leave",
        },
    },
    "son": {
        "text": "Hi \"your son from the future\" I'm Joms Sr",
        "options": {
            "1": "Why are you \"Joms Sr\" if you don't have a child yet?",
            "2": "Can I get on the computer?",
            "3": "Leave",
        },
        "next": {
            "1": "jomsSr",
            "2": "computer",
            "3": "leave",
        },
    },
    "jomsSr": {
        "text": "I'll tell you when you're older.",
        "options": {
            "2": "Can I get on the computer?",
            "3": "Leave",
        },
        "next": {
            "2": "computer",
            "3": "leave",
        },
    },
    "computer": {
        "text": "Shhhh Joe is streaming.",
        "options": {"1": "Leave"},
        "next": {"1": "leave"},
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

jomsSrPastLivingDialog = {
    "start": {
        "text": "He keeps repeating the words \"Space Jam DVD.\" We don't even have a TV.",
        "options": {"1": "Leave"},
        "next": {"1": "leave"},
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

inventorDialog = {
    "start": {
        "text": "Hello Joms",
        "options": {
            "3": "What do you do here?",
            "2": "What are you doing in the bathroom?",
            "1": "Leave",
        },
        "next": {
            "3": "invent",
            "2": "bathroom",
            "1": "leave",
        },
    },
    "invent": {
        "text": "I invent fantastic creations. Robots, AI language models, home appliances -- I make it all. Just give me the supplies and I can whip you up something.",
        "options": {
            "2": "What are you doing in the bathroom?",
            "1": "Leave",
        },
        "next": {
            "2": "bathroom",
            "1": "leave",
        },
    },
    "bathroom": {
        "text": "All the greatest ideas are conceived on the toilet. Plus, when I'm bored I can always play a set of Melty Blood in one of the stalls.",
        "options": {
            "3": "What do you do here?",
            "1": "Leave",
        },
        "next": {
            "3": "invent",
            "1": "leave",
        },
    },
    "freeze": {
        "text": "I have just the thing. It's the Portable Heater (Fuel not Included)! Just fill it up with some low-octane fuel and flip the switch.",
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
        "text": "Iraq.",
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
        "sound": "quoiPanic",
    },
    "roll": {
        "text": "**** YOU ****!",
        "options": {
            "1": "Leave",
        },
        "next": {
            "1": "leave",
        },
        "sound": "quoiPanic",
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
        "sound": "quoi",
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

karuDialog = {
    "start": {
        "text": "Hi Whore! <3",
        "options": {
            "1": "Why is there a batting cage in the bathroom?",
            "2": "Hi whooooore! <3",
            "3": "Leave",
        },
        "next": {
            "1": "batting",
            "2": "whore",
            "3": "leave",
        },
        "sound": "quoi",
    },
    "whore": {
        "text": "Oh, FINALLY! A proper greeting! I was beginning to think I was the only cultured person in this whole town.",
        "options": {
            "1": "Why is there a batting cage in the bathroom?",
            "3": "Leave",
        },
        "next": {
            "1": "batting",
            "3": "leave",
        },
    },
    "batting": {
        "text": "I know right? It's so pedestrian. My last school's bathroom had catering and live ballet performances.",
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
        "events": ["freezeRoom"],
        "sound": "freezeSound",
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
        "sound": "winSound",
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
        "text": "You log onto discord and check #dragons-den. Somehow Piss-course returned. You make the wise decision to not get involved.",
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
        "text": "You check the recent uploads of your favorite Youtuber, Joseph Anderson, to see if he uploaded the Witcher 3 video yet. It doesn't appear to have been released. Where could it be?",
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
        "events": ["whereIsWitcher"],
    },
    "victory": {
        "text": "You check Youtube... and there it is. \"The Witcher 3 - Worse Than Breaking Bad\" by Joseph Anderson. Total runtime: 239 hours and 53 minutes.",
        "options": {"1": "Watch Witcher 3 Video"},
        "next": {"witcher"},
    },
    "witcher": {
        "text": "You settle down to watch the entire video in one sitting. As Joe's calming tone washes over you, you have one final thought... \"It was worth the wait.\"",
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
        "text": "You check the recent uploads of your favorite Youtuber, Joseph Anderson, to see if he uploaded the Witcher 3 video yet. It doesn't appear to have been released. Where could it be?",
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
            "4": "Where did the bouncer's body go?",
            "2": "ur a {Bar}",
            "3": "Leave",
        },
        "next": {
            "1": "drink",
            "4": "bouncer",
            "2": "pupper",
            "3": "leave",
        },
    },
    "bouncer": {
        "text": "It's a {Plothole}.",
        "options": {
            "1": "Leave",
        },
        "next": {"1": "leave"},
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
        "options": {"1": "Thanks...?"},
        "next": {"1": "leave"},
        "events": ["giveJuice"],
        "sound": "bagSound",
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}


falzarDialog = {
    "start": {
        "text": "ID, please.",
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
        "text": "Sure, show me your ID first.",
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
        "text": "Listen kid, I can't let you in without an ID. It's almost lunch time, so scram before I become a Hostile Crocodile.",
        "options": {
            "1": "At least tell me what's in the bar.",
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
        "text": "Beacoi Osfnoe believes in Women's Rights (and Lefts, in this case), but the Women's League is on Thursdays.",
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
            "3": "Katana",
            "4": "Nevermind I'm scared.",
        },
        "next": {
            "1": "shotput",
            "2": "gun",
            "3": "katana",
            "4": "leave",
        },
    },
    "urAGirl": {
        "text": "Sorry miss, but girls aren't allowed to fight in Beacoi's Fight Club. Please come back on Thursday for the Women's league.",
        "options":  {"1": "Leave"},
        "next": {"1": "leave"},
    },
    "shotput": {
        "text": "You pick up the Shot Put Ball and stand ready. With a ring of the bell, Beacoi rushes you. You dropped everything you were holding, but since you didn't create an elaborate Rube Goldberg death trap before hand, it was ineffective.",
        "options": {"1": "Continue..."},
        "next": {"1": "lose"},
    },
    "gun": {
        "text": "You pick up the Gun and stand ready. With a ring of the bell, Beacoi rushes you. You take aim and fire dead-center on your target. Beacoi effortlessly deflect the bullet with his razor-sharp, knife-like talons.",
        "options": {"1": "Continue..."},
        "next": {"1": "lose"},
    },
    "katana": {
        "text": "You pick up the Katana and stand ready. With a ring of the bell, Beacoi rushes you. As you attempt to parry Beacoi's slashes, the Glorious Nippon Steel folded over a thousand times shatters into a thousand pieces.",
        "options": {"1": "Continue..."},
        "next": {"1": "lose"},
    },
    "lose": {
        "text": "You collapsed and all goes black. You wake up back in your room, bruised and bloodied.",
        "options": {"1": "Ow..."},
        "next": {"1": "leave"},
        "events": ["loseFight"],
        "sound": "oof",
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
        "sound": "homerun",
    },
    "victory": {
        "text": "Not bad, kid. No one's ever managed to beat me in a fight. For that, I will give you my most prized possession, a mint condition Space Jam DVD.",
        "options": {"1": "Leave"},
        "next": {"1": "leave"},
        "sound": "bagSound",
    },
    "leave": {
        "text": "",
        "options": {},
        "next": None,
    },
}

