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
pygame.font.init()
font = pygame.font.SysFont(None, 32)
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
    renderDialog = render(state.dialog, font)
    renderHover = render(state.hoverText, font)
    screen.blit(renderDialog, renderDialog.get_rect(center = (640, 600)))
    screen.blit(renderHover, renderHover.get_rect(center = (640, 100)))

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
    
    # state.hoverText = f"{pygame.mouse.get_pos()}"
    return state


# Function to run the given dialog tree
def startDialog(state, assets, x=640, y=550, fontSize=32):
    # Always assume dialog starts at start in the dict
    currNode = "start"
    state.dialog = ""
    while True:
        # Need to draw everything here so that the dialog doesnt constantly stack up.
        drawEverything(state=state, assets=assets)

        # Display Response
        currText = state.currDialogTree[currNode]["text"]

        # currTextSplit = currText.split('\n')
        currTextSplit = splitString(currText)
        for i, line in enumerate(currTextSplit):
            renderDialog = render(line, font)
            yOff = y - ((len(currTextSplit)-1-i)*fontSize)
            screen.blit(renderDialog, renderDialog.get_rect(center = (x, yOff)))           

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
            screen.blit(assets.imageLookup[state.currDialogTree[currNode]["image"]], (150,150))
            pygame.display.update()

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
            currNode = state.currDialogTree[currNode]["next"][selectedOption]
            if "events" in state.currDialogTree[currNode]:
                for event in state.currDialogTree[currNode]["events"]:
                    state, assets = eventLookup[event](state, assets)

        clock.tick(60)


### Base Item Classes
# Base Room class with it's background, selectable objects, and exits
class Room(object):
    def __init__(self, name, bg=None, selectables=[], exits=[]):
        self.bg = bg
        self.selectables = selectables
        self.name = name
        self.exits = exits

# Base selectable class. Anything that can be iteracted with should be this class.
class Selectable(object):
    def __init__(self, pos, name="", image=None, examine="", useTxt="I can't use that"):
        self.pos = pos
        self.image = image
        self._name = name
        self.examineTxt = examine
        self.useTxt = useTxt

    @property
    def name(self):
        return self._name

    # Just to simplfy this call
    def get_rect(self):
        return self.image.get_rect(topleft=self.pos)
    
    # Selectables that don't just say it's useTxt should override this method
    def use(self, state, assets):
        state.dialog = self.useTxt
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

# Base class for exits
# TODO I could probably make this a selectable idk
class Exit(object):
    def __init__(self, rect, name="", newLoc=""):
        self.rect = rect
        self.newLoc = newLoc
        self.name = name

    def get_rect(self):
        return self.rect

# Item class specifically for being put into your inventory. Probably doesn't need its own class.
class Item(Selectable):
    def useWith(self, state, assets):
        state.dialog = "Those don't do anything together."
        return (state, assets)

class Pickupable(Selectable):
    def __init__(self, pos, invItem, name="", image=None, examine="", useTxt="I can't use that"):
        super().__init__(pos, name, image, examine, useTxt)
        self.invItem = invItem

    def use(self, state, assets):
        state.dialog = f"You took the {self.name}"
        state.currInventory.append(self.invItem)
        state.currRoom.selectables.remove(self)
        return (state, assets)

class Microwave(Pickupable):
    def use(self, state, assets):
        state, assets = super().use(state, assets)
        state.currRoom.selectables.append(assets.socket)
        return (state, assets)

class Socket(Selectable):
    def useWith(self, state, assets):
        # TODO change this to time machine later
        if state.selectedItem.name == "Microwave":
            state.dialog = f"You plugged in the {state.selectedItem.name}"
            state.currRoom.selectables.remove(self)
            state.currInventory.remove(state.selectedItem)
            state.currRoom.selectables.append(assets.microwave)
            state.selectedItem = None
            return (state, assets)
        else:
            return super().useWith(state, assets)

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
            state.currInventory.remove(state.selectedItem)
            state.dialog = f"You ate the {state.selectedItem.name}"
            return (state, assets)


# The current state of the game. All the flags and stuff is stored here.
class State(object):
    def __init__(self, assets):
        self.dialog = ""
        self.hoverText = ""
        self.currDialogTree = assets.dialogTrees["mainMenu"]
        self.currNode = "start"
        # TODO change to main menu room
        self.currRoom = assets.bedroom
        self.currInventory = []
        self.selectedItem = None
        self.wrenchTaken = False
        self.examScore = 0


