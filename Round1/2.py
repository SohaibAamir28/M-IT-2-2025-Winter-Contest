def farmer_john_card_game(t, test_cases):
    results = []

    for case in test_cases:
        n, m, cards = case
        order = list(range(1, n + 1))  # Start with the default permutation [1, 2, ..., n]

        # Sort cows by their smallest card
        sorted_cows = sorted(range(n), key=lambda x: min(cards[x]))
        order = [cow + 1 for cow in sorted_cows]  # Adjust 0-based to 1-based indexing

        valid = True
        center_pile = -1
        for _ in range(m):
            for cow in order:
                # Find the smallest valid card for the current cow
                valid_cards = [card for card in cards[cow - 1] if card > center_pile]
                if not valid_cards:
                    valid = False
                    break
                center_pile = min(valid_cards)
                cards[cow - 1].remove(center_pile)
            if not valid:
                break

        if valid:
            results.append(" ".join(map(str, order)))
        else:
            results.append("-1")

    return results

# Input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []
index = 1
for _ in range(t):
    n, m = map(int, data[index].split())
    cards = [list(map(int, data[index + i + 1].split())) for i in range(n)]
    test_cases.append((n, m, cards))
    index += n + 1

# Output
results = farmer_john_card_game(t, test_cases)
print("\n".join(results))
