def Merge(a,b,arr):
    print("in merge")
    print("input for merge a",a)
    print("input for merge b",b)
    i=0
    j=0
    count=0
    while i<len(a) and j<len(b):
        print(len(a),"len a")
        print("len b",len(b))
        if a[i]<b[j]:
            arr.insert(count,a[i])
            i+=1
            count+=1
        else:
            arr.insert(count,b[j])
            j+=1
            count+=1
    #while i<len(a):
        #arr.insert(count,a[i])
        #i+=1
        #count+=1
    #while j<len(b):
        #arr.insert(count,b[j])
        #count+=1
        #j+=1

def Sort(arr):
    l=0
    h=len(arr)
    mid=(l+h)/2
    a=[]
    b=[]
    if h-1>l:
        i=l
        while i<mid:
            #print("inside first")
            a.append(arr[i])
            i+=1
        j=0
        while i<h:
            #print("inside second")
            #print(i)
            b.append(arr[i]) 
            i+=1
            j+=1
        print(a)
        print(b)
        Sort(a)
        Sort(b)
        Merge(a,b,arr)
    else:
         return
arr=[2,1,3,5,4]
Sort(arr)
print(arr)






