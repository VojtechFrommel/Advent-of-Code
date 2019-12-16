#zapisovat obsazené pozice a porovnávat shodu -> jak je daleko -> je to menší vzdálenost, než ta poslední?
#Vojtìch Frömmel
#2019

#Špatný solution -> pøíliž nárocné

inFile = open("test.txt","r");
rawData = inFile.readlines();
firstWire = rawData[0].split(",");
secondWire = rawData[1].split(",");

#print(firstWire);
#print(secondWire);

inFile.close();

curCoords = [0,0]; #x,y
usedCoords = [];

direction = "";
hm = [];
howmuch = 0;

#right, left, up, down
x = 0;
y = 0;


for i in range (0, len(firstWire)):
    direction = firstWire[i][0];
    
    if(direction == "R"):
        hm = firstWire[i].split("R");
        hm.remove(hm[0]);
        howmuch = int(hm[0]);
        #print(howmuch);
        for j in range(howmuch+1):
            usedCoords.append([x,y]);
            x += 1;
    elif(direction == "U"):
        hm = firstWire[i].split("U");
        hm.remove(hm[0]);
        howmuch = int(hm[0]);
        #print(howmuch);
        for j in range(howmuch+1):
            usedCoords.append([x,y]);
            y += 1;
    elif(direction == "L"):
        hm = firstWire[i].split("L");
        hm.remove(hm[0]);
        howmuch = int(hm[0]);
        #print(howmuch);
        for j in range(howmuch+1):
            usedCoords.append([x,y]);
            x -= 1;
    elif(direction == "D"):
        hm = firstWire[i].split("D");
        hm.remove(hm[0]);
        howmuch = int(hm[0]);
        #print(howmuch);
        for j in range(howmuch+1):
            usedCoords.append([x,y]);
            y -= 1;
print(usedCoords);

for i in range (0, len(secondWire)):
    print("i: ",i)
    direction = secondWire[i][0];

    print(direction);
    
    if(direction == "R"):
        hm = secondWire[i].split("R");
        hm.remove(hm[0]);
        howmuch = int(hm[0]);
        #print(howmuch);
        for j in range(howmuch+1):
            print("j:",j);
            for k in range(len(usedCoords)):
                if(x == usedCoords[k][0] and y == usedCoords[k][1]):
                    print("SHODA")
                    #shoda -> spoèítej vzdálenost
                else:
                    usedCoords.append([x,y]);
            x += 1;
    elif(direction == "U"):
        hm = secondWire[i].split("U");
        hm.remove(hm[0]);
        howmuch = int(hm[0]);
        #print(howmuch);
        for j in range(howmuch+1):
            print("j:",j);
            for k in range(len(usedCoords)):
                if(x == usedCoords[k][0] and y == usedCoords[k][1]):
                    print("SHODA")
                    #shoda -> spoèítej vzdálenost
                else:
                    usedCoords.append([x,y]);
            y += 1;
    elif(direction == "L"):
        hm = secondWire[i].split("L");
        hm.remove(hm[0]);
        howmuch = int(hm[0]);
        #print(howmuch);
        for j in range(howmuch+1):
            for k in range(len(usedCoords)):
                if(x == usedCoords[k][0] and y == usedCoords[k][1]):
                    print("SHODA")
                    #shoda -> spoèítej vzdálenost
                else:
                    usedCoords.append([x,y]);
            x -= 1;
    elif(direction == "D"):
        hm = secondWire[i].split("D");
        hm.remove(hm[0]);
        howmuch = int(hm[0]);
        #print(howmuch);
        for j in range(howmuch+1):
            for k in range(len(usedCoords)):
                if(x == usedCoords[k][0] and y == usedCoords[k][1]):
                    print("SHODA")
                    #shoda -> spoèítej vzdálenost
                else:
                    usedCoords.append([x,y]);
            y -= 1;
print(usedCoords);
    
