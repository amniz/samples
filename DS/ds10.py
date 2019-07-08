from ds9 import make
l=make()
from stackreal import Stack
h=Stack()
for i in l:
    h.add(i)
print("in h")
h.display()
