
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

    # Sort lists from smallest to largest
    locationID.sort()
    print(f"Locations: {locationID}")
    distance.sort()
    print(f"Distances: {distance}")

    # Get the difference from locationID[i] to distance[i] and store it in a new list
    totalDistance = []
    for i in range(len(locationID)):
        dist = int(distance[i]) - int(locationID[i])
        if dist < 0:
            dist *= -1
        totalDistance.append(dist)
    print(f"total Distances: {totalDistance}")

    # Calculate the total distance
    total = 0
    for i in range(len(totalDistance)):
        total += totalDistance[i]

    print(f"Total Distance: {total}")

if __name__ == "__main__":
    main()