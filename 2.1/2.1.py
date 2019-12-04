import math

#vstup
inFile = open("2.1.txt","r")
dataNotSplitted = inFile.read();
data = dataNotSplitted.split(",");

#prevod vstupu na int
for i in range (0, len(data)):
    data[i] = int(data[i])
    
#deklarace
index1 = 0;
index2 = 0;
index3 = 0;
hodnota1 = 0;
hodnota2 = 0;
vysledek = 0;

print(data)

for i in range (0, len(data)):
    print("i:", i, "data[i]:", data[i]);
    if(i%4 == 0):
        if(data[i] == 1):
            print("scitam")
            index1 = data[i+1];
            index2 = data[i+2];
            index3 = data[i+3];

            print("indexy:", index1, " ", index2, " ", index3)

            hodnota1 = data[index1];
            hodnota2 = data[index2];

            print("hodnoty:", hodnota1, " ", hodnota2)

            data[index3] = hodnota1 + hodnota2
        elif(data[i] == 2):
            print("nasobim")
            index1 = data[i+1];
            index2 = data[i+2];
            index3 = data[i+3];

            print("indexy:", index1, " ", index2, " ", index3)

            hodnota1 = data[index1];
            hodnota2 = data[index2];

            print("hodnoty:", hodnota1, " ", hodnota2)

            data[index3] = hodnota1 * hodnota2
        elif(data[i] == 99):
            print("HALT")
            break;
        i = i +4;

print(data);
