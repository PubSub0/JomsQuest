import sys
import pygame
from dialog import *

# Initializing stuff needed for pygame
# Default init stuff
pygame.init()
# TODO change this to 1280x720
# screen = pygame.display.set_mode((800, 600))
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Joms Quest IV: The Search for a Better Subtitle (Version 1.1.0.37)")
clock = pygame.time.Clock()

# Setup for font outlining
fontSize = 32
pygame.font.init()
font = pygame.font.SysFont(None, fontSize)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

### Helpers
# Helper functions for outlining text 
_circle_cache = {}
def _circlepoints(r):
    r = int(round(r))
    if r in _circle_cache:
        return _circle_cache[r]
    x, y, e = r, 0, 1 - r
    _circle_cache[r] = points = []
    while x >= y:
        points.append((x, y))
        y += 1
        if e < 0:
            e += 2 * y - 1
        else:
            x -= 1
            e += 2 * (y - x) - 1
    points += [(y, x) for x, y in points if x > y]
    points += [(-x, y) for x, y in points if x]
    points += [(x, -y) for x, y in points if y]
    points.sort()
    return points

def render(text, font, gfcolor=white, ocolor=black, opx=5):
    textsurface = font.render(text, True, gfcolor).convert_alpha()
    w = textsurface.get_width() + 2 * opx
    h = font.get_height()

    osurf = pygame.Surface((w, h + 2 * opx)).convert_alpha()
    osurf.fill((0, 0, 0, 0))

    surf = osurf.copy()

    osurf.blit(font.render(text, True, ocolor).convert_alpha(), (0, 0))

    for dx, dy in _circlepoints(opx):
        surf.blit(osurf, (dx + opx, dy + opx))

    surf.blit(textsurface, (opx, opx))
    return surf

def splitString(text, max_length=60):
    words = text.split()
    lines = []
    currLine = ""

    for word in words:
        if len(currLine) + len(word) + 1 <= max_length:
            if currLine:
                currLine += " "
            currLine += word
        else:
            lines.append(currLine)
            currLine = word
    
    if currLine:
        lines.append(currLine)
    
    return lines

# Prints state.dialog and state.hoverText
def printText(text, x, y):
    currTextSplit = splitString(text)
    for i, line in enumerate(currTextSplit):
        renderDialog = render(line, font)
        yOff = y - ((len(currTextSplit)-1-i)*fontSize)
        screen.blit(renderDialog, renderDialog.get_rect(center = (x, yOff)))      


### Functions which run stuff
# Quick function to update the current state of things
# TODO maybe move dialog and hoverText to state?
def drawEverything(state, assets):
    # Update background to current room's background
    screen.blit(state.currRoom.bg, (0,0))

    # Update current UI elements
    for selectable in assets.global_selectables:
        screen.blit(selectable.image, selectable.pos)

    # Update room selectables
    for selectable in state.currRoom.selectables:
        screen.blit(selectable.image, selectable.pos)

    # Print out the current texts.
    printText(state.dialog, 640, 600)
    printText(state.hoverText, 640, 100)

# Gives you the current hovertext
# TODO maybe move hovertext to state?
def checkHoverText(selectablesLists, state) -> str:
    state.hoverText = ""

    # If an item is selected, then prepend the "Use {item} with {hover}" to the hoverText
    if state.selectedItem:
        state.hoverText += f"Use {state.selectedItem.name} with "
    
    for selectables in selectablesLists:
        for selectable in selectables:
            if selectable.get_rect().collidepoint(pygame.mouse.get_pos()):
                if state.selectedItem != selectable:
                    if selectable != assets.bag or state.selectedItem is None:
                        state.hoverText += selectable.name
    
    # state.hoverText += f"{pygame.mouse.get_pos()}"
    return state


# Function to run the given dialog tree
def startDialog(state, assets, x=640, y=550, fontSize=32):
    # Always assume dialog starts at start in the dict
    currNode = "start"
    state.dialog = ""
    playedSoundAtNode = False
    while True:
        # Need to draw everything here so that the dialog doesnt constantly stack up.
        drawEverything(state=state, assets=assets)

        # Display Response
        currText = state.currDialogTree[currNode]["text"]    
        printText(currText, x, y)

        # Display options
        options = state.currDialogTree[currNode]["options"]
        if not options:
            return (state, assets)

        y_offset = 40
        currOptions = {}
        for optionKey, optionText in options.items():
            optionDialog = render("- "  + optionText, font)
            # Jank shit to make the dialog being hovered over yellow
            if optionDialog.get_rect(center = (x, y+y_offset)).collidepoint(pygame.mouse.get_pos()):
                optionDialog = render("- " + optionText, font, gfcolor=yellow)
            optionRect =  optionDialog.get_rect(center = (x, y+y_offset))
            screen.blit(optionDialog, optionRect)
            currOptions[optionKey] =  optionRect 
            y_offset += fontSize

        # TODO make the x,y cords better
        if "image" in state.currDialogTree[currNode]:
            screen.blit(assets.imageLookup[state.currDialogTree[currNode]["image"][0]], state.currDialogTree[currNode]["image"][1])
            pygame.display.update()

        if "sound" in state.currDialogTree[currNode]:
            # Check if we already played it
            if not playedSoundAtNode:
                assets.soundLookup[state.currDialogTree[currNode]["sound"]].play()
                playedSoundAtNode = True

        pygame.display.update()

        # Handle events
        selectedOption = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePos = pygame.mouse.get_pos()
                for optionKey, optionRect in currOptions.items():
                    if optionRect.collidepoint(mousePos):
                        selectedOption = optionKey

        if selectedOption is not None:
            playedSoundAtNode = False
            currNode = state.currDialogTree[currNode]["next"][selectedOption]
            if "events" in state.currDialogTree[currNode]:
                for event in state.currDialogTree[currNode]["events"]:
                    state, assets = eventLookup[event](state, assets)

        clock.tick(60)


### Base Item Classes
# Base Room class with it's background, selectable objects, and exits
class Room(object):
    def __init__(self, name, bg=None, selectables=[], exits=[], enterEvents=[], song=None):
        self.bg = bg
        self.selectables = selectables
        self.name = name
        self.exits = exits
        self.enterEvents = enterEvents
        self.song = song

# Base selectable class. Anything that can be iteracted with should be this class.
class Selectable(object):
    def __init__(self, pos, name="", image=None, examine="", useTxt="I can't use that", useSound=None):
        self.pos = pos
        self.image = image
        self._name = name
        self.examineTxt = examine
        self.useTxt = useTxt
        self.useSound = useSound

    @property
    def name(self):
        return self._name

    # Just to simplfy this call
    def get_rect(self):
        return self.image.get_rect(topleft=self.pos)
    
    # Selectables that don't just say it's useTxt should override this method
    def use(self, state, assets):
        state.dialog = self.useTxt
        if self.useSound is not None:
            self.useSound.play()
        return (state, assets)

    # Should be overidden with conditional uses with other items. These typically should only check for one other selectable type.
    def useWith(self, state, assets):
        state.dialog = "Those don't do anything together."
        return (state, assets)

    def examine(self, state, assets):
        state.dialog = self.examineTxt
        return (state, assets)

# Base class for NPCs
class NPC(Selectable):
    def __init__(self, pos, name="", image=None, examine="", dialogTree={}):
        super().__init__(pos=pos, name=name, image=image, examine=examine)
        self.dialogTree = dialogTree
    
    def use(self, state, assets):
        state.currDialogTree = self.dialogTree
        return startDialog(state=state, assets=assets)

    def useWith(self, state, assets):
        state.dialog = "They don't want that."
        return (state, assets)

