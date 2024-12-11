from time import time
def main():
    reports = []
    with open("./input.txt") as f:
        reports = f.readlines()

    isSafe = 0
    for idx, report in enumerate(reports):
        prevnum = 0
        nextnum = 0
        numbers = report.split(" ")
        safe = True
        decr = False
        incr = False
        for idxx, num in enumerate(numbers):
            if prevnum == 0:
                prevnum = int(num)
                continue

            try:
                nextnum = int(numbers[idxx + 1])
            except IndexError:
                nextnum = int(num)

            if prevnum < int(num):
                incr = True
            else:
                decr = True

            if int(num) == prevnum or decr and incr:
                safe = False
                break

            if int(num) - prevnum > 3 or int(num) - prevnum < -3:
                safe = False
                break

            prevnum = int(num)
        if safe:
            isSafe = isSafe + 1

    print("safe:", isSafe)

if __name__ == "__main__":
    t = time()
    main()
    print(time() - t)
