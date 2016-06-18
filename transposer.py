import numpy as np

notes = ["A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb","G", "G#/Ab"]
undesirableIndices = [1, 4, 6, 9, 11]
capoPlacement = 0
success = False

endInput = False
chordList = []
chordIndexList = np.array([])
updatedChordList = []
updatedChordIndexList = []

while(not endInput):
    newChord = input("Enter next chord or type ''end'' to finish: \n")
    if(newChord == 'end' or newChord == 'End'):
        endInput = True
    else:
        chordList.append(newChord)

for i in chordList:
    for index, j in enumerate(notes):
        if( (len(i) == 1 and i ==j) or (len(i) > 1 and i in j) ):
            chordIndexList = np.append(chordIndexList, index)

while( (not success) and capoPlacement < 11):
    capoPlacement += 1
    success = True
    updatedChordIndexList = (chordIndexList + (12 - capoPlacement))%12
    print(updatedChordIndexList)
    for j in updatedChordIndexList:
        for k in undesirableIndices:
            if(j==k):
                success = False
    if(success == True):
        break

if( not success ):
    print("No solution found")
else:
    for i in updatedChordIndexList:
        updatedChordList.append(notes[int(i)])
    print("Capo on " + str(capoPlacement))
    for i in range(0, len(updatedChordList)):
        print(updatedChordList[i] + "|" + chordList[i])
