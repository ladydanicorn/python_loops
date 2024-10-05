#Assignment 1

import random

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 
mood = ['happy', 'sad', 'angry', 'excited', 'relaxed', 'bored', 'anxious']

for i in range(7):
    day = days[i]
    mood = random.choice(mood)
    print(f"On {day}, you were feeling {mood}.")