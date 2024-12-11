from time import time
import re

def main():
    lines = []
    with open("./input.txt") as f:
        lines = f.readlines()
    # mul\([0-9]*,[0-9]*\)
    answer = 0
    for line in lines:
        search = r"mul\([0-9]*,[0-9]*\)"
        matches = re.findall(search, line)
        for match in matches:
            match = match.replace("mul(", "").replace(")", "")
            dig1 = int(match.split(",")[0])
            dig2 = int(match.split(",")[1])
            res = dig1 * dig2
            print(f"{dig1} * {dig2} = {res}")
            answer += res
    print(answer)

if __name__ == "__main__":
    t = time()
    print(t)
    main()
    print(time())
    print(time() - t)