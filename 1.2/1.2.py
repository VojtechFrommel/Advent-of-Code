#Made by: Vojtech Frömmel
#Advent od Code 2019

import math;

data = [];

inFile = open("1.2.txt","r")
indata = inFile.readlines();
inFile.close();

result = 0;
summary = 0;

def rekVypocet(res):
    x = math.floor(res/3) - 2;
    if x <= 0: x=0;
    return x;

for i in range (0,len(indata)):
    result = math.floor(int(indata[i])/3) - 2;
    summary += result;
    while result > 0:
        result = rekVypocet(result);
        summary += result;

print("výsledek: ", summary);