class JomsSrPast(NPC):
    def useWith(self, state, assets):
        if state.selectedItem == assets.spaceJam:
            state.currRoom.selectables.remove(self)
            self.pos = assets.jomsSr.pos
            assets.pastLivingRoom.selectables.append(self)
            state.dialog = "\"Could that be? It is! A MINT CONDITION SPACE JAM DVD! I must watch it right away!\" Just like that, Joms Sr runs into the living room to watch the Space Jam DVD."
            return (state, assets)
        else:
            return super().useWith(state, assets)

class Beacoi(NPC):
    def useWith(self, state, assets):
        if state.selectedItem == assets.batItem:
            if not state.isGirl:
                state.currDialogTree = assets.dialogTrees["beacoiWinDialog"]
                startDialog(state, assets)
                state.currInventory.append(assets.spaceJam)
                state.currInventory.remove(state.selectedItem)
                return (state, assets)
            else:
                state.dialog = "Sorry miss, but girls aren't allowed to fight in Beacoi's Fight Club. Please come back on Thursday for the Women's league."
                return (state, assets)
        else:
            return super().useWith(state,assets)

class Computer(NPC):
    def use(self, state, assets):
        if assets.jomsSrPast in state.currRoom.selectables:
            state.dialog = "I can't use that, Joms Sr is using it."
            return (state, assets)
        else:
            return super().use(state, assets)

class Botseph(NPC):
    def use(self, state, assets):
        if assets.falzar in state.currRoom.selectables:
            state.dialog = "I can't speak to it, the bouncer is in the way."
            return (state, assets)
        else:
            return super().use(state,assets)

class Falzar(NPC):
    def useWith(self,state,assets):
        if state.selectedItem == assets.popcorn:
            state.currRoom.selectables.remove(self)
            state.currInventory.remove(state.selectedItem)
            state.currInventory.append(assets.popcornEmpty)
            state.dialog = "You offer the popcorn to the crocodile who scoops a handful. As they eat the popcorn, its effect is immediate. The crocodile wavers before falling face first onto the floor."
            assets.kritterSfx.play()
            return (state, assets)
        elif state.selectedItem == assets.pizza:
            state.dialog = "The crocodile takes one look at the pineapple pizza and is clearly disgusted by the sight."
            return (state, assets)
        else:
            return super().useWith(state, assets)

class Jelly(NPC):
    def useWith(self, state, assets):
        if state.selectedItem == assets.pizza:
            state.currRoom.selectables.remove(assets.bagChan)
            state.currRoom.selectables.append(assets.bagChanFull)
            state.currInventory.remove(state.selectedItem)
            assets.omnom.play()
            state.dialog = "\"You mean it? Don't mind if I do! Been a while since I got one with the box...\" Bagchan devours the pizza, box and all. You could swear you saw a look of terror on Norm's face before the box disappeared under the bag."
            return (state, assets)
        else:
            return super().useWith(state, assets)

class Train(NPC):
    def use(self, state, assets):
        state.holdClicks = True
        if state.ticketGiven:
            clock.tick(60)
            state.currRoom.song.stop()
            state.currRoom = assets.moncton
            state.currRoom.song.play(-1)
            return (state, assets)
        else:
            return super().use(state, assets)

    def useWith(self, state, assets):
        state.holdClicks = True
        if state.selectedItem == assets.trainTicket:
            state.dialog = "(You give Choo Choo Charon the ticket.) Next stop, Iraq! Hop onboard!"
            state.ticketGiven = True
            state.currInventory.remove(state.selectedItem)
        else:
            return super().useWith(state, assets)
        return (state, assets)

class PastMoms(NPC):
    def useWith(self, state, assets):
        if state.selectedItem == assets.greatVegetables:
            state.isGirl = True
            state.currInventory.remove(assets.greatVegetables)
            assets.timeShift.play()
            state.dialog = "You feed Moms the GREAT VEGETABLES. You feel different somehow."
            assets.portrait.image = pygame.image.load("graphics/JomsGirl.png")
        elif state.selectedItem == assets.chicken:
            state.isGirl = False
            assets.timeShift.play()
            state.dialog = "You feed Moms a piece of the Roast Karu. You feel different somehow."
            assets.portrait.image = pygame.image.load("graphics/Joms.jpg")
        else:
            return super().useWith(state, assets)
        return (state, assets)

class FrozenKaru(NPC):
    def useWith(self, state, assets):
        if state.selectedItem == assets.heaterFueled:
            state.dialog = "You attempt to heat up Karu."
            state.currInventory.remove(state.selectedItem)
            state.currRoom.selectables.remove(self)
            state.currRoom.selectables.append(assets.fireKaru)
            state.karuOnFire = True
            assets.fireSound.play()
            return (state, assets)
        else:
            return super().useWith(state, assets)

class Nodja(NPC):
    def useWith(self, state, assets):
        if state.selectedItem == assets.microwaveItem:
            state.selectedItem = None
            state.currInventory.remove(assets.microwaveItem)
            state.currInventory.append(assets.phoneWaveItem)
            assets.wrenchSound.play()
            state.dialog = "A broken microwave huh? I can fix this and make a few improvements."
        else:
            return super().useWith(state, assets)
        return (state, assets)

# Base class for exits
# TODO I could probably make this a selectable idk
class Exit(object):
    def __init__(self, rect, name="", newLoc=""):
        self.rect = rect
        self.newLoc = newLoc
        self.name = name

    def get_rect(self):
        return self.rect

    def enterRoom(self, state, assets):
        # Change song if needed
        if (state.currRoom.song != (newRoom := assets.roomLookup[exit.newLoc]).song):
            if state.currRoom.song is not None:
                state.currRoom.song.stop()
            if newRoom.song is not None:
                newRoom.song.play(-1)
        state.currRoom = newRoom
        state.dialog=""
        for enterEvent in state.currRoom.enterEvents:
            state, assets = eventLookup[enterEvent](state, assets)
        return (state, assets)

class BathroomExit(Exit):
    def enterRoom(self, state, assets):
        if state.isGirl:
            return super().enterRoom(state, assets)
        else:
            state.dialog = "I can't go into the girl's bathroom. I'm a boy!"
            return (state, assets)

class Trapdoor(Exit):
    def enterRoom(self, state, assets):
        if assets.falzar in state.currRoom.selectables:
            state.dialog = "I can't go there, the bouncer is in way."
            return (state, assets)
        return super().enterRoom(state, assets)

# Item class specifically for being put into your inventory. Probably doesn't need its own class.
class Item(Selectable):
    def useWith(self, state, assets):
        state.dialog = "Those don't do anything together."
        return (state, assets)

class Heater(Item):
    def useWith(self, state, assets):
        if state.selectedItem.name == "High-Proof Alchohol":
            assets.bagSound.play()  
            state.currInventory.remove(self)
            state.currInventory.append(assets.heaterFueled)
            state.currInventory.remove(state.selectedItem)
            state.dialog = "You fuel up the Portable Heater (Fuel not Included) with the High-Proof Alchohol"
            return (state, assets)
        else:
            return super().useWith(state, assets)

class PlotPast(Selectable):
    def useWith(self, state, assets):
        if state.selectedItem == assets.popcornEmpty:
            state.currInventory.remove(state.selectedItem)
            state.currRoom.selectables.remove(self)
            state.currRoom.selectables.append(assets.plotPlantedPast)
            assets.garden.selectables.remove(assets.weedPlot)
            assets.garden.selectables.append(assets.vegetablesPlot)
            state.dialog = "You sowed the garden with the popcorn kernels"
            return (state, assets)
        else:
            return super().useWith(state, assets)

class VegetablesPlot(Selectable):
    def use(self, state, assets):
        assets.gvSfx.play()
        if assets.greatVegetables not in state.currInventory:
            state.dialog = "GREAT VEGETABLES GREAT VEGETABLES GREAT VEGETABLES GREAT VEGETABLES GREAT VEGETABLES GREAT VEGETABLES GREAT VEGETABLES"
            state.currInventory.append(assets.greatVegetables)
        else:
            state.dialog = "GREAT VEGETABLES!"
        return state, assets

