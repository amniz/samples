num=[0,1,2,3,4,5,6,7,8,9]
import random
k=set()
l=random.randint(0,10)
citer=0
count=1
while True:
    #print("inside while")
    l = random.randint(0, 10)
    for  i in num:
        if i==l:
            #for j in k:
            #print("inside ol")
            #print("j",j)
            #if j==l:
            k.add(l)
            num.remove(l)
            count+=1
            # print(l)
            # print(k)
            # print(num)

                # else:
                #     count+=1
        else:
            #print("in else")
            count+=1
    if len(num)==0:
        break
print(count)
