
"""
This program demonstrates datetime handling by creating and displaying specific dates,
times, formatted timestamps, and comparing a target date with the current date
"""

import datetime
date=datetime.date(2025,1,2)
print(date)
today=datetime.date.today()
print(today)

time=datetime.time(12,30,0)
print(time)
now=datetime.datetime.now()
now=now.strftime("%H:%M:%S %m-%d-%Y")
print(now)
target_datetime=datetime.datetime(2030,1,2,12,30,1)
current_date=datetime.datetime.now()
if target_datetime<current_date:
    print("date passed")
else:
    print('not passed')