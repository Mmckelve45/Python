import datetime
t = datetime.time(5,25,1)


print(t)
t.hour
t.minute
t.second
t.microsecond

datetime.tim.min
print(datetime.time.max)
print(datetime.time.resolution)


today = datetime.date.today()
print(today)

today.timetuple()
today.day

print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.resolution)

d1 = datetime.date(2015,3,11)
print(d1) #2015-03-11

d2 = d1.replace(year=1990)

d1-d2 #returns time delta (days)
