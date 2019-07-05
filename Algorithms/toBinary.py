#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:to give the binary representation of the decimal number typed as the input

def tobin():
    n=int(input("enter the number"))
    st=str()
    while n>=1:
        st+=str(int(n%2))
        n/=2
    e=len(st)
    while e<32:
        st+="0"
        e+=1
    t=str()
    while e>0:
        e-=1
        t+=st[e]
    return t

    
    
