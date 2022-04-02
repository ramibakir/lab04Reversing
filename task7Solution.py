snTotal = 14

unicodeValues = []
firstHalf = []
secondHalf = []
letters = []

with open("task7.txt", 'r') as file:
    for value in file:
        strippedValue = value.replace("\n", "")
        unicodeValues.append(int(strippedValue))

#print(unicodeValues)
reversedValues = unicodeValues[::-1]
length = len(reversedValues)
mid_split = length//2
firstHalf = reversedValues[:mid_split]
secondHalf = reversedValues[mid_split:]

for fH, sH in zip(firstHalf, secondHalf):
    chr_val = fH + snTotal
    chr_val2 = sH + snTotal
    letters.append(chr(chr_val))
    letters.append(chr(chr_val2))

print(''.join(map(str, letters)))


