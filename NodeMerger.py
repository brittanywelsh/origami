
# NodeMerger takes a node tree (i.e. a graph) and merges nodes according to certain rules.

# The input is a graph, specified in list syntax as follows:
#	Graph = [ ListOfPointers, ListOfLinks, ListOfContent ]
#		ListOfPointers = [0, 1, 2, ...]
#			(each 'pointer' is an integer that specifies a particular node.)
#		ListOfLinks = [ LinksOfNode0, LinksOfNode1, ... ]
#			(each 'LinksOfNodeX' element is a list of the form ["#a", "#b", ...] where '#C' is a string specified by the encoding/decording scheme described below)
#		ListOfContent = [ [ContentA, ContentB, ...], [ContentC, ContentD, ...] ]
#			(each 'ContentX' element is a list containing data of arbitrary type (for now))
#
# HOW IT WORKS: The graph is specified by three lists.
#	0. The 0th list is a list of pointers. Every pointer is an integer. Every pointer corresponds to a specific list index in the other two lists. The list is initially populated with the set [0, 1, 2, ..., n-1] for a graph with n nodes.
#	1. The 1st list is a list of links. Each link is a list of strings of the form '#X' where # is an integer numeral and X is a character that represents a particular relation/link type, as specified by the encoding scheme (described below).
#	2. The 2nd list is a list of content lists. Every node has a list representing the value/contents of that node.
#
#

""" FOR MERGING PUPOSES: 

Every graph has a LIST OF POINTERS and a LIST OF LINKS.
Each initial graph has a list of pointers which is exactly the set [0, 1, 2, 3, ..., n-1] (for a graph with n nodes)
Everytually, we want to shuffle around pointers so that we can quickly merge nodes together without having to change lists around too much...
Therefore, we have the following system:

	- Every (integer) POSITION in the LIST OF POINTERS uniquely references a unique node on the initial graph, which may have since been merged with another node.
	- Every (integer) VALUE in the LIST OF POINTERS references some node on the current graph, but it may be different from the POSITION of that element IFF that node has been subsumed by another node.

	- Every position on the LIST OF LINKS is the original position of the node on the initial graph, therefore uniquely specified. (However, this particular element may be referenced more than once by the LIST OF POINTERS.)
	- Every element on the LIST OF LINKS refers to a number, but it should always POINT TO THE *POSITION* on the LIST OF POINTERS.
			** This is so that there is only ever one "level of misdirection" in our merge scheme.
			** This also helps us so that we don't have to do too many list manipulations when we merge nodes.
                        !! Issue: we are already doing heaps list manipulation for other reasons- transative properties, symetric properties, removing duplicate, etc. Would it be easier to just mess with the lists?
                                                                
"""



"""
To-do later:
	- implement genetic algortihm capabilities
"""

import copy

BrittanyGraphForTesting = [
	[0,1,2,3,4,5],

	[
		[1], [0], [], [4,5], [3], [3]
	],

	[
		["a"],["b"],["c"],["d"],["e"],["f"]
	]
]


