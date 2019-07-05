import Linkedlist
f=open("olakka.txt",'r')
data=f.readlines()

data1=f.read()

def readw(data):
    j=[]

    for i in data:
        k=0
        c=0
        while k<len(i):
            if i[k] == '\n':
                m=i.replace('\n','')
                while c < len(m):

                    if m[c] == ' ':
                        j.append(m.split(' '))
                        break

                    c += 1
                break

            k+=1
    return j
