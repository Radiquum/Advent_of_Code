
def main():
    # Create 2 empty lists
    locationID = []
    distance = []

    # Open the file and read the lines
    with open("./input.txt") as f:
        for line in f.readlines():
            curLine = line.strip()
            items = curLine.split()
            locationID.append(items[0])
            distance.append(items[1])

    numbers = {}

    # For each number in left list find all of it in the right list
    for i in range(len(locationID)):
        numbers[locationID[i]] = distance.count(locationID[i])


    # Count the similarity score
    simScores = []
    for i in range(len(locationID)):
        simScores.append(int(locationID[i]) * int(numbers[locationID[i]]))

    simScoreCount = 0
    for i in range(len(simScores)):
        simScoreCount += int(simScores[i])
    print(f"Similarity Score: {simScoreCount}")

if __name__ == "__main__":
    main()