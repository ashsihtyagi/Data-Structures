class circular_Queue:
    front=-1
    rear=-1
    arr=[]

    def __init__(self,n):
        self.back=n-1
        self.arr=[0]*n
        self.cs=0
        self.ms=n
        self.front=0
        self.rear=n-1


    def is_full(self):
        return self.cs==self.ms

    def is_empty(self):
        return self.cs==0

    def push(self,element):

        if not self.is_full():
            self.rear=(self.rear+1)%self.ms
            self.arr[self.rear]=element
            self.cs+=1

        else:
            print("Queue is full")

    def pop(self):
        if not self.is_empty():
            self.front=(self.front+1)%self.ms
            self.cs-=1
        else:
            print("queue is empty")

    def get_front(self):
        if not self.is_empty():
            return self.arr[self.front]

        else:
            return None

    def display(self):
        temp=0
        i=self.front
        while temp<self.cs:
            temp+=1
            print(self.arr[i])
            i=(i+1)%self.ms
        print("######")




q = circular_Queue(5)
q.push(10)
q.push(20)
q.push(30)
q.push(40)
q.push(50)
q.display()
q.push(60)
q.display()
q.pop()
q.pop()
q.display()

