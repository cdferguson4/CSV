import csv
import matplotlib.pyplot as plt
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv")

new_file = open("death_valley_2018_simple.csv")

csv_file = csv.reader(open_file,delimiter=",")
new_csv = csv.reader(open_file,delimiter=",")

header_row = next(csv_file)
new_header=next(new_csv)

print(type(header_row))
print(type(new_header))


for index,column_header in enumerate(header_row):
    print(index,column_header)
    print(index,new_header)

new_date = datetime.strptime('2018-07-01','%Y-%m-%d')
print(new_date)

thedate = datetime.strptime('2018-07-01','%Y-%m-%d')
print(thedate)

highs =[]
lows =[]
dates =[]

for rec in csv_file:
    try:
        mydate = datetime.strptime(rec[2],'%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {mydate}")

    else:
        highs.append(int(rec[5]))
        lows.append(int(rec[6]))
        mydate = datetime.strptime(rec[2],'%Y-%m-%d')
        dates.append(mydate)

new_highs = []
new_lows = []
new_dates = []

for recs in new_csv:
    try:
        yourdate = datetime.strptime(rec[2],'%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {yourdate}")
    else:
        new_highs.append(int(rec[4]))
        new_lows.append(int(rec[5]))
        yourdate = datetime.strptime(rec[2],'%Y-%m-%d')
        new_dates.append(yourdate)

fig = plt.figure()

plt.subplot(2,1,1)
plt.title("SITKA AIRPORT, AK US")
plt.plot(dates,highs,c="red",alpha=.5)
plt.plot(dates,lows,c="blue",alpha=.5)
plt.fill_between(dates,highs,lows,facecolor="blue",alpha=.1)


#figs = plt.figure()




new_file = open("death_valley_2018_simple.csv")

new_csv = csv.reader(new_file,delimiter=",")


new_header=next(new_csv)


print(type(new_header))




new_date = datetime.strptime('2018-07-01','%Y-%m-%d')
print(new_date)




new_highs = []
new_lows = []
new_dates = []

for recs in new_csv:
    try:
        yourdate = datetime.strptime(rec[2],'%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {yourdate}")
    else:
        new_highs.append(rec[4])
        new_lows.append(rec[5])
        yourdate = datetime.strptime(rec[2],'%Y-%m-%d')
        new_dates.append(yourdate)




plt.subplot(2,1,2)
plt.title("death valley")
plt.plot(new_dates,new_highs,c="red",alpha=.5)
plt.plot(new_dates,new_lows,c="blue",alpha=.5)
plt.fill_between(new_dates,new_highs,new_lows,facecolor="blue",alpha=.1)



plt.suptitle("Temperature comparison between SITKA AIRPORT, AK US an DEATH VALLEY, CA")

plt.show()
