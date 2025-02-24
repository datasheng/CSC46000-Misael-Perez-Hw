import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url="https://www.ccny.cuny.edu/registrar/fall"

r=requests.get(url)
html_doc =r.text
soup = BeautifulSoup(html_doc, "html.parser")
#print(soup.find_all('tr'))
#shows everything within "tr". Lets try to my a dict of table three columns
#Date, Days, Information
tab= []
for tr in soup.find_all('td'):
    Old = tr.get_text()
    Old = Old.replace('\t', '')
    tab.append(Old.replace('\n', ''))
column1=[]
column2=[]   
column3=[]
index=0
for n in range(len(tab)):
    index+=1
    if index == 1:
        column1.append(tab[n])
    if index == 2:
        column2.append(tab[n])
    if index == 3:
        column3.append(tab[n])
        index= index - 3
        
for n in range(len(column1)):
    stripspace= column1[n].strip()
    if column1[n].count('-') > 0:
        continue
    elif column1[n].count(',')>0:
        column1[n]= datetime.strptime(stripspace, "%B %d, %Y").date()
    else:
        column1[n]= datetime.strptime(f"{stripspace}, 2021", "%B %d, %Y").date()

data= {
    "Date":column1,
    "Week Day":column2,
    "Description":column3
    
}

df= pd.DataFrame(data)
print(df)


