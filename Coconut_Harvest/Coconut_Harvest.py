# Read the input.
# Line 1: two integers T (number of trees) and V (number of villagers).
# Line 2: V numbers, the minutes each villager takes to harvest one tree.
def get_input():
    first = input().split()
    trees = int(first[0])
    # V is given but not otherwise needed; the times list tells us how many.
    times = [int(x) for x in input().split()]
    return trees, times


# How many trees can all villagers harvest within a given time limit?
# A villager who takes p minutes per tree finishes limit // p trees in that
# time, so the total is the sum of those whole-tree counts.
def trees_harvested(times, limit):
    total = 0
    for p in times:
        total += limit // p
    return total


# Find the shortest time in which all the trees can be harvested.
# The number harvested only grows as time increases, so we binary search
# for the smallest time that reaches the required number of trees.
def shortest_time(trees, times):
    if trees == 0:
        return 0

    # Lower bound: 0 minutes harvests nothing.
    # Upper bound: the single fastest villager could harvest every tree alone
    # in trees * (fastest time), which is certainly enough for everyone.
    low = 0
    high = trees * min(times)

    while low < high:
        mid = (low + high) // 2
        if trees_harvested(times, mid) >= trees:
            high = mid          # mid works, look for something smaller
        else:
            low = mid + 1       # mid is too small, go higher

    return low


# Make main
def main():
    trees, times = get_input()
    print(shortest_time(trees, times))


if __name__ == "__main__":
    main()
