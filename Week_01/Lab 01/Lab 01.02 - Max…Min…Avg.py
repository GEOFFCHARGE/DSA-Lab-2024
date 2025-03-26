"""Lab 01.02 - Max…Min…Avg"""
import json
def spam():
    my_list = json.loads(input())
    high = my_list[0]
    lows = my_list[0]
    for i in my_list:
        if i > high:
            high = i
        if i < lows:
            lows = i
    high = round(high, 2)
    lows = round(lows, 2)
    aver = round((sum(my_list) / len(my_list)), 2)
    print(f"({high}, {lows}, {aver})")
spam()
