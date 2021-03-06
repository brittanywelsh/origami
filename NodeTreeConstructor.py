"""
Node approach:
- have a bag of nodes which have inputs, outputs (some have no input -- start nodes)
- inputs/outputs are some sort of "significant object" or thing or whatever
- have a function which grabs nodes, then goes backward to grab corresponding inputs
"""

"""
Data Input Structure
====================
Col 1		Col 2					Col 3				Col 4				Col 5
[Snippet]	Input Node(s)			Output node(s)		Input Node Types	Output Node Types
			(comma separated)		(comma separated)	(comma separated)	(comma separated)

- (for now, every node has a type)
- (when dealing with a generic node, the name of the node is the same as the node type)


"""

import random

"""
# SnippetList is a list of 3-tuples. Each 3-tuple is a "snippet" and has input list, output string, & desc. string.
SnippetList = [
[ ["JarOfAir","Island"], "Shell", "Swim to the bottom of the bay and find a shell"],
[ ["HighPlace"], "Translation", "Take a photo of the ruins at the top of the mountain. Take it to the Archeologist to decipher"],
[ ["AnchorStaff"], "HighPlace", "Use the AnchorStaff to change to timing on the moving platforms on the <TallPlace>. Climb to the top."],
[ [], "Flower", "Find a flower"],
[ [], "Shell", "Find a shell"],
[ ["Map"], "DeepPlace", "Use the map to navigate the labrinth to the bottom of the deep place"],
[ ["FireSpell"], "HighPlace", "Use the FireSpell to keep yourself warm as you climb the frozen mountainside."],
[ ["DeepPlace","FireSpell"], "Diamond", "Battle the Frost Dragon in the <Deep Place>- retrieve the Diamond"],
[ ["GreaseSpray"], "Sword", "Find a sword stuck in a rusty gear mechancism- use the GreaseSpray to free the mechanism and withdraw it."],
[ ["Translation","Book"], "Map", "Use your translation on a book to retrieve instructions about where stuff is."],
[ [], "Book", "Find a book at the local library"],
[ ["Diamond"], "AnchorStaff", "A local wizard needs a diamond to complete her experiment. Give her the diamond to complete it, and she'll let you test it out."],
[ [], "Candle", "Buy a candle from the local store."],
[ [], "Sword", "Buy a sword from the local store"],
[ ["Sword"], "Flower", "Use your sword to hack flowers of a rugged tree"],
[ ["Shield"], "HighPlace", "Use your shield to withstand incoming boulders as you climb the mountain"],
[ ["Map"], "FarPlace", "Use the map to navigate the forest to the other side"],
[ ["DeepPlace"], "Island", "Follow the tunnel to the Island."],
[ ["Candle"], "DeepPlace", "Use your candle to navigate the darkness"],
[ ["Island"], "Shell", "Pick a shell up from the beach"],
[ [], "Island", "Take a ferry across to an island."],
[ ["Sword"], "Diamond", "Fight goblins, find diamond"],
[ ["DeepPlace"], "Book", "Find an ancient tome in the deep place"],
[ ["GreaseSpray"], "Shield", "Use the grease spray to repair the blacksmiths mechanism."],
[ ["DoubleJump"], "HighPlace", "Double jump your way to <TallPlace>"],
[ ["DoubleJump"], "Island", "Double jump your way across the rocks to the island."],
[ ["DoubleJump"], "FarPlace", "Double jump your way across a chasm to farplace"],
[ [], "DoubleJump", "Learn doublejump at the end of the tutorial"],
[ ["Sword","Shield","AnchorStaff"], "Win", "Fight the Jabberwock- save the kingdom"],
[ ["JarOfAir","Candle"], "DeepPlace", "Protect your candle in the jar, explore the wet cave."],
[ ["Candle","Flower","Shell"], "Win", "Ward off evil spirits using the flower, candle and shell. Save the kingdom."],
[ ["DeepPlace","HighPlace","FarPlace","Island"], "Win", "Take photos of everywhere in the land, and become a ledgendary nature photographer."],
[ ["Axe"], "FarPlace", "Cut down a tree with the axe to form a bridge across the chasm"],
[ ["GreaseSpray"], "Axe", "Use the Grease to unrust the Tin man- he gives you his axe in return."],
[ ["FireSpell"], "Sword", "Use your fire to heat the blacksmiths forge- in return he will smelt you a fine sword."],
[ ["LightningSpell","FeatherFall","AnchorStaff"], "Win", "Battle the Iron Sorcerer and Save the kingdom"],
[ ["FeatherFall"], "DeepPlace", "Jump down into the gaping pit. Use your ring of featherfall to survive."],
[ [], "Win", "What an amazing day today is! Congradulations on getting out of bed today."],
[ ["GhostSpeak"], "FireSpell", "Go to the graveyard and talk to a ghostly wizard. S/he teaches  you the fireball spell."],
[ ["GhostSpeak"], "Map", "Talk to the ghost of an explorer and learn way through <SOMEWHERE>"],
[ ["GhostSpeak","Flower"], "DeepPlace", "Talk to the ghosts at the entrance to <DeepPlace>- they will let you pass if lay flowers around their tombs."],
[ ["Shell","GhostSpeak"], "Island", "Listen to the voices of Lost sailors in the Shell. Learn the location of a distant Island."],
[ ["FeatherFall","Axe"], "AnchorStaff", "Battle the gorgon!- use the feathfall spell to prevent yourself being knocked into the pit of lava."],
[ [], "Hammer", "Steal a hammer from the blacksmith"],
[ ["Flower","Shell"], "GhostSpeak", "Bring the witchdoctor ingrediants and they will teach you to speak with ghosts."],
[ ["Book"], "GhostSpeak", "Retrieve the priests holy book, and he will teach you how to speak with ghosts."],
[ [], "Shield", "Buy a shield"],
[ [], "GreaseSpray", "Find a can of GreaseSpray in a tool shed."],
[ ["Flower"], "GreaseSpray", "Help an Alchemist make their brew. Recieve a random concoction in return."],
[ [], "HighPlace", "Climb!"],
[ [], "Map", "Find a map in the local bookstore"],
[ [], "Candy", "Go buy some candy"],
[ ["Candy"], "GreaseSpray", "A child in town will trade pranking supplies for some candy."],
[ ["GiantStrength"], "DeepPlace", "Push a huge boulder our of your way in order to explore the tomb."],
[ ["Hammer","FireSpell"], "GiantStrength", "Pass a test of the Forge God to earn giantStrength"],
[ ["GiantStrength"], "HighPlace", "Roll boulders into position so that you can climb the mountain."],
[ ["HighPlace"], "GhostSpeak", "Talk to the Oracle and learn to speak with Ghosts."],
[ ["Feather","Book"], "FeatherFall", "Read a Spellbook, and teach yourself FeatherFall"],
[ [], "Feather", "Capture a chicken"],
[ ["AnimalSpeak"], "Feather", "Convince a great Eagle to give you one of its feathers."],
[ ["Flower"], "Candy", "Bring ingrediants for making Candy."],
[ ["Candy"], "AnimalSpeak", "A sweet toothed forest spirit will teach you to speak with animals."],
[ ["Rope"], "HighPlace", "Use Rope to climb the mountain"],
[ ["FireSpell"], "Axe", "Defeat the living bramble and reclaim the huntsmans axe."],
[ ["DeepPlace"], "GhostSpeak", "The ancient spirits in the ghost place will teach you how to talk to others."],
[ ["Hammer"], "Shield", "Give the Blacksmith a new hammer, get a shield"],
[ ["Diamond","LightningSpell","GhostSpeak"], "Win", "Help Doctor Frankenstien finish his diabolic experiment!"],
[ ["HighPlace","AnimalSpeak"], "LightningSpell", "Talk to the thunderbird at the top of the mountain. It will teach you how to create lightning."],
[ ["PotionOfHealing"], "AnchorStaff", "A priest will give her/her staff to whoever can cure their spouses illness"],
[ ["RareHerb","Feather","Shell"], "PotionOfHealing", "Witchdoctor can brew up a healing potion... with enough ingredients."],
[ ["Book","RareHerb","Flower"], "PotionOfHealing", "You can cook up a potion of healing with sufficient research and preparation"],
[ [], "RareHerb", "So the herb isn't all that Rare- you find one walking around."],
[ ["DoubleJump"], "RareHerb", "Retrieve some of the RareHerb from a treetop, just out of reach of passers by."],
[ ["Axe"], "RareHerb", "Cut through a thicket of brambles to find the RareHerb."],
[ ["HighPlace"], "RareHerb", "Find a strange plant at the top of a mountain."],
[ ["Book"], "RareHerb", "Using your knowledge and reading of herbology, you now have the knowledge to identify this rare and precious plant."],
[ ["RareHerb"], "GiantStrength", "Eat the herb, become strong like a giant!"],
[ ["GiantStrength"], "Diamond", "Bash open a boulder, retrieve the Diamond inside"],
[ ["Hammer"], "Diamond", "Bash open a boulder, retrieve the Diamond inside"],
[ [], "GhostSpeak", "The first time the player dies, a nearby ghost shows up and brings you back, chatting to you in the process. You are informed that although you are now dead, your quest is not yet over."],
[ ["GreaseSpray","LightningSpell"], "FarPlace", "Repair the SteelChariot, and power it using lightning- it will take you far away."],
[ ["Diamond","Hammer"], "LightningSpell", "Shatter the Diamond, and gain the power of lightning"],
[ ["Feather","Shell","RareHerb"], "AnimalSpeak", "Complete the ritual in the forest- talk to the spirit wolf."],
[ [], "JarOfAir", "get a jar of air. wheeeee"],
[ [], "Rope", "Buy a rope."]
           ]
"""

