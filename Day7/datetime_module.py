import datetime

#3 classes of datetime module
#datetime
#date
#timedelta

print(datetime.datetime.now())

print(datetime.date.today())


#date class

d=datetime.date(2022,3,29) #object of date class
print(d)
print(type(d))

print(d.year)
print(d.month)
print(d.day)

#datetime class
#year month day hour minute second microsecond
d=datetime.datetime(2022,3,29,1,34,55,456) #object of datetime class
print(d)
print(type(d))

print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.timestamp()) # 1 jan 1970 to 29 march 2022


#timestamp to date
date_ts= datetime.date.fromtimestamp(1648497895.000456)
print(date_ts)

#Time class
#hour minute second microsecond
t= datetime.time(11,34,56,345)
print(t)
print(t.hour)
print(t.minute)
print(t.second)

#Timedelta Class
d1=datetime.date(2022,3,29)
d2=datetime.date(2021,3,29)
d3 =d1-d2
print(d3)
print(type(d3))

#differnce between two timedelta objects
t1=datetime.timedelta(weeks=2,days=5,hours=3,seconds=33)
t2=datetime.timedelta(weeks=5,days=3,hours=4,seconds=24)
t3=t1-t2
print(t3)

print(t1.total_seconds())

import datetime

#Formate Date using strftime

d= datetime.datetime.now()

print(d.strftime("%d-%b-%Y %A %I%p"))
#d -> day
#m -> month
#Y -> year
#B -> full name of month
#b -> month ab
#H -> hour
#M -> minutes
#S -> seconds
#I -> hour(12 hr clock)