class Pickupable(Selectable):
    def __init__(self, pos, invItem, name="", image=None, examine="", useTxt="I can't use that"):
        super().__init__(pos, name, image, examine, useTxt)
        self.invItem = invItem

    def use(self, state, assets):
        state.dialog = f"You took the {self.name}"
        state.currInventory.append(self.invItem)
        state.currRoom.selectables.remove(self)
        assets.bagSound.play()
        return (state, assets)

class ScorchedFountain(Pickupable):
    def use(self, state, assets):
        state, assets = super().use(state,assets)
        state.currRoom.selectables.append(assets.scorchedFountain)
        return (state, assets)

class Microwave(Pickupable):
    def use(self, state, assets):
        state, assets = super().use(state, assets)
        state.dialog = "You picked up the Broken Microwave"
        state.currRoom.selectables.append(assets.socket)
        return (state, assets)

class BatRack(Pickupable):
    def use(self, state, assets):
        state, assets = super().use(state, assets)
        state.holdClicks = True
        state.currRoom.selectables.append(assets.batRackEmpty)
        state.dialog = "You took the bat off the rack."
        return(state, assets)

class PhoneWaveActive(Selectable):
    def use(self, state, assets):
        assets.timeTravelSound.play()
        if state.currRoom == assets.kitchen:
            state.currRoom = assets.pastKitchen
        else:
            state.currRoom = assets.kitchen
        return (state, assets)

class Pot(Selectable):
    def use(self, state, assets):
        state.dialog = "You stirred the pot! Congratulations."
        return (state, assets)

class TrashCan(Selectable):
    def use(self, state, assets):
        if assets.popcorn in state.currInventory:
            state.dialog = "One handful of dirty popcorn is enough for me."
        else:
            state.dialog = "You rummage through the trash and pick up a handful of Dirty Popcorn."
            state.currInventory.append(assets.popcorn)
        return (state, assets)

class Fridge(Selectable):
    def use(self, state, assets):
        if state.drinkInFridge and state.currRoom == assets.kitchen:
            state.currInventory.append(assets.highProofDrink)
            state.drinkInFridge = False
            assets.bagSound.play()
            state.dialog = "Looks like the juice fermented into alchohol. (You Recieved High-Proof Alchohol)"
            return (state, assets)
        else:
            return super().use(state, assets)

    def useWith(self, state, assets):
        if state.currRoom == assets.pastKitchen and state.selectedItem == assets.juice:
            state.drinkInFridge = True
            state.currInventory.remove(state.selectedItem)
            state.dialog = "You put the Juice into the fridge."
        else:
            return super().useWith(state, assets)
        return (state, assets)

class Socket(Selectable):
    def useWith(self, state, assets):
        # TODO change this to time machine later
        if state.selectedItem.name == "PhoneWave (Name Subject To Change)":
            state.dialog = f"You plugged in the {state.selectedItem.name}"
            state.currRoom.selectables.remove(self)
            state.currInventory.remove(state.selectedItem)
            state.currRoom.selectables.append(assets.phoneWave)
            state.selectedItem = None
            return (state, assets)
        else:
            return super().useWith(state, assets)

class BreakGlass(Selectable):
    def useWith(self, state, assets):
        if state.selectedItem.name == "Brick":
            if state.karuOnFire:
                assets.glassBreak.play()
                state.currRoom.selectables.remove(self)
                state.currRoom.selectables.append(assets.keypad)
            else:
                state.dialog = "There's no emergancy. I shouldn't break the glass."
        return (state, assets)

# Global Inventory Icon
class Bag(Selectable):
    def __init__(self, pos, name="", image=None, examine="", useTxt="I can't use that"):
        super().__init__(pos, name, image, examine, useTxt)
        self.invOpen = False

    @property
    def name(self):
        if self.invOpen:
            return "Close Inventory"
        else:
            return "Open Inventory"

    def use(self, state, assets):
        if self.invOpen:
            self.invOpen = False
            return (state, assets)
        self.invOpen = True
        return openInventory(state, assets)

# Character portrait
class Joms(Selectable):
    def useWith(self, state, assets):
        if isinstance(state.selectedItem, Item):
            state.dialog = f"You aren't hungry."
            return (state, assets)


# The current state of the game. All the flags and stuff is stored here.
class State(object):
    def __init__(self, assets):
        self.currSong = None
        self.dialog = ""
        self.hoverText = ""
        self.currDialogTree = assets.dialogTrees["mainMenu"]
        self.currNode = "start"
        self.holdClicks = False
        # TODO change to main menu room
        self.currRoom = assets.titleScreen
        self.currInventory = []
        self.selectedItem = None
        self.examScore = 0
        self.karuOnFire = False
        self.isGirl = False
        self.drinkInFridge = False
        self.ticketGiven = False
        self.checkedItemsForPizza = False


