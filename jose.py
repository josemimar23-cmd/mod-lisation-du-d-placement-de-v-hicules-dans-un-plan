from tkiteasy import *
from pprint import pprint

plan=[[0]*40 for i in range (15)]
plan2=[]
with open("plan.txt", "r") as f:
    for line in f:
        line=line.strip()
        plan2.append(line)
pprint(plan2)