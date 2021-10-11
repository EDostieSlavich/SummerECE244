#provides system specifics
import sys

#needed to make web requests
import requests

#store the data we get as a dataframe
import pandas as pd

#convert the response as a strcuctured json
import json

#mathematical operations on lists

import numpy as np

#parse the datetimes we get from NOAA
from datetime import datetime

#add the access token you got from NOAA
Token = 'QbUfrFiAhMCQJpobnyrIDvnbDycnanjZ'

#Long Beach Airport station
station_id = 'GHCND:USW00023129'

# Amherst Station
# station_id = 'GHCND:USC00190120'


# initialize lists to store data
dates_temp = []
dates_prcp = []

class QuestionThree(object):

    def highest_temp(self, alist):
        i = 0
        maximum = alist[0]
        k = 0
        while i + 1 < len(alist):
            if alist[i] >= alist[i + 1]:
                i = i + 1
            else:
                if alist[i + 1] > maximum:
                    maximum = alist[i + 1]
                    k = i + 1
                else:
                    i = i + 1
        return maximum, k

    def lowest_temp(self, alist):
        i = 0
        minimum = alist[0]
        k = 0
        while i + 1 < len(alist):
            if alist[i] <= alist[i + 1]:
                i = i + 1
            else:
                if alist[i + 1] < minimum:
                    minimum = alist[i + 1]
                    k = i + 1
                else:
                    i = i + 1

        return minimum, k

    def average_high(self, alist):
        sum = 0
        i = 0
        length = len(alist)
        for i in range(length):
            sum += alist[i]
        avgHigh = sum/length
        avgHigh = "{:.2f}".format(avgHigh)
        return avgHigh

    def average_low(self, alist):
        sum = 0
        i = 0
        length = len(alist)
        for i in range(length):
            sum += alist[i]
        avgLow = sum/length
        avgLow = "{:.2f}".format(avgLow)
        return avgLow

# DO NOT MODIFY  THE CODE BELOW!!!!!!
def GetTemps(startyear, endyear, type):
    dates_temp = []
    tempsmax = []
    tempsmin = []
    for year in range(startyear, endyear):
        year = str(year)
        print('working on year ' + year)
        for type in type:
            print('working on Type:' + type)
            # make the api call
            r = requests.get(
                'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=' + type + '&limit=1000&stationid=GHCND:USC00190120&startdate=' + year + '-01-01&enddate=' + year + '-12-31',
                # 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=PRECIP_15&stationid=COOP:010008&units=metric&startdate=2010-05-01&enddate=2010-05-31',
                headers={'token': Token})
            # load the api response as a json
            d = json.loads(r.text)
            print(d)
            if type == 'TMAX':
                # get all items in the response which are average temperature readings
                max_temps = [item for item in d['results'] if item['datatype'] == 'TMAX']
                # get the date field from all average temperature readings
                dates_temp += [item['date'] for item in max_temps]
                # get the actual average temperature from all average temperature readings
                tempsmax += [item['value'] for item in max_temps]
                print(tempsmax)
            elif type == 'TMIN':
                # get all items in the response which are average temperature readings
                min_temps = [item for item in d['results'] if item['datatype'] == 'TMIN']
                # get the date field from all average temperature readings
                dates_temp += [item['date'] for item in min_temps]
                # get the actual average temperature from all average temperature readings
                tempsmin += [item['value'] for item in min_temps]
                print(tempsmin)
            else:
                print('Datatype not supported!!!')
    return tempsmax, tempsmin, dates_temp

maxTemps, minTemps, datesTemp = GetTemps(2010,2011,['TMAX', 'TMIN'])

statistics = QuestionThree()
max, maxindex = statistics.highest_temp(maxTemps)
min, minindex = statistics.lowest_temp(minTemps)
print('Max:', max , maxindex, ' Min:', min, minindex)
avg_max = statistics.average_high(maxTemps)
avg_min = statistics.average_low(minTemps)
print("Average high: ", avg_max, " Average low:", avg_min)

#initialize dataframe
df_temp = pd.DataFrame()

#populate date and average temperature fields (cast string date to datetime and convert temperature from tenths of Celsius to Fahrenheit)
df_temp['date'] = [datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in dates_temp]
df_temp['avgTemp'] = [float(v)/10.0*1.8 + 32 for v in maxTemps]
