#1
s=int(input())
h=s//3600
m=(s%3600)//60
s=s%60
print(h,m,s)

#2
a,b,h=map(float,input().split())
S=(a+b)*h/2
V=h/3*(a+b+(a*b)**0.5)
print(S,V)

#3
m1,m2,m3=map(float,input().split())
x1,y1=map(float,input().split())
x2,y2=map(float,input().split())
x3,y3=map(float,input().split())
M=m1+m2+m3
x=(m1*x1+m2*x2+m3*x3)/M
y=(m1*y1+m2*y2+m3*y3)/M
print(x,y)

#4
import math
R=float(input())
V=4*math.pi*R**3/3
S=math.pi*R**2
print(V,S)
print(V/S)

#5
import math
a,b,c=map(float,input().split())
ma=0.5*math.sqrt(2*b**2+2*c**2-a**2)
mb=0.5*math.sqrt(2*a**2+2*c**2-b**2)
mc=0.5*math.sqrt(2*a**2+2*b**2-c**2)
print(ma,mb,mc)

#6
import math
r,h=map(float,input().split())
l=math.sqrt(r**2+h**2)
S=math.pi*r*(r+l)
V=math.pi*r**2*h/3
print(S,V)

#7
import math
r=float(input())
V=4*math.pi*r**3/3
S=4*math.pi*r**2
print(f"{V:.3f}")
print(f"{S:.3f}")

#8
x=int(input())
print(oct(x)[2:])

#9
import math
x1,y1=map(float,input().split())
x2,y2=map(float,input().split())
d=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(d)

#10
a = int(input())
b = int(input())

max = (a+b + abs(a - b)) // 2

print(max)

#11
a,b=map(int,input().split())
a=a+b
b=a-b
a=a-b
print(a,b)

#12
a,b,c=map(int,input().split())
print(f"{(a+b+c)/3:.2f}")

#13
a,b,c=map(float,input().split())
discount=(a+b+c)*0.13
print(f"{discount:.1f}")

#14
a=list(map(float,input().split()))
print(sum(a))

#15
n=int(input())
a=n//100
b=n//10%10
c=n%10
print(a+b+c)

#16
import math
a,b=map(float,input().split())
c=math.sqrt(a**2+b**2)
print(f"{c:.5f}")

#17
name_max=""
price_max=0
for _ in range(5):
    name,price=input().split()
    price=float(price)
    if price>price_max:
        price_max=price
        name_max=name
print(name_max)

#18
max_name=""
max_expense=0
total=0
total_count=0
for _ in range(4):
    name,count,expense=input().split()
    count=float(count)
    expense=float(expense)
    if expense>max_expense:
        max_expense=expense
        max_name=name
    total+=expense
    total_count+=count
print(max_name)
print(total/total_count)
