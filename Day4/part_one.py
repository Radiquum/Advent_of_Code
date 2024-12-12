from time import time

def findWord(lines, line, x, y):
    count = 0
    directions = {
        "up": True,
        "down": True,
        "left": True,
        "right": True,
    }

    if x == 0 or (x - 3 < 0):
        directions["left"] = False
    if x == len(line) or (len(line) - x - 3 < 0):
        directions["right"] = False

    if y == 0 or (y - 3 < 0):
        directions["up"] = False
    if y == len(lines) or (len(lines) - y - 3 < 0):
        directions["down"] = False

    if directions['right']:
        r = line[x:x+4]
        if r == "XMAS":
            count += 1
    if directions['left']:
        l = line[x-3:x+1]
        if l == "SAMX":
            count += 1

    if directions['up'] :
        try:
            if lines[y][x] == "X" and lines[y - 1][x] == "M" and lines[y - 2][x] == "A" and lines[y - 3][x] == "S":
                count += 1
        except IndexError:
            pass

    if directions['down']:
        try:
            if lines[y][x] == "X" and lines[y + 1][x] == "M" and lines[y + 2][x] == "A" and lines[y + 3][x] == "S":
                count += 1
        except IndexError:
            pass

    if directions['up'] and directions["right"]:
        try:
            if lines[y][x] == "X" and lines[y - 1][x + 1] == "M" and lines[y - 2][x + 2] == "A" and lines[y - 3][x + 3] == "S":
                count += 1
        except IndexError:
            pass
    if directions['down'] and directions["right"]:
        try:
            if lines[y][x] == "X" and lines[y + 1][x + 1] == "M" and lines[y + 2][x + 2] == "A" and lines[y + 3][x + 3] == "S":
                count += 1
        except IndexError:
            pass
    if directions['up'] and directions["left"]:
        try:
            if lines[y][x] == "X" and lines[y - 1][x - 1] == "M" and lines[y - 2][x - 2] == "A" and lines[y - 3][x - 3] == "S":
                count += 1
        except IndexError:
            pass
    if directions['down'] and directions["left"]:
        try:
            if lines[y][x] == "X" and lines[y + 1][x - 1] == "M" and lines[y + 2][x - 2] == "A" and lines[y + 3][x - 3] == "S":
                count += 1
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
        # print(y, line)
        for char in line:
            if char == "X":
                answer += findWord(lines, line, x, y)
            x += 1
        y += 1
    print("\n", "answer:", answer)

if __name__ == "__main__":
    t = time()
    main()
    print(time() - t)