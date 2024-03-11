# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:41:22 2022

@author: RAJPOOT
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
start = time.time()
count = 1
header = "Brand,Model,Price,Processor,Screen Resolution,RAM,SSD Capacity,Screen Size"
f = open (file="DellLaptop.csv", encoding="utf-8", mode="a",)
# f.write(header+"\n")
# for i in range(1,40):
for l in range(1,42):
    
    url1 = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=dell+laptop&_sacat=0&LH_TitleDesc=0&_ipg=240&_pgn=" +str(l)
    r = requests.get(url1)
    htmlContent = r.text
    
    soup = BeautifulSoup(htmlContent, "html.parser")
    links=[]
    allLaptop = soup.find_all('a',class_= "s-item__link")
    
    
    
    for d in allLaptop:
        st=str(d)
        x=st.split('href="')
        y=x[1].split('"')
        links.append(y[0])
        
    
    for k in range(1,len(links)-1):
        url2 = links[k]
        r = requests.get(url2)
        htmlContent = r.text
        soup2 = BeautifulSoup(htmlContent, "html.parser")
        
        labels = []
        values = []
        allAttributes = soup2.find_all('div',class_= "ux-layout-section__item ux-layout-section__item--table-view")
        
        for tag in allAttributes:
            value = tag.find_all('div', class_="ux-labels-values__values")
            label = tag.find_all('div', class_="ux-labels-values__labels")
            
            for a in range(len(label)):
                labels.append(label[a].get_text())
                values.append(value[a].get_text())
        Model = ""
        Brand = ""
        Processor = "N/A"
        Resolution = "N/A"
        Ram = "N/A"
        Storage = "N/A"
        Price = "N/A"
        battery = "N/A"
        CameraResolution = "N/A"
        ScreenSize = "N/A"
        for i in range(len(labels)):
            if(labels[i] == "Model:"):
                Model = values[i].replace(',','-')
            elif(labels[i] == "Brand:"):
                Brand = values[i].replace(',','-')
            elif(labels[i] == "Processor:"):
                Processor = values[i].replace(',','-')
            elif(labels[i] == "Resolution:" or labels[i] == "Maximum Resolution:"):
                 Resolution = values[i].replace(',','-') 
            elif(labels[i] == "Camera Resolution:"):
                CameraResolution = values[i].replace(',','-') 
            elif(labels[i] == "RAM:" or labels[i] == "RAM Size:" ):
                 Ram = values[i].replace(',','-')
            elif(labels[i] == "Screen Size:"):
                 ScreenSize = values[i].replace(',','-')
            elif(labels[i] == "SSD Capacity:" or labels[i] == "Storage Capacity:" or labels[i] == "	Hard Drive Capacity:"): 
                 Storage = values[i].replace(',','-')
            elif(labels[i] == "BATTERY:"): 
                 battery = values[i].replace(',','-')
        if(soup2.find('div',class_= "mainPrice") != None):
            Price = soup2.find('div',class_= "mainPrice").get_text()
            Price = Price.split("$")[1].strip()
            Price = Price.split('.')[0].strip().replace(',','')
            Price = int(Price)*218 
        elif(soup2.find('div',class_= "notranslate u-cb vi-bidConvPrc2 convPrice") != None):
            Price = soup2.find('div',class_= "notranslate u-cb vi-bidConvPrc2 convPrice").get_text()
            Price = Price.split("$")[1].strip()
            Price = Price.split('.')[0].strip().replace(',','')
            Price = int(Price)*218 
            
        if(Brand != "" and Model != ""):
            row = (Brand + "," + Model + "," + str(Price) + "," + Processor+ "," + Resolution + "," + battery + "," + CameraResolution + ","  + Ram + "," + Storage + ","+ ScreenSize +"\n")
            print("page = "+ str(l) + " "+ str(count) + " " + row)
            f.write(row)
            f.flush()
            count = count + 1
        # print(count,  " " , Brand + "," + Model + "," + str(Price) + "," + Processor+ "," + Resolution + ","  + Ram + "," + Storage + ","+ ScreenSize +"\n")   
    
end = time.time()
print(end-start) 
# processor = allAttributes.split("Resolution:")
# print(processor)    





