class node:
    data=-1
    next=None

    def __init__(self,data):
        self.data=data

def length_of_ll(head):
    count=0
    temp=head
    while(temp!=None):
        count+=1
        temp=temp.next
    #print(count)
    return count

def display_all(head):
    temp=head
    while (temp!=None):
        print(temp.data,end="->")
        temp=temp.next

    return


def push(head,data):
    if head==None:
        return node(data)

    new_node=node(data)
    new_node.next=head
    head=new_node
    #print (head.data)
    return head


def pop(head):
    temp=head
    head=head.next
    #del temp
    return head


n=int(input())

head1=None

while n>0:
    n-=1
    x=int(input())
    head1=push(head1,x)

display_all(head1)