from tkiteasy import *
from pprint import pprint


plan=[]
with open("plan.txt", "r") as f:
   entete = f.readline().strip().split()
   c=int(entete[0])
   l=int(entete[1])
   
   for i in range(l):
       line=f.readline().strip()
       plan.append(line)
pprint(plan)
