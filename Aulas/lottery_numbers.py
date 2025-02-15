import random

# Generate 6 unique numbers between 1 and 60
lottery_numbers = random.sample(range(1, 61), 6)

# Sort the numbers in ascending order
lottery_numbers.sort()

print("Números sorteados:", lottery_numbers)
