import random
li=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
n=9
print("id of li in normal",id(li))
def disp(li):
    print("id of li in disp",id(li))
    for i in range(0,len(li)):
        j=0
        while j<3:
            print(li[i][j],"|",end='')
            j+=1
        print()
def check(l,n):
    print("id of l in check",id(l))
    hum=0
    comp=0
    for i in range(3):
        for j in range (1):
            if l[i][j]=='x' and l[i][j+1]=='x' and l[i][j+2]=='x':
                hum+=1
    for i in range(3):
        for j in range (1):
            if l[i][j]=='o' and l[i][j+1]=='o' and l[i][j+2]=='o':
                comp+=1
    for i in range(1):
        for j in range (3):
            if l[i][j]=='x' and l[i+1][j]=='x' and l[i+2][j]=='x':
                hum+=1
    for i in range(1):
        for j in range (3):
            if l[i][j]=='o' and l[i+1][j]=='o' and l[i+2][j]=='o':
                comp+=1
    if l[0][0]=='x' and l[1][1]=='x' and l[2][2] =='x' or l[0][2]=='x' and l[1][1]=='x' and l[2][1]=='x':
        hum+=1
    if l[0][0]=='o' and l[1][1]=='o' and l[2][2] =='o' or l[0][2]=='o' and l[1][1]=='o' and l[2][1]=='o':
        hum+=1
    if comp or hum==1 and n<3:
        if hum>comp:
            print("human wins")
        elif comp>hum:
            print("comp wins")
        else:
            print("match draw")
            exit()
    
            
while n>0:
    if n%2!=0:
        row=int(input("enter the value row"))
        col=int(input("enter the value of col"))
        if li[row][col]==' ':
            print("hum sel",row," ",col)
            li[row][col]='x'
            n-=1
            disp(li)
            check(li,n)
        else:
            print("its already selected enter another one")
    else:
        row=random.randint(0,2)
        col=random.randint(0,2)
        if li[row][col]==' ':
            print("comp sel",row," ",col)
            li[row][col]='o'
            n-=1
            check(li,n)
        else:
            continue

check(li,n)        
        
    
                
