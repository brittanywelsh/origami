"""
-------
ORIGAMI
-------

This program generates a story/game walkthrough from a list of "snippets" (which are causal links between various types of inputs and outputs, such as characters, locations, and game-significant items).

A "SNIPPET" is a list of the form [Description, Inputs, Outputs, InputTypes, OutputTypes], where each of the constituent parts is a list of strings

1. NodeTreeConstructor
	Generates 
	a. Read inputs (snippets, input/output of snippets) from CSV file
	b. Generate tree of causally-linked events, from start to end of game
		- procedure loops until an acceptable tree is generated
2. 
"""



"""
0. What input does "World Builder" need?
1. Write merger

"""




"""
To-do list:
- write input parser
- input interpreter (determine the links between nodes)
	* nodes can have sub-types/super-types.
"""



""""""""""""""""""""""""""""""""""""""


"""
ListOfCharacterRoles = ["Healer", "Villain", "Foil", "Mentor", "Love Interest", "Shopkeeper"]
ListOfItems = ["Potion", "Amulet", "Sword", "Key", "Dragon Axe", "Staff of Anchoring"]
ListOfPlaces = ["Big Forest", "Sea", "Beach", "Town", "Mountain", "Evil Lair In the Dark Woods", "Haunted House"]
ListOfPlaceRoles = ["Start location", "End location", ]
# PlaceRoleInStory
# PlaceTerrainType
"""

"""
# Characters:
ListOfCharacterRelationships = ["Sibling of ", "Parents of", "Child Of"]
ListOfCharacterProfessions = ["Baker", "Smith", "Tax collector", "Dragon slayer", "Child"]
ListOfCharacterPersonalities = ["Wise", "Bubbly", "Serious", "Stern", "Giving", "Greedy", "Suspicious", "Paranoid", "Trouble-maker", "Worried", "Carefree"]

def CreateFamilyTree():
	NumberOfCharacters = 10
	NumberOfCharacterFragments = 20
"""

# PlayerTimeline
# What do players do?
#	- go to (place)
#	- get (item)  from (place)
#	- get (item) from (person)
#	- give (item) to (person)
#	- talk to  (person) about (event)
#	- overcome (obstacle) using (item)
#	- overcome (obstacle) using (knowledge)
#	- get (knowledge) from (place) about (event)
#	- get (knowledge) from (person)

# Knowledge maps for what the player knows?

# Example, simplified game.
# - GOAL: Escape the dungeon
# - NTK: LOCATION of EXIT
# - NTK: GOAL
# - NTK: GOAL consist of LOCATION (EXIT) + ITEM (KEY) - how to complete the GOAL


# Example of You Have to Burn the Rope:
# - 


"""
Approaches for Player Knowledge.....
Basic: X is required for Y
- contruct a line of requisite arrows that lead the player through the game (knowledge-wise)
- ... but separate from the actual player timeline.
-- 

"""

"""
Timeline:

Top level:
- Kill (monster)
	- ... with (weapon)
		-> get (weapon) from (place)/(person)/(purchase)
	- ... with (magic)
		-> get ()
	- ... with (skill)
	- ... with (help from living entity)
- Get to (place)
- Obtain (item)


(DOING THING) with (OBJECT USED TO DO THING)
- kill with weapon/skill/whatever
"""


