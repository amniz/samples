f=open("abc.txt","r")
g=f.read()
s=[]

for i in 'aeiou':
	s.append(i)
def check(s,g):
	l=[]
	for k in g:
		if k in s:
			l.append(k)
	return l
m=check(s,g)
#print(m)
mr=reversed(m)
coun=[0,0,0,0,0]
for k in mr:
	j=0
	while j<=4:
		if s[j]==k:
		
			lw=s.index(k)
			coun[lw]+=1
			m.pop()
			j-=1
			break
		else:
			j-=1
			
print(s)
print(coun)

			

		
	 
	
	
	


