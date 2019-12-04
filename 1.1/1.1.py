#Made by: Vojtech Frömmel
#Advent od Code 2019

import math;

data = [];

inFile = open("1.1.txt","r")
indata = inFile.readlines();
result = 0;
summary = 0;

for i in range (0,len(indata)):
    xdata = int(indata[i]);
    result =math.floor(xdata/3) - 2;
    summary += result;
    print(result)

print("výsledek: ", summary);

inFile.close();
