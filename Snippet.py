#Sam Johnston
#2019

import time
import datetime
import requests
import csv
from bs4 import BeautifulSoup

def record_data(time_steps):

    starttime = datetime.datetime.now()

    usageFile = ## Add file path to usage file csv
    dataFile = ## Add file path to data file csv

    url = 'http://127.0.0.1' ## Add wireless access point address, localhost used as example ONLY
    count = 0
    time_count = 0

    with open(usageFile, 'r+') as csvUsageFile:
        writer = csv.writer(csvUsageFile)
        reader = csv.reader(csvUsageFile)
        for row in reader:
            break
        if row == ["Start_time", "End_time"]:
            pass
        else:    
            writer.writerow(["Start_time", "End_time"])
        
    with open(dataFile, 'w',1) as file:
        file.truncate()

    with open(dataFile, 'w',1) as file:
        writer = csv.writer(file)
        writer.writerow(["Time_Stamps", "aX", "aY","aZ","gX","gY","gZ","Temp"])

        
    while True:

        try:
            r = requests.get(url, timeout=0.5)
        except requests.exceptions.Timeout:
            with open(usageFile, 'a') as csvUsageFile:
                writer = csv.writer(csvUsageFile)
                if count == 0:
                    writer.writerow([starttime,datetime.datetime.now()])
                    count = count + 1
            time.sleep(0.05)
        else:
            with open(dataFile, 'a') as file:
                writer = csv.writer(file)
            
                page = requests.get(url)
                pageSoup = BeautifulSoup(page.text, 'html.parser')

                dataTags = pageSoup.find_all('p')
                dtText = [x.text for x in dataTags]
                dtText.insert(0,datetime.datetime.now())

                writer.writerow([dtText[0],dtText[1],dtText[2],dtText[3],dtText[4],dtText[5],dtText[6],dtText[7]])

                time.sleep(0.05)

                time_count += 1

                if time_count == time_steps+1:
                    break
    return    
