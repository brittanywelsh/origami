# Input is a CSV where each line is of the form:
# "Snippet", "InNode1,InNode2", "OutNode1,OutNode2", "InNode1Type,InNode2Type", "OutNode1Type,OutNode2Type"


"JarOfAir,Island"	"Shell"	"Swim to the bottom of the bay and find a shell"
"HighPlace"	"Translation"	"Take a photo of the ruins at the top of the mountain. Take it to the Archeologist to decipher"
"AnchorStaff"	"HighPlace"	"Use the AnchorStaff to change to timing on the moving platforms on the <TallPlace>. Climb to the top."

# Discard 1st line (column titles)
# For each line in input file: read line; put line in RowList
# For each row:
#	"S", "a,b,c", "d,e,f", "x,y,z", "u,v,w"
#	-->
#	[ "S", ["a", "b", "c"], ["d", "e", "f"], ["x", "y", "z"], ["u", "v", "w"] ]

inputFileName = "QuestSnippets.csv"
#inputFileName = "input.csv"
columnDelimiter = "#"  # separates columns




MasterSnippetsList = []

inputFile = open(inputFileName, "r")
for line in inputFile:
	InputsList = []
	OutputsList = []
	InputTypesList = []
	OutputTypesList = []
	line.replace("\n","") # remove newline symbols
	ListOfItems = line.split("#")
	Snippet = ListOfItems[0]
	InputItems = ListOfItems[1]
	OutputItems = ListOfItems[2]
	InputTypes = ListOfItems[3]
	OutputTypes = ListOfItems[4]
	for item in InputItems.split(","):
		InputsList.append(item)
	for item in OutputItems.split(","):
		OutputsList.append(item)
	for item in InputTypes.split(","):
		InputTypesList.append(item)
	for item in OutputTypes.split(","):
		OutputTypesList.append(item)
	RowList = []
	RowList.append(Snippet)
	RowList.append(InputsList)
	RowList.append(OutputsList)
	RowList.append(InputTypesList)
	RowList.append(OutputTypesList)
	MasterSnippetsList.append(RowList)



#for thing in MasterSnippetsList:
#	print thing, "\n"

"""
from sys import stdout

userinput = raw_input()
itemlist = userinput.split(',') # input split
arr = []
for item in itemlist:
	# Do something for each input
	arr.append( ) # intended output

stdout.write(arr[0])
for i in range(len(arr)):
	if i != 0:
		stdout.write(",")
		stdout.write(arr[i])
"""