inputFileName = "QuestSnippets.csv"
#inputFileName = "input.csv"
columnDelimiter = "#"  # separates columns

SnippetList = []

inputFile = open(inputFileName, "r")
for line in inputFile:
	InputsList = []
	OutputsList = []
	InputTypesList = []
	OutputTypesList = []
	line.replace("\n","") # remove newline symbols
	ListOfItems = line.split("#")
	Description = ListOfItems[0]
	InputItems = ListOfItems[1]
	OutputItems = ListOfItems[2]
	InputTypes = ListOfItems[3]
	OutputTypes = ListOfItems[4]
	for item in InputItems.split(","):
		if item != '0':
			InputsList.append(item)
	for item in OutputItems.split(","):
		OutputsList.append(item)
	for item in InputTypes.split(","):
		if item != '0':
			InputTypesList.append(item)
	for item in OutputTypes.split(","):
		OutputTypesList.append(item)
	NewSnippet = []
	NewSnippet.append(Description)
	NewSnippet.append(InputsList)
	NewSnippet.append(OutputsList)
	NewSnippet.append(InputTypesList)
	NewSnippet.append(OutputTypesList)
	SnippetList.append(NewSnippet)
#for thing in SnippetList:
#	print thing, "\n"


#for i in range(0,10):
#	print random.randint(0,10)



