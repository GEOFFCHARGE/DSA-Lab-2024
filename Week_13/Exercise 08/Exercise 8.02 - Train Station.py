"""Exercise 8.02 - Train Station"""
def main():
    platform = 0
    reserved = []
    arrive = sorted([float(i) for i in input().replace(" ", "").strip("[]").split(",") if i])
    depart = sorted([float(i) for i in input().replace(" ", "").strip("[]").split(",") if i])
    for i in range(len(arrive)):
        reserved.append((arrive[i], depart[i]))
        reserved = [j for j in reserved if arrive[i] <= j[1]]
        platform = max(platform, len(reserved))
    print(platform)
main()
