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
        print(numbers)
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
                print(f"increases\n {prevnum} < {int(num)}")

            if prevnum > int(num) :
                decr = True
                print(f"decreases\n {prevnum} > {int(num)}")

            if (int(num) == prevnum):
                print(f"not and increase nor a decrease\n {prevnum} == {int(num)}")
                safe = False
                break

            if decr and incr:
                print("not always increases or decreases")
                safe = False
                break

            if incr and int(num) - prevnum > 3:
                print(f"increases not by 1, 2 or 3 | {int(num)} - {prevnum} == {int(num) - prevnum}")
                safe = False
                break
            if decr and prevnum - int(num) > 3:
                print(f"decreases not by 1, 2 or 3 | {prevnum} - {int(num)} == {prevnum - int(num)}")
                safe = False
                break

            prevnum = int(num)
        if safe:
            print("SAFE")
            isSafe = isSafe + 1
        else:
            print("NOT SAFE")
        print("\n--------------------------------------------------------------------------------\n")

    print("safe:", isSafe)

if __name__ == "__main__":
    t = time()
    print(t)
    main()
    print(time())
    print(time() - t)
