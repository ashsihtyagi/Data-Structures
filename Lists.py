class lists:
    a=0
    li=[]

    def __init__(self,a):
        self.a=a
        self.li.append(a)

    def add(self,c):
        self.li.extends(c)


l1=lists(2)
print(l1[0])
l2=lists(3)
print(l2[0])

print(l1.add(l2))

