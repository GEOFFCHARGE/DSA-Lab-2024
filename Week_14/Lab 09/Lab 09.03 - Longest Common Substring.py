"""Lab 09.03 - Longest Common Substring"""
def main():
    str1 = input()
    str2 = input()
    n = len(str1)
    grid = [[0 for _ in range(n)] for _ in range(n)]
    long_common = 0
    rows_common = 0
    for row in range(n):
        for col in range(n):
            if str1[row] == str2[col]:
                grid[row][col] = grid[row - 1][col - 1] + 1
            if grid[row][col] > long_common:
                long_common = grid[row][col]
                rows_common = row
    if long_common:
        print(str1[rows_common - long_common + 1: rows_common + 1])
        print(long_common)
    else:
        print("No common substring.")
main()
