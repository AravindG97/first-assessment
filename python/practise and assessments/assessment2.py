import math
import datetime
from datetime import timedelta
country=["uk","usa","india","mexico","australia"]
time_zone=["gmt","est","ist","cst","adet"]
time=["gmt-5.5","est-10.5","ist+0.0","cst-11.5","adet+5.5"]
currency=['pound','usd','inr','usd','aud']
language=['english','english','hindi','spaanish','english']
currency_rate=['92.72','71.32','1','71.32','47.73']

def con(a):
  return float(a)

list1=map(con,currency_rate)
list1=list(list1)

def rate(a,b):
  x=country.index(a)
  print("the equivalent currency for "+str(b)+" INR : "+str("%.2f" %(b/list1[x]))+" "+str(currency[x]))


def timee(a):
  aa=country.index(a)
  x=datetime.datetime.now()
  xx=time[aa]
  if "-" in xx:
    yy=float(xx.split("-")[1])
  else:
    yy=float(xx.split("+")[1])
  i,j=math.modf(yy)
  sum=int(float((i))*60)+int(j)*60
  if "-" in xx:
    actual_time=x-timedelta(0,0,0,0,sum)
  else:
    actual_time=x+timedelta(0,0,0,0,sum)
  print("current time in india: "+str(x.strftime("%H %M"))+" IST")
  print("current time in "+str(country[aa])+": "+actual_time.strftime("%H %M")+" "+str(time_zone[aa]))

def display(a):
  dic={}
  for x in range (len (country)) :
    dic[country[x]] = {}
  aa = 0
  for x in dic :
    for i in range (len (time_zone)) :
      if i == aa :
        dic[x]["time_zone"] = time_zone[i]
        dic[x]["time"] = time[i]
        dic[x]["currency"] = currency[i]
        dic[x]["language"] = language[i]
        dic[x]["currency_rate"] = currency_rate[i]
      else :
        continue
    aa += 1
  for x,y in dic.items():
    if x==a:
      for i,j in y.items():
        print(i+" : "+str(j))


con=input("enter the country from uk,us,mexico,australia: ")
val=int(input("enter the amount: "))
display(con)
rate(con,val)
timee(con)
