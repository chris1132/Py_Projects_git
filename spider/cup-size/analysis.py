

import csv
import re

def opencsv():
    list=[]
    A,B,C,D,E=0,0,0,0,0
    s=set()
    with open('data/cup_all.csv',"r",encoding="utf-8") as f:
        fin_csv = csv.reader(f)
        for row in fin_csv:
            if len(tuple(row))!=0:
                pa='(.*)尺码:(.*)([A-Z])'
                rema=re.match(pa,tuple(row)[1], re.M|re.I)
                if rema:
                    cup_size=str(rema.group(3))
                    if cup_size=="A":
                        A+=1
                    if cup_size=="B":
                        B+=1
                    if cup_size=="C":
                        C+=1
                    if cup_size=="D":
                        D+=1
                    elif cup_size=="E":
                        E+=1

    print("A:",A)
    print("B:",B)
    print("C:",C)
    print("D:",D)
    print("E:",E)

if __name__=="__main__":
    opencsv()