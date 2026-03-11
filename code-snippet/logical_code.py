x=[1,2,3,4]
y=x
y[2]=20
print(x)
#output:[1,2,20,4]

x=[1,2,3,True]
y=x.pop(True)
print(y)
#output:2

n=int("5")
if n%2:
    print("odd")
else:
    print("even")    
#output:odd

x=True+True*False*False
y=x
print(y*y)
#output:1

x={1,2,3,4,5}
y={8,9,2,3,4}
a=x-y
print(a)
#output:{1,5}


cart=("shoes","id","rollno")
a,b,c=cart
print(b)
#output:id

a="178"
b="45"
c="871"
d="54" 
if a==c[::-1]:
    if b==d[::-1]:
        print("False")
    else:
        print("True")
else:
    print("error")            
#output:False

x=int("11",2)
print(x)
#output:3

a="10"
b="2" 
c=a>b
print(c)
#output:False

a=[1,2,3]
b=(7,a)
a.append(4)
print(b)
#output:(7[1,2,3])

x="python"
y=x*2
print(y[1:5])
#output:ytho

nums=[5,10,15,20]
a=True
b=False
c=a+b+a
print(nums[c])
#output:15





