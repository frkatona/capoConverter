## define valid chords for all capo positions and a keyList for reference
capoPositions = {
    '0': ['A', 'Am', 'C', 'D', 'Dm', 'E', 'Em', 'F', 'Fm', 'G'],
    '1': ['A#', 'A#m', 'C#', 'D#', 'D#m', 'F', 'Fm', 'F#', 'F#m', 'G#'],
    '2': ['B', 'Bm', 'D', 'E', 'Em', 'F#', 'F#m', 'G', 'Gm', 'A'],
    '3': ['C', 'Cm', 'D#', 'F', 'Fm', 'G', 'Gm', 'G#', 'G#m', 'A#'],
    '4': ['C#', 'C#m', 'E', 'F#', 'F#m', 'G#', 'G#m', 'A', 'Am', 'B'],
    '5': ['D', 'Dm', 'F', 'G', 'Gm', 'A', 'Am', 'A#', 'A#m', 'C'],
    '6': ['D#', 'D#m', 'F#', 'G#', 'G#m', 'A#', 'A#m', 'B', 'Bm', 'C#'],
    '7': ['E', 'Em', 'G', 'A', 'Am', 'B', 'Bm', 'C', 'Cm', 'D'],
    '8': ['F', 'Fm', 'G#', 'A#', 'A#m', 'C', 'Cm', 'C#', 'C#m', 'D#'],
    '9': ['F#', 'F#m', 'A', 'B', 'Bm', 'C#', 'C#m', 'D', 'Dm', 'E'],
    '10': ['G', 'Gm', 'A#', 'C', 'Cm', 'D', 'Dm', 'D#', 'D#m', 'F'],
    '11': ['G#', 'G#m', 'B', 'C#', 'C#m', 'D#', 'D#m', 'E', 'Em', 'F#']
}

keyList = ['A', 'Am', 'A#', 'A#m', 'B', 'Bm', 'C', 'Cm', 'C#', 'C#m', 'D', 'Dm', 'D#', 'D#m', 'E', 'Em', 'F', 'Fm', 'F#', 'F#m', 'G', 'Gm', 'G#', 'G#m']

## user input desired chords
chordString = input("Enter chords: ")
chordList = chordString.split()

## identify valid capo positions
validPositions = []
for position in capoPositions:
    if all(elem in capoPositions[position] for elem in chordList):
        validPositions.append(position)

## find new chord shapes and output
if len(validPositions) == 0:
    print("No valid capo positions!  Learn barre chords!")
else:
    for validPosition in validPositions:
        print("Capo position: ", validPosition)
        for chord in chordList:
            firstPositionIndex = keyList.index(chord)
            print(chord, " -> ", keyList[(firstPositionIndex - int(validPosition) * 2)])