# Container for all the instances of things the game uses. Inefficient but fuck it.
class Assets(object):
    def __init__(self):
        # Music
        self.jomaliaSong = pygame.mixer.Sound("Audio/JomsSong.wav")
        self.girlsBathroomSong = pygame.mixer.Sound("Audio/girlsBathroomSong.mp3")
        self.monctonSong = pygame.mixer.Sound("Audio/monctonSong.mp3")
        self.monctonSong.set_volume(.3)
        self.classroomSong = pygame.mixer.Sound("Audio/classroomSong.mp3")
        self.classroomSong.set_volume(.3) 

        # Sounds
        self.kritterSfx = pygame.mixer.Sound("Audio/kritter.mp3")
        self.joeWhat = pygame.mixer.Sound("Audio/WHAT.wav")
        self.joeWhat.set_volume(.3)
        self.mayuri = pygame.mixer.Sound("Audio/mayuri.mp3")
        self.mayuri.set_volume(.2)
        self.quoi = pygame.mixer.Sound("Audio/quoi.mp3")
        self.quoiPanic = pygame.mixer.Sound("Audio/quoiPanic.mp3")
        self.bagSound = pygame.mixer.Sound("Audio/bagSound.mp3")
        self.omnom = pygame.mixer.Sound("Audio/omnom.mp3")
        self.oof = pygame.mixer.Sound("Audio/oof.mp3")
        self.oof.set_volume(.5)
        self.wrenchSound = pygame.mixer.Sound("Audio/wrenchSound.mp3")
        self.gvSfx = pygame.mixer.Sound("Audio/great_vegetables.wav")
        self.gvSfx.set_volume(.2)
        self.winSound = pygame.mixer.Sound("Audio/win.mp3")
        self.winSound.set_volume(.2)
        self.glassBreak = pygame.mixer.Sound("Audio/glassBreak.mp3")
        self.glassBreak.set_volume(.3)
        self.timeTravelSound = pygame.mixer.Sound("Audio/timeTravelSound.mp3")
        self.timeTravelSound.set_volume(.3)
        self.timeShift = pygame.mixer.Sound("Audio/timeShift.mp3")
        self.timeShift.set_volume(.3)
        self.homerun = pygame.mixer.Sound("Audio/homerun.mp3")
        self.homerun.set_volume(.2)
        self.sprinklerSound = pygame.mixer.Sound("Audio/sprinklerSound.mp3")
        self.sprinklerSound.set_volume(.3)
        self.fireSound = pygame.mixer.Sound("Audio/fireSound.mp3")
        self.fireSound.set_volume(.3)
        self.freezeSound = pygame.mixer.Sound("Audio/freezeSound.mp3")
        self.freezeSound.set_volume(.3)

        self.soundLookup = {
            "mayuri": self.mayuri,
            "quoi": self.quoi,
            "quoiPanic": self.quoiPanic,
            "oof": self.oof,
            "winSound": self.winSound,
            "freezeSound": self.freezeSound,
            "bagSound": self.bagSound,
            "homerun": self.homerun,
            "sprinklerSound": self.sprinklerSound,
        }


        # Dialog trees
        self.dialogTrees = {
            "mainMenu": mainMenu,
            "settingsMenu": settingsMenu,
            "quizDialog": quizDialog,
            "phoneWaveDialog": phoneWaveDialog,
            "keypadDialog": keypadDialog,
            "momsDialog": momsDialog,
            "jomsSrDialog": jomsSrDialog,
            "inventorDialog": inventorDialog,
            "trainDialog": trainDialog,
            "karuDialog": karuDialog,
            "frozenKaruDialog": frozenKaruDialog,
            "fireKaruDialog": fireKaruDialog,
            "thermostatDialog": thermostatDialog,
            "normDialog": normDialog,
            "computerDialog": computerDialog,
            "pastComputerDialog": pastComputerDialog,
            "bagChanDialog": bagChanDialog,
            "bagChanStuffedDialog": bagChanStuffedDialog,
            "falzarDialog": falzarDialog,
            "botsephDialog": botsephDialog,
            "beacoiDialog": beacoiDialog,
            "beacoiWinDialog": beacoiWinDialog,
        }

        # Inventory Items
        brickExamine = "A kitchen brick. A useful cooking tool and nutritious too."
        brickImage = pygame.transform.scale(pygame.image.load("graphics/brick.png"), (100,50))
        self.brickItem = Item(pos=(0,0), name="Brick", image=brickImage, examine=brickExamine)
        mwExamine = "It's a Genbu'd Microwave."
        microwaveImage = pygame.transform.scale(pygame.image.load("graphics/microwave.png"), (100,50))
        self.microwaveItem = Item(pos=(0,0), name="Broken Microwave", image=microwaveImage, examine=mwExamine)
        pwImage = pygame.transform.scale(pygame.image.load("graphics/phonewave.png"), (100,50))
        self.phoneWaveItem = Item(pos=(0,0), name="PhoneWave (Name Subject To Change)", image=pwImage, examine="It's the PhoneWave (Name Subject to Change)!")
        trainTicketImage = pygame.transform.scale(pygame.image.load("graphics/trainTicket.png"), (100,100))
        self.trainTicket = Item(pos=(0,0), name="Train Ticket", image=trainTicketImage, examine="A round trip pass on the Maroon Vista train line.")
        batItem = pygame.transform.scale(pygame.image.load("graphics/bat.png"), (100,100))
        self.batItem = Item(pos=(0,0), name="Baseball Bat", image=batItem, examine="I better be careful, this is a deadly weapon.")
        self.popcorn = Item(pos=(0,0), name="Suspect Popcorn", image=pygame.image.load("graphics/popcorn.png"), examine="A bag of dirty popcorn I found in the trash.")
        chickenItem = pygame.transform.scale(pygame.image.load("graphics/Karu_Cooked.png"), (100,100))
        self.chicken = Item(pos=(0,0), name="Roasted Karu", image=chickenItem, examine="Roasted Karu, cooked to perfection!")
        self.highProofDrink = Item((0,0), name="High-Proof Alchohol", image=pygame.image.load("graphics/bottle.png"), examine="I don't think I'm old enough to have this.")
        self.juice = Item((0,0), name="Juice Box", image=pygame.image.load("graphics/juice.png"), examine="A fruity drink that never expires.")
        self.heater = Heater((0,0), name="Portable Heater (Fuel Not Included)", image=pygame.image.load("graphics/heater.png"), examine="This is useless without fuel.")
        self.heaterFueled = Item((0,0), name="Portable Heater (Fuel Included)", image=pygame.image.load("graphics/heaterFueled.png"), examine="This is useless without fuel.")
        self.popcornEmpty = Item((0,0), name="Popcorn Kernels", image=pygame.image.load("graphics/emptyPopcorn.png"), examine="There's nothing left except for popcorn kernels.")
        self.greatVegetables = Item((0,0), name="GREAT VEGETABLES", image=pygame.image.load("graphics/greatVegetables.png"), examine="GREAT VEGETABLES")
        self.pizza = Item((0,0), name="Norm's Pineapple Pizza", image=pygame.image.load("graphics/pizza.png"), examine="Pineapple on Pizza? The perfect balance of sweet and savory!")
        self.spaceJam = Item((0,0), name="Space Jam DVD", image=pygame.image.load("graphics/spaceJam.png"), examine="A Space Jam DVD with a very low resolution PNG Icon. A Space Jam DVD PNG.")

        # Selectables
        self.portrait = Joms(pos=(1180,0), name="Joms", image=pygame.image.load("graphics/Joms.jpg"), examine="It's me, Joms!", useTxt="Moms told me I shouldn't touch myself.")
        self.bag = Bag(pos=(1080,0), name="Open Inventory", image=pygame.image.load("graphics/bag.png"), examine="It's my bag.")
        self.settings = NPC(pos=(0,0), name="Settings", image=pygame.image.load("graphics/settings.png"), examine="A hastily drawn cogwheel", dialogTree=self.dialogTrees["settingsMenu"])
        self.computer = Computer(pos=(550,350), name="Use Computer", image=pygame.image.load("graphics/Computer.png"), examine="My old computer I use to browse dank memes.", dialogTree=self.dialogTrees["computerDialog"])
        self.computerPast = Computer(pos=(550,350), name="Use Computer", image=pygame.image.load("graphics/ComputerPast.png"), examine="A new computer Joms Sr uses to browse dank memes.", dialogTree=self.dialogTrees["pastComputerDialog"])
        self.bed = Selectable(pos=(0,330), name="Bed", image=pygame.image.load("graphics/bed.png"), examine="Even though it's a waste of time, I like to make my bed every morning.")
        self.bedPast = Selectable(pos=(0,330), name="Bed", image=pygame.image.load("graphics/bedPast.png"), examine="Looks like Joms Sr also wastes his time making his bed each morning.")
        self.weedPlot = Selectable(pos=(80,435), name="Weed-Filled Garden", image=pygame.image.load("graphics/plotWeeds.png"), examine="No one has weeded this garden in years.")
        self.plotPast = PlotPast(pos=(80,435), name="Weed-Free Garden", image=pygame.image.load("graphics/plotPast.png"), examine="Looks like this was the last time the garden was weeded.")
        self.plotPlantedPast = PlotPast(pos=(80,435), name="Weed-Free Garden", image=pygame.image.load("graphics/pastPlotPlanted.png"), examine="The garden has been planted with popcorn kernels.")
        self.vegetablesPlot = VegetablesPlot(pos=(80,435), name="GREAT VEGETABLES!", image=pygame.image.load("graphics/plotVegetables.png"), examine="GREAT VEGETABLES!")
        self.brick = Pickupable(pos=(490,318), invItem=self.brickItem, name="Kitchen Brick", image=pygame.image.load("graphics/brick.png"), examine=brickExamine)
        self.oven = Selectable(pos=(173,312), name="Oven", image=pygame.image.load("graphics/oven.png"), examine="Looks like chocolate chip-less chocolate chip cookies are being baked. Delicious!", useTxt="The chocolate chipless chocolate chip cookies aren't finished yet.")
        self.ovenPast = Selectable(pos=(173,312), name="Oven", image=pygame.image.load("graphics/oven.png"), examine="Our oven. Looks like Moms is cooking dinner.")
        self.fridge = Fridge(pos=(891,110), name="Fridge", image=pygame.image.load("graphics/fridge.png"), examine="There's nothing in it except some expired fruit.", useTxt="There's nothing in there that I want.")
        self.fridgePast = Fridge(pos=(891,110), name="Fridge", image=pygame.image.load("graphics/fridge.png"), examine="There's nothing in it except some ripe fruit.", useTxt="There's nothing in there that I want.")
        self.pot = Pot(pos=(190,260), name="Pot", image=pygame.image.load("graphics/pot.png"), examine="A pot of Moms' famous unsalted minced meat.")
        self.microwave = Microwave(pos=(170,129), invItem=self.microwaveItem, name="Microwave", image=pygame.image.load("graphics/microwave.png"), examine=mwExamine)
        self.socket = Socket(pos=(250,145), name="Electrical Outlet", image=pygame.image.load("graphics/socket.png"), examine="An electrical outlet.")
        self.phoneWaveActive = PhoneWaveActive(pos=(170,129), name="PhoneWave (Name Subject To Change)", image=pygame.image.load("graphics/phonewaveActive.png"), examine="It's the PhoneWave (Name Subject to Change)!")
        self.breakGlass = BreakGlass(pos=(500,330), name="Emergency Break Glass", image=pygame.image.load("graphics/breakGlass.png"), examine="\"Incase of emergancy, break glass.\"")
        self.sprinkler1 = Selectable(pos=(475,110), name="Sprinkler", image=pygame.image.load("graphics/sprinklersOff.png"), examine="An emergancy sprinkler programmed to turn on at 7:30.")
        self.sprinkler2 = Selectable(pos=(910,110), name="Sprinkler", image=pygame.image.load("graphics/sprinklersOff.png"), examine="An emergancy sprinkler programmed to turn on at 7:30.")
        self.batRack = BatRack(pos=(1050,550), invItem=self.batItem, name="Bat Rack", image=pygame.image.load("graphics/batRack.png"), examine="A bat rack, it's a rack for bats, a bat rack.")
        self.batRackEmpty = Selectable(pos=(1050,550), name="Bat Rack", image=pygame.image.load("graphics/batRackEmpty.png"), examine="I don't even own a bat, let alone many bats that would nessesitate a rack.")
        self.trashCan = TrashCan(pos=(170,400), name="Trash Can", image=pygame.image.load("graphics/trashCan.png"), examine="A dirty trashcan with a bag of uneaten popcorn ontop.")
        self.sink = Selectable(pos=(203,305), name="Sink", image=pygame.image.load("graphics/sink.png"), examine="A dirty sink.", useTxt="I don't need to pee.")
        self.stadium = Selectable(pos=(940,310), name="Stadium", image=pygame.image.load("graphics/stadium.png"), examine="The world famous Moncton Stadium", useTxt="There's nothing happening there.")
        self.cave = Selectable(pos=(0,240), name="Dragon's Den", image=pygame.image.load("graphics/dragonsDen.png"), examine="\"Beware of Dragon\"", useTxt="You hear a terrifying roar and decide not to enter.", useSound=self.joeWhat)
        # Global selectables container
        self.global_selectables = [self.bag, self.settings, self.portrait]

        # NPCs
        self.phoneWave = NPC(pos=(170,129), name="PhoneWave", image=pygame.image.load("graphics/phonewave.png"), examine="It's the PhoneWave (Name Subject To Change)", dialogTree=self.dialogTrees["phoneWaveDialog"])
        self.keypad = NPC(pos=(500,330), name="Emergancy Keypad", image=pygame.image.load("graphics/keypad.png"), examine="How does this help in the event of an emergancy?", dialogTree=self.dialogTrees["keypadDialog"])
        self.moms = NPC(pos=(400,300), name="Moms", image=pygame.image.load("graphics/moms.png"), examine="It's Momma Joms, Moms!", dialogTree=self.dialogTrees["momsDialog"])
        self.momsPast = PastMoms(pos=(400,300), name="Moms", image=pygame.image.load("graphics/momsPast.png"), examine="It's Momma Joms, Moms!", dialogTree=self.dialogTrees["momsDialog"])
        self.jomsSr = NPC(pos=(800,300), name="Joms Sr.", image=pygame.image.load("graphics/jomsSr.png"), examine="It's my dad, Joms Sr!", dialogTree=self.dialogTrees["jomsSrDialog"])
        self.jomsSrPast = JomsSrPast(pos=(650,300), name="Joms Sr.", image=pygame.image.load("graphics/jomsSrPast.png"), examine="It's my dad, Joms Sr!", dialogTree=self.dialogTrees["jomsSrDialog"])
        self.kusoro = NPC(pos=(0,220), name="Hastily Drawn Axolotl Professor", image=pygame.image.load("graphics/kusoro.png"), examine="It's my teacher, Hastily Drawn Axolotl Professor.", dialogTree=self.dialogTrees["quizDialog"])
        self.nodja = Nodja(pos=(365,300), name="Suspicious Inventor", image=pygame.image.load("graphics/nodja.png"), examine="Suspicious blue man hanging out in the bathroom", dialogTree=self.dialogTrees["inventorDialog"])
        self.train = Train(pos=(500,0), name="Choo Choo Charon", image=pygame.image.load("graphics/train.png"), examine="Hop aboard the Maroon Vista!", dialogTree=self.dialogTrees["trainDialog"])
        fountainOnImg = pygame.transform.scale(pygame.image.load("graphics/Fountain_On.png"), (400,333))
        fountainIceImg = pygame.transform.scale(pygame.image.load("graphics/Fountain_Ice.png"), (400,333))
        fountainFireImg = pygame.transform.scale(pygame.image.load("graphics/Fountain_Fire.png"), (400,333))
        fountainChickenImg = pygame.transform.scale(pygame.image.load("graphics/Fountain_Chicken.png"), (400,333))
        fountainScorchImg = pygame.transform.scale(pygame.image.load("graphics/Fountain_Scorched.png"), (400,333))
        self.karu = NPC(pos=(500,300), name="Karu", image=fountainOnImg, examine="It's Karu swimming in the fountain.", dialogTree=self.dialogTrees["karuDialog"])
        self.frozenKaru = FrozenKaru(pos=(500,300), name="Frozen Karu", image=fountainIceImg, examine="It's Karu frozen solid in the fountain.", dialogTree=self.dialogTrees["frozenKaruDialog"])
        self.fireKaru = NPC(pos=(500,300), name="Flaming Karu", image=fountainFireImg, examine="Damn, Karu's looking hot.", dialogTree=self.dialogTrees["fireKaruDialog"])
        self.chickenKaru = ScorchedFountain(pos=(500,300), invItem=self.chicken, name="Cooked Karu", image=fountainChickenImg, examine="I may have been slightly too late turning on the sprinklers.")
        self.scorchedFountain = Selectable(pos=(500,300), name="Scorched Fountain", image=fountainScorchImg, examine="It's a fountain, slightly scorched.")
        self.thermostat = NPC(pos=(180,380), name="Thermostat", image=pygame.image.load("graphics/thermostat.png"), examine="Joms Sr doesn't let me mess with our thermostat at home not since the incident.", dialogTree=self.dialogTrees["thermostatDialog"])
        self.normChan = NPC(pos=(430,130), name="Norm-chan", image=pygame.image.load("graphics/normChan.png"), examine="The very handsome owner of this fine establishment.", dialogTree=self.dialogTrees["normDialog"])
        bagChanImage = pygame.transform.scale(pygame.image.load("graphics/Jelly_Normal.png"), (100,200))
        bagChanStuffedImage = pygame.transform.scale(pygame.image.load("graphics/Jelly_Stuffed.png"), (100,200))
        self.bagChan = Jelly(pos=(440,375), name="Jelly", image=bagChanImage, examine="It's world famous streamer/entertainer Jelly", dialogTree=self.dialogTrees["bagChanDialog"])
        self.bagChanFull = NPC(pos=(440,375), name="Stuffed Jelly", image=bagChanStuffedImage, examine="Jelly's insatiable trash-lust has been satisfied... for now...", dialogTree=self.dialogTrees["bagChanStuffedDialog"])
        falzarImage = pygame.transform.scale2x(pygame.image.load("graphics/Bouncer_Falzar.png"))
        self.falzar = Falzar((500,0), name="Crocodile with Style", image=falzarImage, examine="A hostile crocodile with style is blocking the entrance.", dialogTree=self.dialogTrees["falzarDialog"])
        self.botseph = Botseph((300,110), name="Botseph", image=pygame.image.load("graphics/botseph.png"), examine="The bartender of the very originally named \"Bar\"", dialogTree=self.dialogTrees["botsephDialog"])
        self.beacoi = Beacoi((600,400), name="Beacoi Ofsnoe", image=pygame.image.load("graphics/Knife_Beacoi.png"), examine="The fearsome Beacoi Ofsnoe with his razer sharp knife-like talons.", dialogTree=self.dialogTrees["beacoiDialog"])

        # Rooms
        self.titleScreen = Room(name="title", bg=pygame.image.load("graphics/titleScreen.png"), selectables=[], exits=[])
        self.bedroom = Room(name="bedroom", bg=pygame.image.load("graphics/Bedroom.png"), selectables=[self.computer, self.bed], exits=[Exit(rect=pygame.Rect(1000, 130, 200, 420), newLoc="livingRoom", name="Go to Living Room")], song=self.jomaliaSong)
        self.pastBedroom = Room(name="bedroom", bg=pygame.image.load("graphics/bedroombgPast.png"), selectables=[self.computerPast, self.bedPast, self.jomsSrPast], exits=[Exit(rect=pygame.Rect(1000, 130, 200, 420), newLoc="pastLivingRoom", name="Go to Living Room")], song=self.jomaliaSong)
        self.livingRoom = Room(
            name="livingRoom",
            bg=pygame.image.load("graphics/livingroom.png"),
            selectables=[self.moms, self.jomsSr],
            exits=[
                Exit(rect=pygame.Rect(155, 160, 150, 300), newLoc="bedroom", name="Go to Bedroom"),
                Exit(rect=pygame.Rect(1180, 170, 100, 400), newLoc="garden", name="Go Outside"),
                Exit(rect=pygame.Rect(0, 150, 60, 400), newLoc="kitchen", name="Go to Kitchen"),
            ],
            song=self.jomaliaSong,
        )
        self.pastLivingRoom = Room(
            name="pastLivingRoom",
            bg=pygame.image.load("graphics/livingroomPast.png"),
            selectables=[self.momsPast],
            exits=[
                Exit(rect=pygame.Rect(155, 160, 150, 300), newLoc="pastBedroom", name="Go to Bedroom"),
                Exit(rect=pygame.Rect(1180, 170, 100, 400), newLoc="pastGarden", name="Go Outside"),
                Exit(rect=pygame.Rect(0, 150, 60, 400), newLoc="pastKitchen", name="Go to Kitchen"),
            ],
            song=self.jomaliaSong,
        )
        self.garden = Room(name="garden", bg=pygame.image.load("graphics/jomsHousebg.png"), selectables=[self.weedPlot], exits=[Exit(rect=pygame.Rect(400, 350, 40, 110), newLoc="livingRoom", name="Go Inside"), Exit(rect=pygame.Rect(1180, 200, 100, 520), newLoc="townSquare", name="Go to Town")], song=self.jomaliaSong)
        self.pastGarden = Room(name="pastGarden", bg=pygame.image.load("graphics/jomsHousebgPast.png"), selectables=[self.plotPast], exits=[Exit(rect=pygame.Rect(400, 350, 40, 110), newLoc="pastLivingRoom", name="Go Inside")], song=self.jomaliaSong)
        self.kitchen = Room(name="kitchen", bg=pygame.image.load("graphics/kitchen.png"), selectables=[self.brick, self.microwave, self.oven, self.pot, self.fridge], exits=[ Exit(rect=pygame.Rect(1180, 170, 100, 400), newLoc="livingRoom", name="Go to Living Room")], song=self.jomaliaSong)
        self.pastKitchen = Room(name="pastKitchen", bg=pygame.image.load("graphics/kitchenPast.png"), selectables=[self.phoneWaveActive, self.ovenPast, self.fridgePast], exits=[ Exit(rect=pygame.Rect(1180, 170, 100, 400), newLoc="pastLivingRoom", name="Go to Living Room")], song=self.jomaliaSong)
        self.townSquare = Room(
            name="townSquare",
            bg=pygame.image.load("graphics/townSquare.png"),
            selectables=[self.bagChan],
            exits=[
                Exit(rect=pygame.Rect(0, 620, 1280, 100), newLoc="garden", name="Go to Joms' House"),
                Exit(rect=pygame.Rect(50, 300, 300, 200), newLoc="bar", name="Go to Bar"),
                Exit(rect=pygame.Rect(920, 305, 350, 190), newLoc="school", name="Go to School"),
                Exit(rect=pygame.Rect(405, 105, 500, 200), newLoc="trainStation", name="Go to Train Station"),
            ],
            enterEvents=["takePopcorn"],
            song=self.jomaliaSong,
        )
        self.school = Room(
            name="school",
            bg=pygame.image.load("graphics/school.png"),
            selectables=[self.breakGlass],
            exits=[
                Exit(rect=pygame.Rect(1150, 170, 300, 600), newLoc="townSquare", name="Go to Town"),
                Exit(rect=pygame.Rect(25, 170, 210, 400), newLoc="classroom", name="Go to Classroom"),
                Exit(rect=pygame.Rect(700, 180, 175, 400), newLoc="boysBathroom", name="Got to Boy's Bathroom"),
                BathroomExit(rect=pygame.Rect(920, 180, 175, 400), newLoc="girlsBathroom", name="Got to Girl's Bathroom"),
            ],
            song=self.jomaliaSong,
        )
        self.classroom = Room(name="classroom", bg=pygame.image.load("graphics/classroom.png"), selectables=[self.kusoro], exits=[Exit(rect=pygame.Rect(1180, 170, 100, 400), newLoc="school", name="Go to Hallway")], song=self.classroomSong)
        self.boysBathroom = Room(name="boysBathroom", bg=pygame.image.load("graphics/boysBathroom.png"), selectables=[self.nodja, self.sink], exits=[Exit(rect=pygame.Rect(0,160,90,500), newLoc="school", name="Go to Hallway")], song=self.jomaliaSong)
        self.girlsBathroom = Room(name="girlsBathroom", bg=pygame.image.load("graphics/girlsBathroom.png"), selectables=[self.sprinkler1, self.sprinkler2, self.batRack, self.thermostat, self.karu], exits=[Exit(rect=pygame.Rect(0,160,160,500), newLoc="school", name="Go to Hallway")], song=self.girlsBathroomSong)
        self.trainStation = Room(name="trainStation", bg=pygame.image.load("graphics/trainStation.png"), selectables=[self.trashCan, self.train], exits=[Exit(rect=pygame.Rect(0, 650, 1280, 100), newLoc="townSquare", name="Go to Town")], song=self.jomaliaSong)
        self.bar = Room(
            name="bar",
            bg=pygame.image.load("graphics/bar.png"),
            selectables=[self.falzar, self.botseph],
            exits=[
                Exit(rect=pygame.Rect(0, 650, 500, 200),newLoc="townSquare", name="Go to Town"),
                Exit(rect=pygame.Rect(0, 140, 150, 500),newLoc="townSquare", name="Go to Town"),
                Trapdoor(rect=pygame.Rect(1070, 490, 200, 150),newLoc="fightClub", name="Enter Trapdoor"),
            ],
            song=self.jomaliaSong,
        )
        self.fightClub = Room(name="fightClub", bg=pygame.image.load("graphics/fightClub.png"), selectables=[self.beacoi], exits=[Exit(rect=pygame.Rect(1100, 134, 300, 420), newLoc="bar", name="Go up ladder")], song=self.jomaliaSong)
        self.moncton = Room(
            name="moncton",
            bg=pygame.image.load("graphics/moncton.png"),
            selectables=[self.cave, self.stadium],
            exits=[
                Exit(rect=pygame.Rect(440, 300, 110, 100), newLoc="trainStation", name="Go to Jomalia"),
                Exit(rect=pygame.Rect(635,350,200,160), newLoc="normsPizza", name="Go to Norm's Pizza"),
            ],
            song=self.monctonSong,
        )
        self.normsPizza = Room(name="normsPizza", bg=pygame.image.load("graphics/normsPizza.png"), selectables=[self.normChan], exits=[Exit(rect=pygame.Rect(0, 620, 1280, 100), newLoc="moncton", name="Go to Moncton")], song=self.monctonSong)

        # LEFT, TOP, WIDTH, HEIGHT

        # Room Lookups
        self.roomLookup = {
            "titleScreen": self.titleScreen,
            "" : self.bedroom,
            "bedroom": self.bedroom,
            "pastBedroom": self.pastBedroom,
            "livingRoom" : self.livingRoom,
            "pastLivingRoom": self.pastLivingRoom,
            "garden" : self.garden,
            "pastGarden": self.pastGarden,
            "kitchen" : self.kitchen,
            "pastKitchen": self.pastKitchen,
            "townSquare": self.townSquare,
            "school": self.school,
            "classroom": self.classroom,
            "boysBathroom": self.boysBathroom,
            "girlsBathroom": self.girlsBathroom,
            "trainStation": self.trainStation,
            "bar": self.bar,
            "fightClub": self.fightClub,
            "moncton": self.moncton,
            "normsPizza": self.normsPizza,
        }

        # Other stuff
        self.inv =  pygame.transform.scale(pygame.image.load("graphics/openInv.png"), (1280,720))
        self.codeGeassShirley = pygame.transform.scale(pygame.image.load("graphics/shirley.webp"), (300,200))
        self.confetti = pygame.image.load("graphics/confetti.png")

        self.imageLookup = {
            "codeGeassShirley" : self.codeGeassShirley,
            "confetti": self.confetti,
        }

