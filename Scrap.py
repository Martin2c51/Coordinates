"""
Created on Mon Jul 15 17:22:39 2019

@author: Martin Martin del campo Benito
"""

import time
import threading
import Coordinates
import pandas as pd
import ACSV

output = "C:/Users/Path/to/your/root.csv"
inputs = "C:/Users/Path/to/your/input.xlsx"

AllCoords = []
AllAddress = []
AllNums = []

def getCoords(direccs, numbers):
    coords = Coordinates.Coordinates(direccs)
    for x in range(len(coords)):
        AllCoords.append(coords[x])
        AllAddress.append(direccs[x])
        AllNums.append(numbers[x])
    ACSV.a_csv([x.split("\n")[2] if "Check" not in x else x for x in AllCoords ], AllNums, output)

   
  


# Read the excel sheet to pandas dataframe
df = pd.read_excel(inputs)

List_Of_List_Address = []
List_Address = []
List_Of_List_Nums = []
List_Nums = []

r = (len(df["ID"])//25)
d = (len(df["ID"])%25)
for x in range(r+1):
    if x==r:
        ini = 0 + (25 * x)
        fin = ini + d
    else:
        ini = 0 + (25 * x)
        fin = ini + 24
    print(str(ini) + "     " + str(fin))
    cont = 0
    for index, row in df.iterrows():
        cont+= 1
        if(cont >= ini and cont <= fin):
            List_Address.append(str(row['DIRECCION']) + ", Uruguay")
            List_Nums.append(str(row['ID']))
    List_Of_List_Address.append(List_Address)
    List_Of_List_Nums.append(List_Nums)
    
    List_Address = [] 
    List_Nums = []

print(len(List_Of_List_Address))


t = time.time()


tarr = []
for x in range(len(List_Of_List_Address)):
    tx = threading.Thread(target=getCoords, args=(List_Of_List_Address[x], List_Of_List_Nums[x],))
    tarr.append(tx)



for x in tarr :
  x.start();

for x in tarr :
  x.join();



dt = time.time()-t
time.sleep(0.1)
print("done in : ", dt//60 , ":", dt%60)