def AlastairMakeTestGraph():
        size=14
        LinkNums=12
        ListNodes=range(size)
        Links= [ [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        Content= [ ["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],["k"],["l"],["m"],["n"],["o"],["p"],["q"],["r"]]
        Content= Content[0:size]
        Links= Links[0:size]
        while LinkNums>0:
                LinkNums=LinkNums-1
                pair=  PickNodesToMerge(ListNodes)
                Links[pair[0]].append(pair[1])
                Links[pair[1]].append(pair[0])

        ReturnMe= [ListNodes,Links,Content]
        return ReturnMe



def SatisfactionConditionsAreNotMet( listOfExistingNodes ):
	if len(listOfExistingNodes) <= 7:
		return False
	else:
		return True

import random
def PickNodesToMerge( listOfNodesToPickFrom ):	
	shuffledList = list(listOfNodesToPickFrom)
	random.shuffle(shuffledList)
	listOfNodesToMerge = [shuffledList[0], shuffledList[1]]
	return listOfNodesToMerge

def GenerateTestGraph( inputGraph, nodesToMerge ):
	pointerA = nodesToMerge[0]
	pointerB = nodesToMerge[1]

                #NOTE (A2B) It appears that our copying was not deep enough. This lead to this method altering its input. Now using the much slower deep copy, but other suggestions welcome.
	newListOfPointers = copy.deepcopy(inputGraph[0])
	newListOfLinks = copy.deepcopy(inputGraph[1])
	newListOfContent = copy.deepcopy(inputGraph[2])
	# [A, B] -> [A, A]
	# We have nodesToMerge = [A,B]. This means we want to replace all instances of "B" with "A".

	# First, do a set merge from content of node ref'd by "B" onto node ref'd by node "A"
	for element in newListOfContent[pointerB]:
		newListOfContent[pointerA].append( element )
	# erase contents at newly="ghosted" node:
	newListOfContent[pointerB] = "BANANA"

	# Ditto, everything that nodeB once linked to s/b linked to by nodeA.
	for integer in newListOfLinks[pointerB]:
		newListOfLinks[pointerA].append( integer )
	# erase...
	newListOfLinks[pointerB] = "BANANA"

	# FINALLY, adjust the pointers: all instances of pointerB become pointerA.
	for index in range(len(newListOfPointers)):
		if newListOfPointers[index] == pointerB:
			newListOfPointers[index] = pointerA

	outputGraph = []
	outputGraph.append(newListOfPointers)
	outputGraph.append(newListOfLinks)
	outputGraph.append(newListOfContent)
	return outputGraph


def ConsolidateGraph(inputGraph):
        #This is a method which writes over link indices, AND removes duplicate links. May be basis for more advanced thing.
        #Give that this method is INTENDED to alter its input, no copying (deep or otherwise) is done.        
        for linksFrom in range(len(inputGraph[1])):
                if inputGraph[1][linksFrom] is not "BANANA":
                        for linkIndex in range(len(inputGraph[1][linksFrom])):
                                inputGraph[1][linksFrom][linkIndex] = inputGraph[0][inputGraph[1][linksFrom][linkIndex] ]
                        inputGraph[1][linksFrom]=[ii for n,ii in enumerate(inputGraph[1][linksFrom]) if ii not in inputGraph[1][linksFrom][:n]]                
        

        
def AbhorSelfLinksTest(inputGraph):
        print "Abhoring SelfLinks"
        for linksFrom in range(len(inputGraph[1])):
                if inputGraph[1][linksFrom] is not "BANANA":                
                        print "is "  ,linksFrom ," in " ,inputGraph[1][linksFrom],"?"
                        if linksFrom in inputGraph[1][linksFrom]:
                                print "YES! Thus self link, thus is bad."
                                return False
        return True

def VerifyTestGraphIsGood( inputGraph ):
	if AbhorSelfLinksTest(inputGraph):
		return True	
	return False

def NodeMerger( inputGraph ):

	latestGraph = list(inputGraph)
	listOfCurrentlyExistingNodes = list(inputGraph[0]) # List of integers which correspond to nodes which are not ghosts. they exist.

	print "\n\n\nTIME TO START THE LOOP!"
	while SatisfactionConditionsAreNotMet( listOfCurrentlyExistingNodes ):

		# Determine (randomly, or not) which nodes to merge:
		nodesToMerge = PickNodesToMerge( listOfCurrentlyExistingNodes )
		print "Merging ", nodesToMerge[1], " into ", nodesToMerge[0]


		print "Previously the list of pointers looked like..... ", latestGraph[0]
		# 'Test merge' the two nodes by generating a new graph with the two nodes being merged:
		testGraph = GenerateTestGraph( latestGraph, nodesToMerge )
		print "\nJust after testGraph the grpah is:\n", latestGraph
                ConsolidateGraph(testGraph)
                
		# Check that the proposed merge doesn't break the rules of the system:
		testGraphIsGood = VerifyTestGraphIsGood( testGraph )


		if testGraphIsGood:
                        print "Updating Graph"
			latestGraph = list(testGraph)
			listOfCurrentlyExistingNodes.remove( nodesToMerge[1] )
		print "Once the loop is complete, the listOfCurrentlyExistingNodes looks like: ", listOfCurrentlyExistingNodes

	print "\nTHE FINAL GRAPH IS:\n", latestGraph
	return latestGraph

InitialGraph= AlastairMakeTestGraph()
print "\nTHE INITIAL GRAPH IS:\n",InitialGraph
NodeMerger(InitialGraph)