# Instance a State and Assets object
assets = Assets()
state = State(assets)

def newGame(state, assets):
    assets=None
    state=None
    assets = Assets()
    state = State(assets)
    state.currRoom = assets.bedroom
    return (state, assets)


# Dialog callable functions
def exitGame(state, assets):
    pygame.quit()
    sys.exit()

def resetQuizScore(state, assets):
    state.examScore = 0
    return (state, assets)

def flagStartedQuiz(state, assets):
    assets.dialogTrees["quizDialog"]["start"]["text"] = "Come to retake the exam?"
    state.currDialogTree = assets.dialogTrees["quizDialog"]
    return (state, assets)

def correctAnswer(state, assets):
    state.examScore += 1
    return (state, assets)

def scoreQuiz(state, assets):
    if state.examScore == 5:
        state.currInventory.append(assets.trainTicket)
        # This is gross but it's way too late for me to make it better
        assets.dialogTrees["quizDialog"]["results"]["text"] = "Congratulations, you passed the exam. Now get out of here. (You recieved a Train Ticket!)"
        assets.dialogTrees["quizDialog"]["start"]["text"] = "Go on, enjoy the school trip."
        assets.dialogTrees["quizDialog"]["start"]["options"] = {"1": "Leave"}
        assets.dialogTrees["quizDialog"]["start"]["next"] = {"1": "leave"}
        assets.dialogTrees["quizDialog"]["results"]["image"] = ("confetti", (0,0))
        assets.dialogTrees["quizDialog"]["results"]["sound"] = "winSound"
    else:
        assets.dialogTrees["quizDialog"]["results"]["text"] = f"({state.examScore+1}/6) You did not pass the exam. Maybe try applying youself next time."
    state.currDialogTree = assets.dialogTrees["quizDialog"]
    return (state, assets)

