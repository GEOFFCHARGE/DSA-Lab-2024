"""(ยากมาก) - อาจารย์ขิมกับกุญแจแห่งเกาะแมวสยาม"""
def อาจารย์ขิมกับกุญแจแห่งเกาะแมวสยาม():
    texts = input()
    lasts = {j: i for i, j in enumerate(texts)}
    stack = []
    for i, j in enumerate(texts):
        if j in stack:
            continue
        while stack and j < stack[-1] and lasts[stack[-1]] > i:
            stack.pop()
        stack.append(j)
    print(*stack, sep="")
อาจารย์ขิมกับกุญแจแห่งเกาะแมวสยาม()
