from time import time

def findWord(lines, x, y):
    count = 0

    if x == 0 or (x - 1 < 0):
        return 0
    if x == len(lines[0]) or (len(lines[0]) - x - 1 < 0):
        return 0

    if y == 0 or (y - 1 < 0):
        return 0
    if y == len(lines) or (len(lines) - y - 1 < 0):
        return 0

    try:
        print(f"""
{lines[y-1][x-1]}.{lines[y-1][x+1]}
.{lines[y][x]}.
{lines[y+1][x-1]}.{lines[y+1][x+1]}
""", end="")
    except IndexError:
        pass

    #
    # M.S
    # .A.
    # M.S
    #
    try:
        if lines[y - 1][x - 1] == "M" and lines[y + 1][x + 1] == "S" and lines[y + 1][x - 1] == "M" and lines[y - 1][x + 1] == "S":
            count += 1
            print(f"""
--ADDED---
M.S
.A.
M.S
----------
""")
    except IndexError:
        pass

    #
    # M.M
    # .A.
    # S.S
    #
    try:
        if lines[y - 1][x - 1] == "M" and lines[y - 1][x + 1] == "M" and lines[y + 1][x - 1] == "S" and lines[y + 1][x + 1] == "S":
            count += 1
            print(f"""
--ADDED---
M.M
.A.
S.S
----------
""")
    except IndexError:
        pass

    #
    # S.S
    # .A.
    # M.M
    #
    try:
        if lines[y - 1][x - 1] == "S" and lines[y - 1][x + 1] == "S" and lines[y + 1][x - 1] == "M" and lines[y + 1][x + 1] == "M":
            count += 1
            print(f"""
--ADDED---
S.S
.A.
M.M
----------
""")
    except IndexError:
        pass

    #
    # S.M
    # .A.
    # S.M
    #
    try:
        if lines[y - 1][x - 1] == "S" and lines[y + 1][x + 1] == "M" and lines[y + 1][x - 1] == "S" and lines[y - 1][x + 1] == "M":
            count += 1
            print(f"""
--ADDED---
S.M
.A.
S.M
----------
""")
    except IndexError:
        pass

    return count


def main():
    lines = []
    with open("./input.txt") as f:
        read = f.readlines()
        for line in read:
            lines.append(line.replace("\n", ""))


    answer = 0
    x, y = 0, 0
    for line in lines:
        x = 0
        for char in line:
            if char == "A":
                answer += findWord(lines, x, y)
            x += 1
        y += 1
    print("\n", "answer:", answer)

if __name__ == "__main__":
    t = time()
    main()
    print(time() - t)