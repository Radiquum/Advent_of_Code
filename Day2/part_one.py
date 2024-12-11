from time import time
def main():
    reports = []
    with open("./input.txt") as f:
        reports = f.readlines()

    isSafe = 0
    for report in reports:
        prevnum = 0
        numbers = report.split(" ")
        safe = True
        decr = False
        incr = False
        for num in numbers:
            num = int(num)
            if prevnum == 0:
                prevnum = num
                continue

            if prevnum < num:
                incr = True
            else:
                decr = True

            if num == prevnum or decr and incr:
                safe = False
                break

            if num - prevnum > 3 or num - prevnum < -3:
                safe = False
                break

            prevnum = num
        if safe:
            isSafe = isSafe + 1

    print("safe:", isSafe)

if __name__ == "__main__":
    t = time()
    main()
    print(time() - t)
