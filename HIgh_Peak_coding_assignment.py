f=open('input.txt','r')

t=f.read()

l=t.split('\n')

l

dic={}

for i in l:
  k=i.split(": ")
  dic[k[0]]=int(k[1])

dic

dicimd = sorted(dic.items(),key=lambda x:x[1],reverse=True)
d=dicimd

d

#number of employees n
n=int(input("Number of employees: "))

import math
min=[math.inf,0,0]

for i in range(len(dic)-n+1):
  if (d[i][1]-d[i+n-1][1]) < min[0]:
    min[0] = d[i][1]-d[i+n-1][1]
    min[1] = i
    min[2] = i+n-1

min

st="Here the goodies that are selected for distribution are:"

for i in range(min[1],min[2]+1):
  st+="\n"+d[i][0]+ ': '+str(d[i][1])

st=st+"\nAnd the difference between the chosen goodie with highest price and the lowest price is " +str(min[0])

st

f1=open("output.txt","w")
f1.write(st)
f1.close()
f.close()