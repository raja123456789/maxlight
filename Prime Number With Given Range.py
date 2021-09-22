start=int(input("Enter The Number:"))
end=int(input("enter the Number:"))
if(start>end):
    start,end=end,start
elif(start==1):
    start=2
for i in range(start,end+1):
    flag=1
    for j in range(2,i):
        if(i%j==0):
            flag=0
            break
    if(flag==1):
        print(i,end=" ")