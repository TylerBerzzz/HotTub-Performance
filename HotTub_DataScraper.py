# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:47:10 2022

@author: tyler
"""

#Created By: Tyler Bershad
#Last Modified: 12/13/2022
#Purpose: Code that is used for experiment 1

#Experiment 1: Turn on the spa and monitor the temperature climb over time.

import asyncio #Parallelization of python to speed up API tasks
from iaqualink.client import AqualinkClient #Needed to access iAqualink Client
import re  #This will be used to remove non-relevant text
import datetime #I want to obtain timestamps
import time
import csv


pool_temp = []
air_temp = []
spa_temp = []
timestamps_unix = []
Sampling_Max = 120 #Max Datapoints
Samples = -1


f = open('output_data.csv', 'w',newline='')
writer = csv.writer(f)
header = ['Pool_Temperature','Air_Temperature','Spa_Temperature', 'Unix_Time']
writer.writerow(header)

while True:
    async def main():
            async with AqualinkClient('your username', 'your password') as c:
                s = await c.get_systems()
                #print(s) #Full System Printout
                d = await list(s.values())[0].get_devices()        
                #print(d) #Full Device Printout
                
                #Collect Unix Timestamps
                timestamps_unix.append(datetime.datetime.now().timestamp())
        
                #Grab all relevant data from the device dictionary
                
                #Obtain and clean the pool temperature
                poolGrab = d.get("pool_temp")
                poolMod_str = re.sub(r'[^0-9]', '', str(poolGrab))
                if poolMod_str != '':
                    poolMod_int = int(poolMod_str)
                    pool_temp.append(poolMod_int)
                else:
                    pool_temp.append('NAN')
                
                #Obtain and clean the air temperature            
                airGrab = d.get("air_temp")
                airMod_str = re.sub(r'[^0-9]', '', str(airGrab))
                if airMod_str != '':
                    airMod_int = int(airMod_str)
                    air_temp.append(airMod_int)
                else:
                    air_temp.append('NAN')
                
                #Obtain and clean the spa temperature in F
                spaGrab = d.get("spa_temp")
                spaMod_str = re.sub(r'[^0-9]', '', str(spaGrab))
                if spaMod_str != '':
                    spaMod_int = int(spaMod_str)
                    spa_temp.append(spaMod_int)
                else:
                    spa_temp.append('NAN')
                
                row = [pool_temp[Samples],air_temp[Samples],spa_temp[Samples],str(datetime.datetime.now().timestamp())] #Create the row as it is pulled
                print(row)
                writer.writerow(row) #Write the row to the file
            
    asyncio.run(main())
    
    #I want to capture temperature every 60 seconds + the api response time
    time.sleep(60) #Sleep in seconds. This determines the rate of data we will capture
    Samples = Samples + 1 #Index starts from 0
    print(Samples)
    
    #After 2 hours, the code should stop once executed
    if (Samples == Sampling_Max):
        print("done")
        f.close() #Close the file
        break    
    
    
