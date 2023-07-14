#Developed by Tyler bershad
#Last Modified: 12/17/2022
#Purpose: Plot data of interest on graph. 

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

#Read in the data from excel/csv
df_exp2 = pd.read_excel('12-14-22_Exp1R_Raw.xlsx')

#Store columns from data of interest in 
airTemp_exp2 = df_exp2.iloc[:,1]
spaTemp_exp2 = df_exp2.iloc[:,2]
unixT_exp2 = df_exp2.iloc[:,3]

unixT_exp2_baseline = unixT_exp2[5] #setting 2 to the baseline to clean the data a bit

unixT_exp2_subt = []
#Convert the Unix time to usable time
for x in range(len(unixT_exp2)):
    unixT_exp2_subt.append(unixT_exp2[x]-unixT_exp2_baseline)    
#print(unixT_exp1_subt)

unixT_exp2_time = []
for x in range(len(unixT_exp2_subt)):
    unixT_exp2_time.append(int(unixT_exp2_subt[x]))

unixT_exp2_time2 = []
for x in range(len(unixT_exp2_time)):
    unixT_exp2_time2.append(datetime.utcfromtimestamp(unixT_exp2_time[x]).strftime('%H:%M:%S')) #Only grab Hours, mins, Sec

spaTemp_fixed = []
airTemp_fixed = []
for x in range(len(spaTemp_exp2)):
    if spaTemp_exp2[x] != "NAN":
        spaTemp_fixed.append(spaTemp_exp2[x])
        airTemp_fixed.append(airTemp_exp2[x])
#print(spaTemp_fixed)

unixT_fixed = []
for x in range(len(spaTemp_fixed)):
    unixT_fixed.append(unixT_exp2_time2[x])
#print (unixT_fixed)

SpaTemp_final = []
unixT_final = []
airTemp_final = []
for x in range(len(unixT_fixed)-1):
    if spaTemp_fixed[x+1]-spaTemp_fixed[x] !=0:
        SpaTemp_final.append(spaTemp_fixed[x])
        unixT_final.append(unixT_fixed[x])
        airTemp_final.append(airTemp_fixed[x])
        
SpaTemp_final2 = []
unixT_final2 = []
airTemp_final2 = []
for x in range(len(unixT_final)):
    if x > 1:
        SpaTemp_final2.append(SpaTemp_final[x])
        unixT_final2.append(unixT_final[x])
        airTemp_final2.append(airTemp_final[x])

# print(SpaTemp_final2)        
# print(unixT_final2)
# print(airTemp_final2)

# print(len(SpaTemp_final2))
# print(len(unixT_final2))
# print(len(airTemp_final2))

sec = 1/60 #1 minute in 60 seconds
hours = 60 #60 minutes in 1 hour
time_min = []
for x in range(len(unixT_final2)):
    sec2min_1 = int(unixT_final2[x][6:])
    sec2min_2 = float((1/60)*sec2min_1)
    hr2min_1 = int(unixT_final2[x][:2])
    hr2min_2 = int(60*hr2min_1)
    if unixT_final2[x][3] == "0":
        mins = int(unixT_final2[x][4])
    else:
        mins = int(unixT_final2[x][3:5])
    time_min.append(round(hr2min_2+sec2min_2+mins,1))
#print(time_min)


plt.plot(time_min,airTemp_final2,'y^')
avg_air = sum(airTemp_final2)/len(airTemp_final2)
avg_air_final = []

for x in range(len(SpaTemp_final2)):
    avg_air_final.append(avg_air)
plt.plot(time_min,avg_air_final,'b--')
plt.text(40,79, 'Ambient Avg: {:.2f} °F'.format(avg_air))


plt.plot(time_min,SpaTemp_final2, 'o', c ="black")
plt.xticks(rotation=75)
plt.title("Spa Temperature (°F) vs Time (min)")
plt.xlabel("Time (min)")
plt.ylabel("Spa Temperature (°F)")
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

#find line of best fit
SpaTemp_final3 = np.array(SpaTemp_final2)
time_final = np.array(time_min)
a, b = np.polyfit(time_final, SpaTemp_final3, 1)
plt.plot(time_final, a*time_final+b,'r--')        
plt.text(60,92, 'y = ' '{:.2f}'.format(a) + 'x + '+'{:.2f}'.format(b) , size=11)

r_squared_value = r2_score(SpaTemp_final3, a*time_final+b)
plt.text(60,89, 'R2 = ' '{:.4f}'.format(r_squared_value), size=11)
plt.ylim([75, 105])
plt.xticks([0,5,10,15,20,25,30,25,30,35,40,45,50,55,60,65,70,75,80])
plt.legend(['Air Temp','Avg Air Temp','Spa Temp','Spa Temp Fitted Line'])

plt.show()