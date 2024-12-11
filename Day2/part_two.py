from time import time
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.DEBUG)

CONFIG_MAX_ERRORS = 1

def main():
    reports = []
    with open("./example.txt") as f:
        reports = f.readlines()

    safeReports = 0
    for report in reports:
        numbers: list = report.strip("\n").split(" ")
        print("------------------------------------")
        logger.info("Report: %s", ' '.join(numbers))

        prevNumber = 0
        totalErrors = 0

        for idx, number in enumerate(numbers):
            increase, decrease = False, False
            number = int(number)
            nextNumber = 0
            if prevNumber == 0:
                prevNumber = number
                continue
            try:
                nextNumber = int(numbers[idx + 1])
            except IndexError:
                nextNumber = int(number)

            errors = {
                'linear': False,
                'same': False,
                'more3': False
            }

            logger.debug('Comparing numbers %s and %s and %s', prevNumber, number, nextNumber)
            if number - prevNumber > 0:
                logger.debug('Numbers %s and %s and %s are increasing', prevNumber, number, nextNumber)
                increase = True
            if number - prevNumber < 0:
                logger.debug('Numbers %s and %s and %s are decreasing', prevNumber, number, nextNumber)
                decrease = True
            if (number - prevNumber < 0 and nextNumber - number > 0) or (number - prevNumber > 0 and nextNumber - number < 0):
                logger.debug('Numbers %s and %s and %s are decreasing', prevNumber, number, nextNumber)
                decrease = True
                increase = True

            if (number - prevNumber > 3 or nextNumber - number > 3) or (number - prevNumber < -3 or nextNumber - number < -3):
                logger.error('MORE THAN 3 AWAY: Current number %s is %s away from previous number %s.', number, number - prevNumber, prevNumber)
                errors.update({'more3': True})
                totalErrors += 1

            if number == prevNumber:
                logger.error('SAME NUMBER: Current number %s is the same as previous number %s.', number, prevNumber)
                errors.update({'same': True})
                totalErrors += 1
                continue

            if decrease and prevNumber < number and nextNumber < number:
                logger.error('NOT LINEAR: Wrong number in a chain. Current number %s should be less than previous number %s and more than next number %s', number, prevNumber, nextNumber)
                increase, decrease = False, False
                errors.update({'linear': True})
                totalErrors += 1
            if increase and prevNumber > number and nextNumber > number:
                logger.error('NOT LINEAR: Wrong number in a chain. Current number %s should be more than previous number %s and less than next number %s', number, prevNumber, nextNumber)
                increase, decrease = False, False
                errors.update({'linear': True})
                totalErrors += 1

            if increase and decrease:
                logger.error('NOT LINEAR: Report can\'t increase and decrease at the same time %s->%s', "->".join(numbers[0:idx:]), nextNumber)
                increase, decrease = False, False
                errors.update({'linear': True})
                totalErrors += 1

            prevNumber = number

        if totalErrors > CONFIG_MAX_ERRORS:
            logger.error('TOO MANY ERRORS: %s | MAX: %s', totalErrors, CONFIG_MAX_ERRORS)
            continue
        else:
            logger.info("Report is safe")
            safeReports += 1
        logger.debug('Final Report: %s | Total errors: %s', ' '.join(numbers), totalErrors)

    print("------------------------------------")
    print("Safe reports:", safeReports)


if __name__ == "__main__":
    t = time()
    main()
    print(time() - t)

#         for idx, num in enumerate(numbers):
#             if prevnum == 0:
#                 prevnum = int(num)
#                 continue

#             try:
#                 nextnum = int(numbers[idx + 1])
#             except IndexError:
#                 nextnum = int(num)

#             if prevnum < int(num):
#                 incr = True
#             else:
#                 decr = True

#             hasErr = False

#             print(f"{idx} || prev: {int(prevnum)} | cur: {int(num)} | next: {int(nextnum)}")
#             if (int(num) == prevnum) or (decr and incr) or (int(num) - prevnum > 3 or int(num) - prevnum < -3):
#                 print(f"\n\n \
# == : {int(num) == prevnum} \n \
# + and - : {decr and incr} \n \
# > 3 or < -3 : {int(num) - prevnum > 3 or int(num) - prevnum < -3}")
#                 errors = errors + 1
#                 # prevnum = int(numbers[idx - 1])
#                 incr = False
#                 decr = False
#                 print("err:", errors, "\n\n")
#                 hasErr = True
#                 if errors > 1:
#                     safe = False
#                     break
#             prevnum = int(num)
#             finNumbers.append(int(num))
#  print("\nIS SAFE:", safe)
#         print(f"\n {finNumbers}\n\n")
#         if safe:
#             isSafe = isSafe + 1
    # print("safe:", isSafe)
    # safe = True
    #     decr = False
    #     incr = False
    #     errors = 0
    #     prevnum = 0
    #     finNumbers = []