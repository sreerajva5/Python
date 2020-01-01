from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

today = date.today()

print("Today's date is ", today)
print("Todays date is %d, current month is %dth month and year is %d." %(today.day, today.month, today.year))
print("Today's weekday is ", today.weekday())




dt = datetime.now()
t = datetime.time(datetime.now())

print("Today's date and time : ", dt)
print("Current time is ", t)



wd = date.weekday(today)   #Days start at 0 for Monday
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("Today's day number is %d which is a %s" %(wd,days[wd]))



now = datetime.now()
print(now)
print(now.strftime("%Y"))  # extracting year
print(now.strftime("%y"))  # extracting year in short # ie 19 instead of 2019
print(now.strftime("%A%d%B%y"))  # day and date in format -Tuesday01October19
print(now.strftime("%c"))  #extract in format Tue Oct  1 12:50:04 2019
print(now.strftime("%X"))   # extract time 12:50:04
print(now.strftime("%x"))    # extract date in format 10/01/19
print(now.strftime("%I:%M:%S %p"))   # extract time with AM,PM
print(now.strftime("%H:%M")) # extract time without AM, PM

print("----------------")


print(timedelta(days = 365, hours = 8, minutes = 15))
print("One year from now it will be : ",str(datetime.now() + timedelta(365)))
print("In one week and four days, it will be : ", str(datetime.now()+timedelta(weeks=1, days=4)))
