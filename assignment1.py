#Q1. Create one variable containing following type of data:
#(i) string
#(ii) list
#(iii) float
#(iv) tuple
a='coding'
print(a,type(a))
b=[1,2,'python']
print(b,type(b))
c=2.8
print(c,type(c))
d=(1,2,3,4)
print(d,type(d))

#2
var1 = ' '
var2 = '[ DS , ML , Python]'
var3 = [ 'DS' , 'ML', 'Python' ]
var4 = 1.
print(type(var1),type(var2),type(var3),type(var4))

#3
e=2
f=2
print(e/f)#it divides2 by 2
print(e%f)#it divides 2 by 2 and give the remainder 
print(e//f)#it gives the divisor
print(e**f)#it gives 2*2*2



#4
l=[1,2,3,8,9,10.5,'syed',2.0,1+2j,True]
for i in l:
    print(i ,'and its data type is', type(i))

    
#5
a=int(input())
b=int(input())
i=0
while i<1:
    if a%b == 0:
        print('a is divisible by b',a/b, 'times')
        break
    else:
        print('a is not divisible by b')
        break
        
        
        
#6
l2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
for i in l2:
    if i%3==0:
        print(i,'is divisible by 3')
    else:
        print(i , ' is not divisible by 3')
        
        
        
#7.1  immutable
a='syed'
a[0]='w'
#7.2   mutable
b=[1,'syed',2.0]
b[0]=500
