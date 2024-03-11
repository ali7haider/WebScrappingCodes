# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 22:28:45 2022

@author: Digital Zone
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
f = open (file="LaptopFlipKartScrap.csv", encoding="utf-8", mode="w",)
f.write(header+"\n")
url1 = "https://www.flipkart.com/search?q=laptop&otracker=AS_Query_HistoryAutoSuggest_2_0&otracker1=AS_Query_HistoryAutoSuggest_2_0&marketplace=FLIPKART&as-show=off&as=off&as-pos=2&as-type=HISTORY&"
u = "https://www.flipkart.com/search?q=laptop&otracker=AS_Query_HistoryAutoSuggest_2_0&otracker1=AS_Query_HistoryAutoSuggest_2_0&marketplace=FLIPKART&as-show=off&as=off&as-pos=2&as-type=HISTORY&"



links=[]
for l in range(2,40):
    print(url1)
    r = requests.get(url1)
    htmlContent = r.text
    soup = BeautifulSoup(htmlContent, "lxml")
    allLaptop = soup.find_all('a',class_= "_1fQZEK")
    
    
    for d in allLaptop:
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
        for i in range(len(labels)):
            if(labels[i] == "Model Name"):
                Model = values[i].replace(',','-')
            elif(labels[i] == "Series"):
                Brand = values[i].replace(',','-')
            elif(labels[i] == "Processor Name"):
                Processor = values[i].replace(',','-')
            elif(labels[i] == "Screen Resolution"):
                  Resolution = values[i].replace(',','-') 
            elif(labels[i] == "RAM"):
                  Ram = values[i].replace(',','-')
            elif(labels[i] == "Screen Size"):
                  ScreenSize = values[i].replace(',','-')
            elif(labels[i] == "SSD Capacity"): 
                  Storage = values[i].replace(',','-')
        if(soup2.find('div',class_= "_30jeq3 _16Jk6d") != None):
            Price = soup2.find('div',class_= "_30jeq3 _16Jk6d").get_text()
            Price = Price.split("₹")[1].strip()
            Price = Price.split('.')[0].strip().replace(',','')
            Price = int(Price)*3
        if(Brand != "" and Model != ""):
            row = (Brand + "," + Model + "," + str(Price) + "," + Processor+ "," + Resolution + ","  + Ram + "," + Storage + ","+ ScreenSize +"\n")
            print(row)
            f.write(row)
            f.flush()
    
            count = count + 1
    url1=u
    url1=url1+"page="+str(l)
    end = time.time()
    print(end-start) 






