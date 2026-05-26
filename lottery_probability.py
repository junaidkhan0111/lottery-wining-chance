import math

def combinations(n, k):
    return math.comb(n, k)

def lottery_probability(total_numbers, numbers_chosen, tickets_bought):
    total_combinations = combinations(total_numbers, numbers_chosen)
    probability = tickets_bought / total_combinations
    return probability, total_combinations

def main():
    print("Lottery Winning Chance Calculator\n")

    n = int(input("Enter total numbers in lottery: "))
    k = int(input("Enter numbers chosen: "))
    t = int(input("Enter number of tickets bought: "))

    probability, total = lottery_probability(n, k, t)

    print("\nResults:")
    print(f"Total possible combinations: {total}")
    print(f"Winning probability: {probability}")
    print(f"That is 1 in {int(1/probability)} chance")

if __name__ == "__main__":
    main()