def essayQuestion(state, assets):
    essayPrompt(state, assets, text="Final question: Define a slur.")
    return (state, assets)

def phoneWaveInput(state, assets):
    input = essayPrompt(state, assets, text="Please enter the date you wish to travel to in the objectively correct YY/DD/M Format.")
    if input == "11037" or input == "11/03/7":
        state.currRoom.selectables.remove(assets.phoneWave)
        state.currRoom.selectables.append(assets.phoneWaveActive)
    return (state, assets)

def takePopcorn(state, assets):
    if assets.popcorn in state.currInventory and assets.bagChan in state.currRoom.selectables:
        state.currInventory.remove(assets.popcorn)
        assets.omnom.play()
        state.dialog = "Like a feral beast, Jelly's insatiable trash-lust activates and is unable to stop themselves from devouring your popcorn, bag and all."
        bagChanDialog["start"]["options"]["mine"] = "Hey, that was mine!"
        bagChanDialog["start"]["options"]["eat"] = "How did you even eat that?"
    return (state, assets)

def setTime(state, assets):
    input = essayPrompt(state, assets, text="Please enter the time you wish to set the clocks to.")
    if input == "10" or input == "10:00" or input == "1000" or input =="10:00pm":
        keypadDialog["explain"]["next"] = {"1": "sprinklers"}
        keypadDialog["start"]["next"] = {"1": "leave"}
        assets.sprinkler1.image = pygame.image.load("graphics/sprinklersOn.png")
        assets.sprinkler2.image = pygame.image.load("graphics/sprinklersOn.png")
        assets.girlsBathroom.selectables.remove(assets.fireKaru)
        assets.girlsBathroom.selectables.append(assets.chickenKaru)
    elif input == "730" or input == "7:30" or input == "7:30am":
        keypadDialog["explain"]["next"] = {"1": "730"}
    else:
        keypadDialog["explain"]["next"] = {"1": "nothing"}
    return (state, assets)