# Container for all the instances of things the game uses. Inefficient but fuck it.
class Assets(object):
    def __init__(self):
        # Dialog trees
        self.dialogTrees = {
            "mainMenu": mainMenu,
            "settingsMenu": settingsMenu,
            # "testManDialog": testManDialog,
            "testManDialog": quizDialog,
            "quizDialog": quizDialog,
        }

        # Inventory Items
        wrenchImage = pygame.transform.scale(pygame.image.load("graphics/wrench.jpg"), (50,50))
        self.wrench = Item(pos=(0,0), name="Wrench", image=wrenchImage, examine="It's a wrench.")

        brickExamine = "A kitchen brick. A useful cooking tool and nutritious too."
        brickImage = pygame.transform.scale(pygame.image.load("graphics/brick.png"), (50,25))
        self.brickItem = Item(pos=(0,0), name="Brick", image=brickImage, examine=brickExamine)

        mwExamine = "I use this to heat up my Hot Pockets."
        microwaveImage = pygame.transform.scale(pygame.image.load("graphics/microwave.png"), (50,25))
        self.microwaveItem = Item(pos=(0,0), name="Microwave", image=microwaveImage, examine=mwExamine)

        # Selectables
        self.portrait = Joms(pos=(1180,0), name="Joms", image=pygame.image.load("graphics/Joms.jpg"), examine="It's me, Joms!", useTxt="Moms told me I shouldn't touch myself.")
        self.bag = Bag(pos=(1080,0), name="Open Inventory", image=pygame.image.load("graphics/bag.png"), examine="It's my bag.")
        self.settings = NPC(pos=(0,0), name="Settings", image=pygame.image.load("graphics/settings.png"), examine="A hastily drawn cogwheel", dialogTree=self.dialogTrees["settingsMenu"])
        self.computer = Selectable(pos=(550,350), name="Use Computer", image=pygame.image.load("graphics/Computer.png"), examine="My old computer I use to browse dank memes.")
        self.bed = Selectable(pos=(0,330), name="Bed", image=pygame.image.load("graphics/bed.png"), examine="Even though it's a waste of time, I like to make my bed every morning.")
        self.weedPlot = Selectable(pos=(80,435), name="Weed-Filled Garden", image=pygame.image.load("graphics/plotWeeds.png"), examine="No one has weeded this garden in years.")
        self.vegetablesPlot = Selectable(pos=(80,435), name="Garden", image=pygame.image.load("graphics/plotVegetables.png"), examine="GREAT VEGETABLES!")
        self.brick = Pickupable(pos=(490,318), invItem=self.brickItem, name="Kitchen Brick", image=pygame.image.load("graphics/brick.png"), examine=brickExamine)
        self.oven = Selectable(pos=(173,312), name="Oven", image=pygame.image.load("graphics/oven.png"), examine="Our oven. Looks like Moms is cooking dinner.")
        self.fridge = Selectable(pos=(891,110), name="Fridge", image=pygame.image.load("graphics/fridge.png"), examine="There's nothing in it except some expired fruit.")
        self.pot = Selectable(pos=(190,260), name="Pot", image=pygame.image.load("graphics/pot.png"), examine="A pot of Moms' famous unsalted minced meat.")
        self.microwave = Microwave(pos=(170,129), invItem=self.microwaveItem, name="Microwave", image=pygame.image.load("graphics/microwave.png"), examine=mwExamine)
        self.socket = Socket(pos=(250,145), name="Electrical Outlet", image=pygame.image.load("graphics/socket.png"), examine="An electrical outlet.")

        # Global selectables container
        self.global_selectables = [self.bag, self.settings, self.portrait]


        # NPCs
        self.testMan = NPC(pos=(400,300), name="Test Man", image=pygame.image.load("graphics/testman.png"), examine="Who the fuck is this?", dialogTree=self.dialogTrees["testManDialog"])

        # Rooms
        self.bedroom = Room(name="bedroom", bg=pygame.image.load("graphics/Bedroom.png"), selectables=[self.computer, self.bed, self.testMan], exits=[Exit(rect=pygame.Rect(1000, 130, 200, 420), newLoc="livingRoom", name="Go to Living Room")])
        self.livingRoom = Room(
            name="livingRoom",
            bg=pygame.image.load("graphics/livingroom.png"),
            selectables=[],
            exits=[
                Exit(rect=pygame.Rect(155, 160, 150, 300), newLoc="bedroom", name="Go to Bedroom"),
                Exit(rect=pygame.Rect(1180, 170, 100, 400), newLoc="garden", name="Go Outside"),
                Exit(rect=pygame.Rect(0, 150, 60, 400), newLoc="kitchen", name="Go to Kitchen"),
            ]
        )
        self.garden = Room(name="garden", bg=pygame.image.load("graphics/jomsHousebg.png"), selectables=[self.weedPlot], exits=[Exit(rect=pygame.Rect(400, 350, 40, 110), newLoc="livingRoom", name="Go Inside"), Exit(rect=pygame.Rect(1180, 200, 100, 520), newLoc="bedroom", name="Go to Town")])
        self.kitchen = Room(name="kitchen", bg=pygame.image.load("graphics/kitchen.png"), selectables=[self.brick, self.microwave, self.oven, self.pot, self.fridge], exits=[ Exit(rect=pygame.Rect(1180, 170, 100, 400), newLoc="livingRoom", name="Go to Living Room")])
        # self.kitchen = Room(name="kitchen", bg=pygame.image.load("graphics/kitchen.png"), selectables=[], exits=[ Exit(rect=pygame.Rect(1180, 170, 100, 400), newLoc="livingRoom", name="Go to Living Room")])

        # Room Lookups
        self.roomLookup = {
            "" : self.bedroom,
            "bedroom" : self.bedroom,
            "livingRoom" : self.livingRoom,
            "garden" : self.garden,
            "kitchen" : self.kitchen
        }

        # Other stuff
        # TODO make this a real image
        self.inv = pygame.image.load("graphics/openInv.png")
        self.codeGeassShirley = pygame.transform.scale(pygame.image.load("graphics/shirley.webp"), (300,200))

        self.imageLookup = {
            "codeGeassShirley" : self.codeGeassShirley,
        }

