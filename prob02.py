upc1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def checkDigit(upc):
    even = 0
    odds = 0
    for i in upc:
        if i % 2 == 0:
            odds = odds + upc[i]
        else:
            even = even + upc[i]

    total = (odds * 3) + even
    total = total % 10

    if total != 0:
        total = 10 - total


    upc.append(total)
    print(upc)


checkDigit(upc1)


