import numpy as np

def quick_sort(list, length):
    pass

# Load the data from the file
left, right = np.loadtxt('Puzzle 1\puzzle input.txt', unpack=True, dtype=int)

left.sort()
right.sort()

sum = 0
for i, _ in enumerate(left):
    sum = sum + abs(left[i]- right[i])


print(sum)