# Instance a State and Assets object
assets = Assets()
state = State(assets)

def newGame(state, assets):
    assets=None
    state=None
    assets = Assets()
    state = State(assets)
    return (state, assets)


# Dialog callable functions
def exitGame(state, assets):
    pygame.quit()
    sys.exit()

def giveWrench(state, assets):
    state.currInventory.append(assets.wrench)
    return (state, assets)

def wrenchTaken(state, assets):
    if "1" in assets.dialogTrees["testManDialog"]["start"]["options"]:
        assets.dialogTrees["testManDialog"]["start"]["options"].pop("1")
    state.wrenchTake = True
    return (state, assets)

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
        state.currInventory.append(assets.wrench)
        assets.dialogTrees["quizDialog"]["results"]["text"] = "Congratulations, you passed the exam. Now get out of here."
        assets.dialogTrees["quizDialog"]["start"]["text"] = "Go on, enjoy the school trip."
        assets.dialogTrees["quizDialog"]["start"]["options"] = {"1": "Leave"}
        assets.dialogTrees["quizDialog"]["start"]["next"] = {"1": "leave"}
    state.currDialogTree = assets.dialogTrees["quizDialog"]
    return (state, assets)

def essayQuestion(state, assets):
    essayPrompt(state, assets)
    return (state, assets)

# Dictionary to map dialog options to functions
eventLookup = {
    "giveWrench" : giveWrench,
    "wrenchTaken" : wrenchTaken,
    "exitGame" : exitGame,
    "newGame" : newGame,

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
                    if selectable.get_rect().collidepoint(x,y):
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
        x = 250
        y = 200
        for item in state.currInventory:
            screen.blit(item.image, (x, y))
            item.pos = (x, y)
            x += 75
            if x >= 500:
                x = 250
                y += 75

        # Update hoverText to whatever the mouse is hovering over
        state = checkHoverText([assets.global_selectables, state.currInventory], state=state)

        # Print out the current texts.
        renderDialog = render(state.dialog, font)
        renderHover = render(state.hoverText, font)
        screen.blit(renderDialog, renderDialog.get_rect(center = (640, 600)))
        screen.blit(renderHover, renderHover.get_rect(center = (640, 100)))

        pygame.display.flip()
        # 60 FPS
        clock.tick(60)



################
def essayPrompt(state, assets):
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
                    # Process the entered text (e.g., send in a chat)
                    # print("Entered:", input_text)
                    input_text = ""
                    return
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

        renderDialog = render("Final question: Define a slur.", font)
        screen.blit(renderDialog, renderDialog.get_rect(center = (640, 550)))

        pygame.display.flip()
        clock.tick(60)



#############
# Actual Game Starts Here
#############
# Main Menu
state.currDialogTree = assets.dialogTrees["mainMenu"]
state, assets = startDialog(state=state, assets=assets)

# Main Gameplay Loop
while True:
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
                if selectable.get_rect().collidepoint(x,y):
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
                if selectable.get_rect().collidepoint(x,y):
                    if event.button == 3:
                        state, assets = selectable.examine(state, assets)
                    elif event.button == 1:
                        if state.selectedItem:
                            state, assets = selectable.useWith(state, assets)
                            state.selectedItem = None
                        else:
                            state, assets = selectable.use(state, assets)
            
            for exit in state.currRoom.exits:
                if exit.rect.collidepoint(x,y):
                    if event.button == 1:
                        state.currRoom = assets.roomLookup[exit.newLoc]
                        state.dialog=""

    # Update hoverText to whatever the mouse is hovering over
    state = checkHoverText([assets.global_selectables, state.currRoom.selectables, state.currRoom.exits], state=state)

    # Draw all objects
    drawEverything(state=state, assets=assets)

    # Update all objects on screen
    pygame.display.flip()    
    # 60 FPS
    clock.tick(60)