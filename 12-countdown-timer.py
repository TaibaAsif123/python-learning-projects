
"""
This program creates a countdown timer that converts user input in seconds to
HH:MM:SS format and counts down to zero with one-second intervals
"""

import time
#time.sleep will sleep the program for whatever seconds
my_time=int(input("Enter time in seconds:"))
for x in range(my_time,0,-1):
    seconds=x % 60 #modulus 60 so seconds dont go above 60
    minutes=int(x/60)%60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIMES'S UP!")