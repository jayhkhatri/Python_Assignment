import random

# random() -returns random float between 0.0 and 1.0 excluded
nums = [10, 4, 5, 8, 1, 3]
print(random.random())
print(random.randint(1, 10))
print(random.choice(nums))
random.shuffle(nums)
print(nums)