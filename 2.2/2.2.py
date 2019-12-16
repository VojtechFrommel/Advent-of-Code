import math

#vstup
inFile = open("2.2.txt","r")
dataNotSplitted = inFile.read();
data = dataNotSplitted.split(",");

inFile.close();

#deklarace
index1 = 0;
index2 = 0;
index3 = 0;
hodnota1 = 0;
hodnota2 = 0;
vysledek = 0;
j = 0;
k = 0;
delka = len(data);

def vypocet(j,k):
    for i in range (0, delka):
        if(i%4 == 0 or i == 0):
            #nastaveni aktualnich hodnot
            data[1] = j;
            data[2] = k;
            if(data[i] == 1):
                index1 = data[i+1];
                index2 = data[i+2];
                index3 = data[i+3];
                hodnota1 = data[index1];
                hodnota2 = data[index2];
                data[index3] = hodnota1 + hodnota2
            elif(data[i] == 2):
                index1 = data[i+1];
                index2 = data[i+2];
                index3 = data[i+3];
                hodnota1 = data[index1];
                hodnota2 = data[index2];
                data[index3] = hodnota1 * hodnota2
            elif(data[i] == 99):
                #print("HALT")
                return data[0];
            i = i +4;

#print(data)

for j in range(70,100):
    for k in range(0,100):
        data = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 6, 19, 2, 19, 6, 23, 1, 23, 5, 27, 1, 9, 27, 31, 1, 31, 10, 35, 2, 35, 9, 39, 1, 5, 39, 43, 2, 43, 9, 47, 1, 5, 47, 51, 2, 51, 13, 55, 1, 55, 10, 59, 1, 59, 10, 63, 2, 9, 63, 67, 1, 67, 5, 71, 2, 13, 71, 75, 1, 75, 10, 79, 1, 79, 6, 83, 2, 13, 83, 87, 1, 87, 6, 91, 1, 6, 91, 95, 1, 10, 95, 99, 2, 99, 6, 103, 1, 103, 5, 107, 2, 6, 107, 111, 1, 10, 111, 115, 1, 115, 5, 119, 2, 6, 119, 123, 1, 123, 5, 127, 2, 127, 6, 131, 1, 131, 5, 135, 1, 2, 135, 139, 1, 139, 13, 0, 99, 2, 0, 14, 0]
        print("j:",j,"k:",k);
        vysledek = vypocet(j,k);

        if(vysledek == 19690720):
            print("FOKIN VYHRA")
            print("vysledek: ",vysledek);
            input();
            break;
        else: vysledek = 0;


print("vysledek: ",vysledek);
