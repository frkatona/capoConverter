## define valid chords for all capo positions
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

## user input desired chords
chordString = input("Enter chords: ")
chordList = chordString.split()
print(chordList)

## identify valid capo positions
validPositions = []
for position in capoPositions:
    if all(elem in capoPositions[position] for elem in chordList):
        validPositions.append(position)

## output
if len(validPositions) != 0:
    print("Valid capo positions: ", validPositions)
else:
    print("No valid capo positions!  Learn barre chords!")