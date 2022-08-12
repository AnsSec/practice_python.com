num=int(input("Enter A Number:"))
diclist=[]
x= list(range(1,num+1))
for i in x:
    if num%i==0:
        diclist.append(i)
print(diclist)