def freezeRoom(state, assets):
    state.currRoom.selectables.remove(assets.karu)
    state.currRoom.selectables.append(assets.frozenKaru)
    inventorDialog["start"]["options"]["freeze"] = "Help, Karu is frozen solid!"    
    inventorDialog["start"]["next"]["freeze"] = "freeze"
    thermostatDialog["start"]["options"].pop("1")
    thermostatDialog["start"]["options"].pop("2")
    thermostatDialog["start"]["text"] = "The thermostate controls are frozen solid. It no longer works."
    return (state, assets)

def giveHeater(state, assets):
    assets.bagSound.play()
    state.currInventory.append(assets.heater)
    inventorDialog["start"]["options"].pop("freeze")
    return (state, assets)

def itemsForPizza(state, assets):
    if state.checkedItemsForPizza:
        return (state, assets)
    # Fuck it, no one's going to talk to norm, go get a different item, then talk to norm again
    state.checkedItemsForPizza = True
    items = 0
    for item in state.currInventory:
        if items < 3:
            normDialog["pay"]["options"][item.name] = f"I'll trade you this {item.name}."
            normDialog["pay"]["next"][item.name] = "deny"
        items += 1
    return (state, assets)

def givePizza(state, assets):
    state.currInventory.append(assets.pizza)
    normDialog["start"]["options"].pop("1")
    return (state, assets)

def loseFight(state, assets):
    state.currRoom = assets.bedroom
    return (state, assets)

def checkGirl(state, assets):
    if state.isGirl:
        beacoiDialog["fight?"]["next"]["1"] = "urAGirl"
    else:
        beacoiDialog["fight?"]["next"]["1"] = "weapon"
    return state, assets

def iVoted(state, assets):
    pastComputerDialog["start"]["options"] = {"5": "Turn off computer"}
    assets.timeShift.play()
    computerDialog["youtube"] = {
        "text": "You check Youtube, and there you see it. The Witcher 3 - Worse Than Breaking Bad by Joeseph Anderson. Total runtime 239 Hours and 53 Minutes.",
        "options": {"1": "Watch Witcher 3 Video"},
        "next": {"1": "witcher"},
    }
    return (state, assets)

