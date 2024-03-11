import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
start = time.time()
count = 1
header = "Brand,Model/Model Number,Price,Processor,Display Resolution,Battery Life,Camera Resolution,RAM,Storage ,Display Size"
f = open (file="MobilesFlipKart.csv", encoding="utf-8", mode="w",)
f.write(header+"\n")
url1 = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&page=1"
u = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&page=1"


ran=0
links=[]
for l in range(2,28):
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
                
        Brand = soup2.title.text.split(" ")[0]
        Model = "NA"
        Price = "NA"
        Processor = "NA"
        Resolution = "NA"
        Battery="NA"
        Camera="NA"
        Ram = "NA"
        Storage = "NA"
        ScreenSize="NA"
        for i in range(len(labels)):
            if(labels[i] == "Model Name"):
                Model = values[i].replace(',','-')
            elif(labels[i] == "Processor"):
                Processor = values[i].replace(',','-')
            elif(labels[i] == "HD Technology & Resolution" or labels[i] == "Resolution"):
                  Resolution = values[i].replace(',','-') 
            elif(labels[i] == "Battery Life" or labels[i] == "Power Consumption" or labels[i] == "Battery Capacity" ):
                  Battery = values[i].replace(',','-')
            elif(labels[i] == "Primary Camera"): 
                  Camera = values[i].replace(',','-')
            elif(labels[i] == "RAM"): 
                  Ram = values[i].replace(',','-')
            elif(labels[i] == "Storage Memory" or labels[i]=="Internal Storage"): 
                  Storage = values[i].replace(',','-')
            elif(labels[i] == "Display Size"):
                  ScreenSize = values[i].replace(',','-')
        if(soup2.find('div',class_= "_30jeq3 _16Jk6d") != None):
            Price = soup2.find('div',class_= "_30jeq3 _16Jk6d").get_text()
            Price = Price.split("₹")[1].strip()
            Price = Price.split('.')[0].strip().replace(',','')
            Price = int(Price)*3
        if(Brand != "NA" and Model != "NA"):
            row = (Brand + "," + Model + "," + str(Price) + "," + Processor+ "," + Resolution + ","   + Battery + ","   + Camera + ","  + Ram + "," + Storage + ","+ ScreenSize +"\n")
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