def NumberOfInputs( inputSnippet ):
	inputList = inputSnippet[1]
	NumberOfInputs = len(inputList)
	return NumberOfInputs

def GetSnippetWithNonemptyInput( listOfSnippets ):
	TestSnippetHasEmptyInput = True
#	OverflowCounter = 0

	while TestSnippetHasEmptyInput:
		RandomNumber = random.randint(0, len(listOfSnippets)-1)
		TestSnippet = listOfSnippets[ RandomNumber ]
		if NumberOfInputs( TestSnippet ) != 0:
			TestSnippetHasEmptyInput = False
			return TestSnippet
#		OverflowCounter += 1
#		if OverflowCounter > 10:
#			return


def GetAppropriateSnippet( outputNeeded, listOfSnippets, inputsForbidden ):
	TestSnippetIsNoGood = True
	OverflowCounter = 0
        IndexDeck= range(0, len(listOfSnippets))
        random.shuffle(IndexDeck)

	while TestSnippetIsNoGood and OverflowCounter<len(IndexDeck):		
		TestSnippet = listOfSnippets[IndexDeck[OverflowCounter] ]
		if TestSnippet[2][0] == outputNeeded:
                        #print "Found method to get",outputNeeded
                        if len([val for val in TestSnippet[1] if val in inputsForbidden])==0:
                                TestSnippetIsNoGood = False
                                return TestSnippet
                        #else:
                         #       print "Can't use method because of forbidden node",[val for val in TestSnippet[1] if val in inputsForbidden]
		OverflowCounter += 1	
	return



