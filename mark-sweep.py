#Homework 3
#CPSC3400
#Jules Hunter
#Mark-Sweep garbage collection simulation

import sys
import string

def processFile(filename):
    marked = [] #marked nodes
    unknown = [] #nodes that require more processing

    #Process the file 
    letters = string.ascii_lowercase+"_"
    numBlocks = 0
    firstLine = True
    for line in open(filename, 'r'):
        line = line.rstrip()

        #first line
        if firstLine == True:
            numBlocks = int(line)
            firstLine = False
            continue

        #process each subsequent line
        components = line.split(',')
        pntr = components[0]
        pointed = int(components[1])

        #if it is a named pointer
        if pntr[0] in letters:
            marked.append(pntr)
            marked.append(pointed)
        #if it is a heap block that has already been marked
        elif int(pntr) in marked:
            if pointed not in marked:
                marked.append(pointed)
        
        #we can't process it yet (may be marked, but the connection hasn't been processed yet)
        else:
            unknown.append((int(pntr), pointed))

    #Finish the mark-sweep
    #If the unmarked list has been updated, check again
    update = True
    while update:
        update = False
        #for all unmarked nodes, double check if they are pointed to
        for item in unknown: 
            if item[0] in marked:
                marked.append(item[1])
                unknown.remove(item)
                update = True

            
        
    #remove named pointers from marked list
    for thing in marked:
        if type(thing) == type("hello"):
            marked.remove(thing)


    marked.sort()

    #create the list of nodes to be swept
    sweep = []
    for i in range(0, numBlocks):
        if i not in marked:
            sweep.append(i)


    return (marked, sweep)


#driver
            
#1. input file
filename = sys.argv[1]

#2,3. process the file and perform the mark-sweep algorithm
myHeap = processFile(filename)

#4. Output which heap blocks are marked and which are swept
print("Marked nodes:",end=" ")
for block in myHeap[0]:
    print(block,end=" ")

print("\nSwept nodes:", end=" ")
for block in myHeap[1]:
    print(block,end=" ")


