from tkiteasy import *
from pprint import pprint

plan2=[]
with open("plan.txt", "r") as f:
    entete = f.readline().strip().split()
    c=int(entete[0])
    l=int(entete[1])
    plan=[[0]*c for i in range (l)]

    for i in range(l):
        line=f.readline().strip()
        plan2.append(line)
pprint(plan2)
