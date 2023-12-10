from collections import Counter

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
alphabet = "AKQJT98765432"

def classify(hand):
    counter = Counter(hand)
    nums = [counter[card] for card in cards]
    #print(nums)
    if max(nums) == 5: return "five_of_a_kind"
    elif max(nums) == 4: return "four_of_a_kind"
    elif max(nums) == 3 and 2 in nums: return "full_house"
    elif max(nums) == 3: return "tree_of_a_kind"
    elif nums.count(2) == 2: return "two_pairs"
    elif max(nums) == 2: return "one_pair"
    else: return "high_card"

def order(hands, start_rank):
    sorted_hands = sorted(hands, key=lambda hand: [alphabet.index(card) for card in hand[0]], reverse=True)
    cumsum = 0
    rank = start_rank
    for hand in sorted_hands:
        #print(int(hand[1]), "*", rank)
        cumsum += int(hand[1])*rank
        rank += 1
    return cumsum, rank

with open("input", "r") as file:
    hands = []
    for line in file:
        hands.append(line.split())
    max_rank = len(hands)
    fives, fours, fulls, threes, twopairs, pairs, highs = [], [], [], [], [], [], []
    for hand in hands:
        type = classify(hand[0])
        print(type)
        match type:
            case "five_of_a_kind":
                fives.append(hand)
            case "four_of_a_kind":
                fours.append(hand)
            case "full_house":
                fulls.append(hand)
            case "tree_of_a_kind":
                threes.append(hand)
            case "two_pairs":
                twopairs.append(hand)
            case "one_pair":
                pairs.append(hand)
            case "high_card":
                highs.append(hand)

    rank = 1
    cumsum = 0
    print()
    for sub_hands in [highs, pairs, twopairs, threes, fulls, fours, fives]:
        if sub_hands:
            print(classify(sub_hands[0][0]), len(sub_hands))
            sum, rank = order(sub_hands, rank)
            print(sum, rank)
            cumsum += sum

    print(cumsum)