def GetSnippetWithOutput( node, listOfSnippets ):
	TestSnippetIsNoGood = True
#	OverflowCounter = 0

	while TestSnippetIsNoGood:
		RandomNumber = random.randint(0, len(listOfSnippets)-1)
		TestSnippet = listOfSnippets[ RandomNumber ]
		if TestSnippet[2][0] == node:
			TestSnippetIsNoGood = False
			return TestSnippet
#		OverflowCounter += 1
#		if OverflowCounter > 10:
#			return

def GetWinningSnippet( listOfSnippets ):
	TestSnippetDoesNotWin = True
#	OverflowCounter = 0

	while TestSnippetDoesNotWin:
		RandomNumber = random.randint(0, len(listOfSnippets)-1)
		TestSnippet = listOfSnippets[ RandomNumber ]
		if TestSnippet[2][0]=="Win":
			TestSnippetDoesNotWin = False
			return TestSnippet
#		OverflowCounter += 1
#		if OverflowCounter > 10:
#			return

def NodeNotOnList( node, listOfNodes ):  # string, list
	for element in listOfNodes:
		if node == element:
			return False
	return True


def BuildNodeTree():
#	NumberOfNodes = len(SnippetList)

	# Start with empty "Walkthrough" list, which will be populated.
	Walkthrough = []

	# This "UnresolvedNodes" list will be used for tracking what still needs to be done.
	UnresolvedNodes = []
	ResolvedNodes = []

#### choose random vs. choose a Snippet with a win condition
#	InitialSnippet = GetSnippetWithNonemptyInput(SnippetList)
	InitialSnippet = GetWinningSnippet(SnippetList)
####

	### GET INITIAL Snippet (with win condition) ###
	Walkthrough.append(InitialSnippet)
	InitialInputList = InitialSnippet[1]
	#print "InitialInputList = ", InitialInputList
	for i in range(len(InitialInputList)):
		UnresolvedNodes.append( InitialInputList[i] )

	### POPULTE THE TREE ###
	iterationNumber = 0
	while len(UnresolvedNodes) > 0:

		iterationNumber += 1
		#print "ITERATION ", iterationNumber, "\tunresolved nodes = ", UnresolvedNodes

		# resolve the FIRST unresolved node
		ThisUnresolvedNode = UnresolvedNodes[0]
		#print "THIS UNRESOLVED NODE = ", ThisUnresolvedNode
		NewSnippet = GetAppropriateSnippet( ThisUnresolvedNode, SnippetList, ResolvedNodes)
		
		if NewSnippet:
			Walkthrough.append(NewSnippet)

			# add any further dependences to the END of the list. If already present, move them to the end, so that they less likely to be resolved, can be reused.
			NewNodeList = NewSnippet[1]
			UnresolvedNodes= [item for item in UnresolvedNodes if item not in NewNodeList]+NewNodeList                        

			# add resolved node to the Resolved list (to avoid circular dependancies.)
			ResolvedNodes.append(UnresolvedNodes[0])

			# remove the FIRST unresolved node from the list
			UnresolvedNodes.pop(0)
		else:
			UnresolvedNodes = []
			#print "FAILURE! ALL IS LOST!"
			return False
                
		if iterationNumber > 100:
			UnresolvedNodes = []

	print "WALKTHROUGH TIME. HERE WE GO."

	Walkthrough.reverse()

	for link in Walkthrough:
		print link[0], "\t\tIn: ", link[1], "  Out:", link[2]
	return True


while not BuildNodeTree():
        print "Try again"



"""
def InputNodeIsEmpty( inputLink ):
	print inputLink
	if len( inputLink[0] ) == 0:
		print "true"
		return True
	else:
		print "false"
		return False """
"""
for i in range (0,len(SnippetList)-1):
	GetNumberOfInputs(SnippetList[i])

InputNodeIsEmpty( SnippetList[3] )
InputNodeIsEmpty( SnippetList[0] )
"""




