"""
Prac 03 - Random
Student: Dawei ZHU - 14613428
"""
import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# Answer:
#   I see 6.
#   From 5 to 20, inclusive.

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# Answer:
#   I see 7.
#   Min:3, max: 9.
#   It does not have 4 as its element.

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# Answer:
#   I see 3.3569414037103855.
#   Min 2.5, max: 5.5.

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
