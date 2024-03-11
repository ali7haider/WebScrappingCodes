# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 00:19:45 2022

@author: Digital Zone
"""

# -*- coding: utf-8 -*-
"""
"""

# -*- coding: utf-8 -*-
"""
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
start = time.time()
count = 1
header = "Brand,Model,Price,Processor,Screen Resolution,RAM,SSD Capacity,Screen Size"
f = open (file="CameraFlipKartScrap2.csv", encoding="utf-8", mode="w",)
f.write(header+"\n")
url1 = "https://www.flipkart.com/cameras/pr?sid=jek%2Cp31&otracker=categorytreepage%3D3&page=1"
u = "https://www.flipkart.com/cameras/pr?sid=jek%2Cp31&otracker=categorytreepage%3D3&page=1"


ran=0
links=[]
for l in range(2,41):
    print(url1)
    r = requests.get(url1)
    htmlContent = r.text
    soup = BeautifulSoup(htmlContent, "lxml")
    allLaptop = soup.find_all('a',class_= "_1fQZEK")
    
    for k in range(0,len(allLaptop)):
        d=allLaptop[k]
        st=str(d)
        x=st.split('href="')
        y=x[1].split('"')
        z="https://www.flipkart.com"+ y[0]
        links.append(z)
    for k in range(1,len(links)-1):
        url2 = links[k]
        r = requests.get(url2)
        htmlContent = r.text
        soup2 = BeautifulSoup(htmlContent, "html.parser")
        
        labels = []
        values = []
        allAttributes = soup2.find_all('div',class_= "_3k-BhJ")
        for tag in allAttributes:
            label = tag.find_all('td', class_="_1hKmbr col col-3-12")
            value = tag.find_all('li', class_="_21lJbe")
            
            for a in range(len(label)):
                labels.append(label[a].get_text())           
                values.append(value[a].get_text())
                
        Model = ""
        Brand = ""
        Processor = ""
        Resolution = ""
        Ram = ""
        Storage = ""
        Price = ""
        ScreenSize=""
        for i in range(len(labels)):
            if(labels[i] == "Brand"):
                Brand = values[i].replace(',','-')
            elif(labels[i] == "Model Name"):
                Model = values[i].replace(',','-')
            elif(labels[i] == "Shutter Speed"):
                Processor = values[i].replace(',','-')
            elif(labels[i] == "Video Resolution"):
                  Resolution = values[i].replace(',','-') 
            elif(labels[i] == "Battery Type"):
                  Ram = values[i].replace(',','-')
            elif(labels[i] == "Compatible Card"): 
                  Storage = values[i].replace(',','-')
            elif(labels[i] == "Image Sensor Size"):
                  ScreenSize = values[i].replace(',','-')
        if(soup2.find('div',class_= "_30jeq3 _16Jk6d") != None):
            Price = soup2.find('div',class_= "_30jeq3 _16Jk6d").get_text()
            Price = Price.split("₹")[1].strip()
            Price = Price.split('.')[0].strip().replace(',','')
            Price = int(Price)*3
        if(Brand != "" and Model != ""):
            row = (Brand + "," + Model + "," + str(Price) + "," + Processor+ "," + Resolution + ","  + Ram + "," + Storage + ","+ ScreenSize +"\n")
            print(count," ",row)
            f.write(row)
            f.flush()
            count = count + 1
    labels.clear()
    values.clear()
    links.clear()
    url1=u
    p="page="+str(l)
    url1=url1.replace('page=1',p)
    end = time.time()
    print("End Time : ",end-start) 






