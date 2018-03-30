def hypotenuse(opp,adj):
  temp1=opp**2
  temp2=adj**2
  sum=temp1+temp2
  thr=math.sqrt(sum)
  return thr

import math



opp=input("Enter the opposite side value\n")
adj=input("Enter the adjacent side value\n")
result=hypotenuse(opp,adj)
print result
