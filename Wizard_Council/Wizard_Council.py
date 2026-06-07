# Read the input.
# Line 1: two integers C (committees) and B (bills).
# Line 2: exactly B letters, each P, R or Q.
def get_input():
    first = input().split()
    committees = int(first[0])
    # B is given but not otherwise needed. Keep only the bill letters, which
    # works whether or not they happen to arrive with spaces between them.
    bills = [c for c in input() if c in "PRQ"]
    return committees, bills


# Determine the largest number of bills that can be rejected.
#
# P always passes and R always rejects regardless of allocation, so the only
# freedom is in the Q bills. A Q is rejected when it is first in its committee
# or follows a passed bill, and passed when it follows a rejected bill.
#
# Track G, the number of committees currently in a "good" state for us, i.e.
# empty or with a passed last bill, so a Q placed there would be rejected.
# A committee whose last bill was rejected is "bad": a Q placed there passes.
def max_rejected(committees, bills):
    good = committees   # every committee starts empty, which counts as good
    rejected = 0

    for bill in bills:
        if bill == "P":
            # Passes anyway; spend it flipping a bad committee good if possible.
            good = min(good + 1, committees)
        elif bill == "R":
            # Always rejected; place on an already-bad committee when one
            # exists so we only sacrifice a good slot if every committee is good.
            rejected += 1
            good = min(good, committees - 1)
        else:  # bill == "Q"
            if good >= 1:
                # Place after a passed bill (or as the first) so it is rejected.
                rejected += 1
                good -= 1
            else:
                # Every committee is bad, so this Q is forced to pass; doing so
                # turns that committee good for the next bill.
                good += 1

    return rejected


# Make main
def main():
    committees, bills = get_input()
    print(max_rejected(committees, bills))


if __name__ == "__main__":
    main()
