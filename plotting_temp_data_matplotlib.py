import csv
import matplotlib.pyplot as plt
from datetime import datetime



filename='data/sitka_weather_2018_simple.csv'

fig, ax=plt.subplots(figsize=(15,6))




#['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']
t_avg=[]
t_min=[]
t_max=[]
dates=[]
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    for row in reader:
        t_min.append(int(row[6]))
        t_max.append(int(row[5]))
        avg=int(row[5])+ int(row[6])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')           #dates are initially stored as string. This converts the dates into an object representing a date
        dates.append(current_date)
        
        t_avg.append(avg//2)


plt.style.use('seaborn')


ax.plot(dates,t_avg,c='blue', alpha=0.7)                #alpha controls how transparent a colour is from 0 to 1 values
ax.plot(dates,t_min,c='green', alpha=0.7)
ax.plot(dates,t_max,c='red', alpha=0.7)
ax.set_title('Average Temperatures in Sitka 2018',fontsize=20)
ax.set_xlabel('Dates',fontsize=15)
fig.autofmt_xdate()                                             #This formats the dates in a better way
ax.set_ylabel('Average Temperatures', fontsize=15)
plt.fill_between(dates, t_max, t_avg, facecolor='orange', alpha=0.4)
plt.fill_between(dates, t_min, t_avg, facecolor='yellow', alpha=0.4)

ax.tick_params(axis='both',labelsize=10)
plt.savefig('matplotlib_temps.png', bbox_inches='tight')
plt.show()
