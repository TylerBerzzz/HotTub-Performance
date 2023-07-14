# HotTub-Performance
Scrape the temperature data from iAqualink controlled Hot Tub systems and plot information to determine system performance.

## Context:
This repository revolves around the need to determine the time to optimal bathing temperature of a hot tub and gain a understanding of the iAqualink system performance. For my parents, owners of the iAqualink-controlled hot tub, they were frequently uncertain when the Hot Tub was ready for use due to its long warm-up time.  

![Hot Tub](https://github.com/TylerBerzzz/HotTub-Performance/assets/30520534/e917ad76-1b11-4d63-a882-b46a0772242f)

## How the Hot Tub Works:
The Hot Tub is connected to a pool, and water circulates between the 2 when the hot tub is not in operation. This leads to a temperature equalibrium between the pool and the tub. The hot tub user has an iAqualink app, which allows them to set the Hot Tub (Spa) temperature to a certain value. Once set to the temperature value of interest, the water stops circulating between the pools and the app displays the instantaneous temperature variable as it changes over time. There is no data analytics that is offered on the app. The problem here is understanding system performance, and that's exactly why this repo exists. 

## There are 2 scripts that are within this repo: 
### 1) HotTub_DataScraper
As it's named, the purpose of this script is to scrape data from the iAqualink API and store the information into a csv file.

### 2) DataAnalyzer
This script reads the csv file and looks at performance characteristics of the graph.

## Here is a sample graph on performance from one of the experiments that I conducted. 
![Experimental_Graph](https://github.com/TylerBerzzz/HotTub-Performance/assets/30520534/811b1eaa-670c-42e3-bd86-1223fceb6d5c)

## Interpretation:
The graph shows that for each minute, the temperature increases 0.32 degrees fahrenheit and starts from the set temperature. It reaches the set temperature after > 1hr and 20 minutes, this is an area of concern for my parents. There is a high R^2, and it is quite consistent through multiple experimental trials. The flat ambient temperature line makes sense, as temperature doesn't widely fluctuate in such a short period of time. There are further explorations that can be done here in the understanding of Hot Tub heat transfer - which is the inspiration of collecting both ambient temperature and tub temperature.  

## What can be done next?
There are further explorations that can be done here in the understanding of Hot Tub heat transfer, should there be a desire to reduce the time to set temperature. 

## Existing Outcomes:
My parents will review the information with iAqualink technicians to improve the performance of the tub. In addition, they now have a better understanding of when to set the Hot Tub temperature in order to enjoy optimal use. 