def giveJuice(state, assets):
    state.currInventory.append(assets.juice)
    botsephDialog["start"]["options"].pop("1")
    return (state, assets)

def credits(state, assets):
    credits_text = [
        ("Director", "PubSub"),
        ("Executive Producer", "PubSub"),
        ("Lead Programmer", "PubSub"),
        ("Lead Writer", "PubSub"),
        ("Storyboarding", "PubSub"),
        ("", "Jelly"),
        ("", "404SamNotFound"),
        ("Joms Quest Title Screen", "404SamNotFound"),
        ("Background Art", "PubSub"),
        ("Sprite Art", "PubSub"),
        ("", "Jelly"),
        ("", "404SamNotFound"),
        ("Music",""),
        ("Joms Quest IV Main Theme", "PubSub"),
        ("Oh Canada", "Calixa Lavallée"),
        ("Miniature Overture", "Pyotr Ilyich Tchaikovsky"),
        ("Specialist in style of Persona 5", "Rohan Adiyodi on Youtube"),
        ("\"You should make Moms romancable\"", "Jelly"),
        ("My Star, My Perfect Silence", "Joms"),
    ]

    # Create a font
    FONT_SIZE = 32
    HEIGHT = 720
    WIDTH = 1280
    BACKGROUND_COLOR = (0, 0, 0)
    CREDITS_SPEED = 2
    TEXT_COLOR = (255, 255, 255)
    font = pygame.font.Font(None, FONT_SIZE)

    # Calculate the total height of the credits
    credits_height = len(credits_text) * FONT_SIZE

    # Initialize the y-position of the credits text
    y_pos = HEIGHT

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Update the y-position to scroll the credits
        y_pos -= CREDITS_SPEED

        # If the credits have scrolled off the screen, reset the y-position
        if y_pos < -credits_height:
            y_pos = HEIGHT

        # # Render and blit the credits text
        for i, (role, name) in enumerate(credits_text):
            textSurf1 = font.render(role, True, TEXT_COLOR)
            textSurf2 = font.render(name, True, TEXT_COLOR)
            text_rect1 = textSurf1.get_rect()
            text_rect1.topleft = (300, y_pos + i * (FONT_SIZE+ 10))
            screen.blit(textSurf1, text_rect1)
            text_rect2 = textSurf2.get_rect()
            text_rect2.topleft = (800, y_pos + i * (FONT_SIZE+ 10))
            screen.blit(textSurf2, text_rect2)

        # Update the display
        pygame.display.flip()

        # Control frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()
    return (state, assets)

# Dictionary to map dialog options to functions
eventLookup = {
    "exitGame" : exitGame,
    "newGame" : newGame,
    "phoneWaveInput": phoneWaveInput,
    "takePopcorn": takePopcorn,
    "setTime": setTime,
    "freezeRoom": freezeRoom,
    "giveHeater": giveHeater,
    "itemsForPizza": itemsForPizza,
    "givePizza": givePizza,
    "loseFight": loseFight,
    "checkGirl": checkGirl,
    "credits": credits,
    "iVoted": iVoted,
    "giveJuice": giveJuice,

    # Quiz
    "resetQuizScore" : resetQuizScore,
    "flagStartedQuiz": flagStartedQuiz,
    "correctAnswer": correctAnswer,
    "scoreQuiz": scoreQuiz,
    "essayQuestion": essayQuestion,
}

# Blocking functions that require user input. These are part of the general gameplay
# Inventory management
def openInventory(state, assets):
    # Draw everything again to clear dialog and hovertext
    drawEverything(state=state, assets=assets)

    while True:
        # Reset Hold Clicks as to not overlap
        state.holdClicks = False
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if event.button == 3:
                    state.selectedItem = None
                # Check if selected a global selectable
                for selectable in assets.global_selectables:
                    if selectable.get_rect().collidepoint(x,y) and not state.holdClicks:
                        if event.button == 3:
                            state, assets = selectable.examine(state, assets)
                        elif event.button == 1:
                            state, assets = selectable.use(state, assets)
                            # Need to specifically check if you close inventory otherwise we'd usewith
                            if selectable == assets.bag:
                                return (state, assets)
                            elif state.selectedItem:
                                state, assets = selectable.useWith(state, assets)
                                state.selectedItem = None
                            else:
                                state, assets = selectable.use(state, assets)

                for invItem in state.currInventory:
                    # Use
                    if invItem.get_rect().collidepoint(x,y):
                        if event.button == 1:
                            if state.selectedItem:
                                state, assets = invItem.useWith(state, assets)
                                state.selectedItem = None
                            else:
                                state.selectedItem = invItem
                        # Examine
                        elif event.button == 3:
                            state, assets = invItem.examine(state, assets)

        # Draw Inventory BG
        screen.blit(assets.inv, (0,0))

        # Update current UI elements
        for selectable in assets.global_selectables:
            screen.blit(selectable.image, selectable.pos)

        # Draw Items
        x = 450
        y = 260
        for item in state.currInventory:
            screen.blit(item.image, (x, y))
            item.pos = (x, y)
            x += 125
            if x >= 875:
                x = 450
                y += 125

        # Update hoverText to whatever the mouse is hovering over
        state = checkHoverText([assets.global_selectables, state.currInventory], state=state)

        # Print out the current texts.
        printText(state.dialog, 640, 600)
        printText(state.hoverText, 640, 100)

        pygame.display.flip()
        # 60 FPS
        clock.tick(60)



################
def essayPrompt(state, assets, text):
    text_color = (255, 255, 255)

    font = pygame.font.Font(None, 32)

    input_text = ""
    input_rect = pygame.Rect(490, 600, 500, 30)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_text
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        # Render input box
        drawEverything(state=state, assets=assets)
        pygame.draw.rect(screen, (100, 100, 100), input_rect)
        text_surface = font.render(input_text, True, text_color)
        width = max(300, text_surface.get_width()+10)
        input_rect.w = width
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        pygame.draw.rect(screen, text_color, input_rect, 2)

        printText(text, 640, 550)

        pygame.display.flip()
        clock.tick(60)



#############
# Actual Game Starts Here
#############
# Main Menu
state.currDialogTree = assets.dialogTrees["mainMenu"]
state, assets = startDialog(state=state, assets=assets)
assets.jomaliaSong.play(-1)

# Main Gameplay Loop
while True:
    state.holdClicks = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if event.button == 3:
                state.selectedItem = None
            # Check if selected a global selectable
            for selectable in assets.global_selectables:
                if selectable.get_rect().collidepoint(x,y) and not state.holdClicks:
                    if event.button == 3:
                        state, assets = selectable.examine(state, assets)
                    elif event.button == 1:
                        if state.selectedItem and selectable != assets.bag:
                            state, assets = selectable.useWith(state, assets)
                            state.selectedItem = None
                        else:
                            state, assets = selectable.use(state, assets)
            # Check if selected a room selectable
            for selectable in state.currRoom.selectables:
                if selectable.get_rect().collidepoint(x,y) and not state.holdClicks:
                    if event.button == 3:
                        state, assets = selectable.examine(state, assets)
                    elif event.button == 1:
                        if state.selectedItem:
                            state, assets = selectable.useWith(state, assets)
                            state.selectedItem = None
                        else:
                            state, assets = selectable.use(state, assets)
            
            for exit in state.currRoom.exits:
                if exit.rect.collidepoint(x,y) and not state.holdClicks:
                    if event.button == 1:
                        state, assets = exit.enterRoom(state, assets)

    # Update hoverText to whatever the mouse is hovering over
    state = checkHoverText([assets.global_selectables, state.currRoom.selectables, state.currRoom.exits], state=state)

    # Draw all objects
    drawEverything(state=state, assets=assets)

    # Update all objects on screen
    pygame.display.flip()    
    # 60 FPS
    clock.tick(60)
