#Vojtìch Frömmel
#2019

inFile = open("3.1.txt","r");
rawData = inFile.readlines();
inFile.close();

firstWire = rawData[0].split(",");
secondWire = rawData[1].split(",");
usedCoordsFirst = [];
usedCoordsSecond = [];
direction = "";
hm = [];
howmuch = 0;

#right, left, up, down (max)
mr1 = 0;
ml1 = 0;
mu1 = 0;
md1 = 0;

mr2 = 0;
ml2 = 0;
mu2 = 0;
md2 = 0;

x = 0;
y = 0;


for i in range (0, len(firstWire)):
    direction = firstWire[i][0];
    
    if(direction == "R"):
        hm = firstWire[i].split("R");
        hm.remove(hm[0]);
        howmuch = int(hm[0]);
        #print(howmuch);
        for j in range(howmuch):
            usedCoordsFirst.append([x,y]);
            x += 1;
        if(x>0 and x>mr1):
            mr1 = x;
    elif(direction == "U"):
        hm = firstWire[i].split("U");
        hm.remove(hm[0]);
        howmuch = int(hm[0]);
        #print(howmuch);
        for j in range(howmuch):
            usedCoordsFirst.append([x,y]);
            y += 1;
        if(y>0 and y>mu1):
            mu1 = y;
    elif(direction == "L"):
        hm = firstWire[i].split("L");
        hm.remove(hm[0]);
        howmuch = int(hm[0]);
        #print(howmuch);
        for j in range(howmuch):
            usedCoordsFirst.append([x,y]);
            x -= 1;
        if(x<0 and x<ml1):
            ml1 = x;
    elif(direction == "D"):
        hm = firstWire[i].split("D");
        hm.remove(hm[0]);
        howmuch = int(hm[0]);
        #print(howmuch);
        for j in range(howmuch):
            usedCoordsFirst.append([x,y]);
            y -= 1;
        if(y<0 and y<md1):
            md1 = y;
#reset values
x=0;
y=0;


for i in range (0, len(secondWire)):
    direction = secondWire[i][0];
    
    if(direction == "R"):
        hm = secondWire[i].split("R");
        hm.remove(hm[0]);
        howmuch = int(hm[0]);
        #print(howmuch);
        for j in range(howmuch):
            usedCoordsSecond.append([x,y]);
            x += 1;
        if(x>0 and x>mr2):
            mr2 = x;
    elif(direction == "U"):
        hm = secondWire[i].split("U");
        hm.remove(hm[0]);
        howmuch = int(hm[0]);
        #print(howmuch);
        for j in range(howmuch):
            usedCoordsSecond.append([x,y]);
            y += 1;
        if(y>0 and y>mu2):
            mu2 = y;
    elif(direction == "L"):
        hm = secondWire[i].split("L");
        hm.remove(hm[0]);
        howmuch = int(hm[0]);
        #print(howmuch);
        for j in range(howmuch):
            usedCoordsSecond.append([x,y]);
            x -= 1;
        if(x<0 and x<ml2):
            ml2 = x;
    elif(direction == "D"):
        hm = secondWire[i].split("D");
        hm.remove(hm[0]);
        howmuch = int(hm[0]);
        #print(howmuch);
        for j in range(howmuch):
            usedCoordsSecond.append([x,y]);
            y -= 1;
        if(y<0 and y<md2):
            md2 = y;
print("BEFORE: ","-y: ",md1,"y: ",mu1,"-x: ",ml1,"x:",mr1);
print("BEFORE: ","-y: ",md2,"y: ",mu2,"-x: ",ml2,"x:",mr2);
print("length before 1: " + str(len(usedCoordsFirst)));
print("length before 2: " + str(len(usedCoordsSecond)));
print("length before both: " + str(len(usedCoordsSecond)+len(usedCoordsFirst)));

if(md1 < md2): md1=md2;
if(mu1 > mu2): mu1=mu2;
if(ml1 < ml2): ml1=ml2;
if(mr1 > mr2): mr1=mr2;

print("AFTER: ","-y: ",md1,"y: ",mu1,"-x: ",ml1,"x:",mr1);

usedCoordsFirst = filter(lambda x: x[0]<=mr1, usedCoordsFirst);
usedCoordsFirst = filter(lambda x: x[0]>=ml1, usedCoordsFirst);
usedCoordsFirst = filter(lambda y: y[1]<=mu1, usedCoordsFirst);
usedCoordsFirst = filter(lambda y: y[1]>=md1, usedCoordsFirst);
usedCoordsFirst = list(usedCoordsFirst);
usedCoordsSecond = filter(lambda x: x[0]<=mr1, usedCoordsSecond);
usedCoordsSecond = filter(lambda x: x[0]>=ml1, usedCoordsSecond);
usedCoordsSecond = filter(lambda y: y[1]<=mu1, usedCoordsSecond);
usedCoordsSecond = filter(lambda y: y[1]>=md1, usedCoordsSecond);
usedCoordsSecond = list(usedCoordsSecond);
print("length after 1: " + str(len(usedCoordsFirst)));
print("length after 2: " + str(len(usedCoordsSecond)));
print("length after both: " + str(len(usedCoordsSecond)+len(usedCoordsFirst)));
#print(usedCoords);

qq = tuple(usedCoordsFirst);
ww = tuple(usedCoordsSecond);
#výpocet shod
matches = [];
for i in range(len(qq)):
    if(i%10 == 0):print(i);
    for j in range(len(ww)):
        if(qq[i] == [0,0]):
            continue;
        if(qq[i][0] == ww[j][0] and qq[i][1] == ww[j][1]):
            matches.append(qq[i]);

print(len(matches));
#print(matches);

#výpocet vzdálenosti
result = 0;
lowestResult = 1000000;

for i in range(len(matches)):
    if(matches[i][0] < 0):
        matches[i][0] = matches[i][0] * (-1);
    if(matches[i][1] < 0):
        matches[i][1] = matches[i][1] * (-1);
    result = matches[i][0] + matches[i][1];
    if(result < lowestResult):
        lowestResult = result;

print(lowestResult);
