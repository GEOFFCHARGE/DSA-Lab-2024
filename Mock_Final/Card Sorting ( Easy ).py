"""Card Sorting ( Easy )"""
def cardSort(list, last):
    cardUnit = ["C", "D", "H", "S"]
    cardFace = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    current = 0
    sorted = False
    while current <= last and not sorted:
        walker = last
        sorted = True
        while walker > current:
            if cardUnit.index(list[walker][-1]) < cardUnit.index(list[walker - 1][-1]) or \
                (cardUnit.index(list[walker][-1]) == cardUnit.index(list[walker - 1][-1]) and \
                cardFace.index(list[walker][:-1]) < cardFace.index(list[walker - 1][:-1])):
                sorted = False
                list[walker], list[walker - 1] = list[walker - 1], list[walker]
            walker -= 1
        current += 1
    return list[::-1]

def cardPoint(card):
    point = 0
    for i in card:
        if i in ("2C", "QS"):
            point += 50
        elif i[0] == "A":
            point += 15
        elif i[:-1] in ("10", "J", "Q", "K"):
            point += 10
        else:
            point += 5
    return point

def playerSort(list, last):
    current = 0
    sorted = False
    while current <= last and not sorted:
        walker = last
        sorted = True
        while walker > current:
            if list[walker][1] < list[walker - 1][1] or \
                (list[walker][1] == list[walker - 1][1] and \
                list[walker][0] < list[walker - 1][0]):
                sorted = False
                list[walker], list[walker - 1] = list[walker - 1], list[walker]
            walker -= 1
        current += 1
    return list[::-1]

import json
def main():
    n = int(input())
    m = int(input())
    player = [json.loads(input()) for _ in range(n)]
    for i in player:
        i.append(cardSort(i[1], m - 1))
        i[1] = cardPoint(i[2])
    player = playerSort(player, n - 1)
    for i in player:
        print(f"{i[0]} -> {i[1]} -> {i[2]}")
main()
