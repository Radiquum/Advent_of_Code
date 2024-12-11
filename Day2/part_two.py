from time import time
class ReportIsNotSafe(Exception):
    pass
def isSequenceSafe(report):
    prevnum = 0
    decr = False
    incr = False
    isSafe = True
    for num in report:
        if prevnum == 0:
            prevnum = num
            continue

        if prevnum < num:
            incr = True
        else:
            decr = True

        if (num == prevnum) or (decr and incr) or (num - prevnum > 3 or num - prevnum < -3):
            raise ReportIsNotSafe
        prevnum = num
    return isSafe


def main():
    reports = []
    with open("./input.txt") as f:
        reports = f.readlines()

    safeReports = 0
    for report in reports:
        report = report.split(" ")
        sanReport = []
        for num in report:
            sanReport.append(int(num))

        try:
            if isSequenceSafe(sanReport):
                safeReports += 1
        except ReportIsNotSafe:
            for i, _ in enumerate(sanReport):
                modReport = sanReport.copy()
                modReport.pop(i)

                try:
                    if isSequenceSafe(modReport):
                        safeReports += 1
                        break
                except ReportIsNotSafe:
                    pass

    print("Safe reports:", safeReports)


if __name__ == "__main__":
    t = time()
    main()
    print(time() - t)
