"""BubbleV2 ( Medium )"""
def bubbleV2():
    bubble = [i for i in input()]
    temper = [int(i) for  i in input().split()]
    jumper = [None for _ in range(len(bubble))]
    jumper[0] = 1
    for i in temper:
        for j in range(len(bubble)):
            if bubble[j] == "o" and jumper[j] == None:
                jumper[j] = i
                break
    temper = [None for _ in range(len(bubble))]
    temper[0] = 0
    for i in range(len(bubble)):
        if jumper[i] == None or temper[i] == None:
            continue
        for j in range(1, jumper[i] + 1):
            if i + j < len(bubble) and bubble[i + j] != "_":
                if temper[i + j] == None:
                    temper[i + j] = temper[i] + 1
                else:
                    temper[i + j] = min(temper[i + j], temper[i] + 1)
    if temper[len(bubble) - 1] != None:
        print(temper[len(bubble) - 1])
    else:
        print(-1)
bubbleV2()
