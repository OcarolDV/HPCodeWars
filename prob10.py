import math

Alphabet = {"A": 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
            'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
            'Z': 26, "!": 1, "'": 1, " ": 1}

pInput = "12 Do Tee!iscdh"
charnum = int(pInput[0:2])
decoded = pInput[3: charnum+3]
Empty = ""

for i in range(charnum):
    Empty = Empty + ' '

c = 0
d = 0
for i in decoded:
    if i == decoded[0]:
        Empty = i + Empty[c:]
    d = d + 1
    if Alphabet[i.upper()] < charnum - c:
        Empty = Empty[0:Alphabet[i.upper()]] + decoded[c+1] + Empty[Alphabet[i.upper()]:]
    elif Alphabet[i.upper()] < 2 * (charnum - c):
        Empty = Empty[0:charnum - Alphabet[i.upper()]] + decoded[c + 1] + Empty[charnum - Alphabet[i.upper()]:]
    # elif Alphabet[i.upper()] < 3 * (charnum - c):
    #     Empty = Empty[0:2 * charnum - Alphabet[i.upper()]] + decoded[c + 1] + Empty[2 * charnum - Alphabet[i.upper()]:]

    c = c + 1

print (Empty)









# x = "Hello"
# print (Alphabet[x.upper()[2]])