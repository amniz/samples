class stack:
	def __init__(self):
		self.item=[]
		self.count=0
	def push(self,data):
		self.item.append(data)
		self.count+=1
	def pop(self):
		r=self.item.pop()
		self.count-=1
		return r
a=stack()
for i in 'aeiou':
	a.push(i)
b=stack()
for i in range(1,6):
	b.push(0)
f=open("abc.txt","r")
g=f.read()
def check(a,b,dat):
	c=stack()
	d=stack()
	j=0
	for i in 'uoiea':
		if i!=dat:
			c.push(a.pop())
			j+=1
		else:
			break
	for k in range(0,j):
		d.push(b.pop())
	b.item[len(b.item)-1]+=1
	temp=j
	while temp>0:
		a.push(c.pop())
		temp-=1


	while temp<j:
		b.push(d.pop())
		temp+=1
	return a,b

for i in g:
	if i in 'aeiou':
		check(a,b,i)	
print(a.item)
print(b.item)
