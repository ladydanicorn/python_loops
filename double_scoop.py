#Assignment 2
 
import random

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
mood = ['happy', 'sad', 'angry', 'excited', 'relaxed', 'bored', 'anxious']
time_of_day = ['morning', 'afternoon', 'evening']

for i in range(7):
    day = days[i]
    current_mood = random.choice(mood)
    time = random.choice(time_of_day)
    print(f"On {day} in the {time}, you were feeling {current_mood}.")