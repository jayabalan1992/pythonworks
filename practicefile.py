import time, calendar
print(time.ctime())
print(time.asctime(time.localtime(time.time())))
print(time.ctime(time.time()))
print(calendar.setfirstweekday(1))