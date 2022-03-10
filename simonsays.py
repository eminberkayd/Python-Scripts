
"""
Basic Simon Says game implemented in Python

It should be worked on command prompt to show its all functionality. Otherwise it will not.
"""

import random
import os
import time
import string

diff = int(input("""Choose your difficulty level:
    (1) - Easy
    (2) - Medium
    (3) - Hard
    (4) - Insane
    """))
if diff == 1:
    s_time=2
elif diff == 2:
    s_time = 1.2
elif diff == 3:
    s_time = 0.8
elif diff == 4:
    s_time = 0.2

colors = string.ascii_uppercase + string.digits
simon = ""

for score in range(999):
    simon += random.choice(colors)
    for item in simon:
        print(item)
        time.sleep(s_time)
        os.system("cls")
    guess = input("Repeat: ")
    os.system("cls")
    if guess.upper() != simon:
        break

print(f"Game Over! Your final score is {score}!")
