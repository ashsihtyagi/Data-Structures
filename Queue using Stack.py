class stackq:
    primary=[]
    secondary=[]
    pri=[]
    sec=[]


    def __init__(self,n):
        self.primary=[0]*n
        self.secondary=[0]*n
        self.cs=-1
        self.pri=[]
        self.sec=[]

    def push_in_pop_efficient(self,element):
        x=self.cs
        m = -1

        if self.cs+1==len(self.primary):
            return self.full()

        if self.cs==-1:

            self.cs+=1
            self.primary[self.cs] = element
            # print(self.cs)
        else:

            #print("cs",x)

            while(x>=0):
                m += 1
                self.secondary[m]=self.primary[x]

                x-=1
            x+=1
            self.primary[x]=element
            #print("x",x)
            #print(self.primary)
            #print(self.secondary)

            while(m>=0):
                x+=1
                self.primary[x]=self.secondary[m]
                m-=1
            self.cs+=1
        #print(self.primary)

        return

    def empty(self):
        print("Queue is empty")

    def full(self):
        print ("Queue is full")

    def display(self):
        e=self.primary[::-1]
        for x in e:
            print(x)
        print("#########")
    def display2(self):

        for x in self.pri:
            print(x)

        print("#########")

    def pop_in_pop_efficient(self):
        if self.cs==-1:
            print("Queue is empty")
        else:
            print("Removed_element",self.primary.pop())
            self.cs-=1

    def push_in_push_efficient(self,element):
        self.cs += 1
        self.pri.append(element)


    def pop_in_push_efficient(self):

        if len(self.pri)==0:
            return self.empty()
        else:
            while(len(self.pri)>1):
                self.sec.append(self.pri.pop())
            self.pri.pop()
            # print(self.pri)
            # print(self.sec)
            while(len(self.sec)>0):
                self.pri.append(self.sec.pop())


print("Pop efficient using Iteration/list_array")
q=stackq(5)

q.push_in_pop_efficient(10)
# #q.pop_in_push_efficient()
# #q.pop_in_push_efficient()
q.push_in_pop_efficient(20)
q.push_in_pop_efficient(30)
q.push_in_pop_efficient(40)
#q.display()
q.push_in_pop_efficient(50)
q.display()
q.push_in_pop_efficient(60)
q.display()
q.pop_in_pop_efficient()
q.pop_in_pop_efficient()
q.display()


print("Push efficient using list methods/append_pop")


q2=stackq(5)
q2.push_in_push_efficient(67)
q2.push_in_push_efficient(45)
q2.push_in_push_efficient(89)
q2.push_in_push_efficient(90)
q2.push_in_push_efficient(23)
q2.display2()

q2.pop_in_push_efficient()
q2.pop_in_push_efficient()

q2.display2()
