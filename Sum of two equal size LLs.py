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


def insert_at_head(head,data):
    if head==None:
        return node(data)

    new_node=node(data)
    new_node.next=head
    head=new_node
    #print (head.data)
    return head

def insert_at_tail(head,data):
    if head==None:
        return node(data)

    temp=head
    while temp.next!=None:
        temp=temp.next

    new_node=node(data)
    temp.next=new_node

    return head


def sum_LL_same_size(head1,head2):

    temp1=head1
    temp2=head2

    if(temp1==None):
        return (None,0)

    result=node(0)
    returned_node,carry=sum_LL_same_size(head1.next, head2.next)
    result.next=returned_node

    sum_=temp1.data+temp2.data+carry


    carry=sum_//10
    result.data=sum_%10


    return (result,carry)

def ll(head1,head2):
    ll,carry=sum_LL_same_size(head1,head2)
    if carry!=0:
        new_node=node(carry)
        new_node.next=ll
        ll=new_node
    return ll

n = int(input())
m = int(input())
    # head=None
head1 = None
head2 = None
head=None

    # while n>0:
    # n-=1
    # x=int(input())
    # head=insert_at_tail(head,x)

while n > 0:
    n -= 1
    x = int(input())
    head1 = insert_at_tail(head1, x)

while m > 0:
    m -= 1
    x = int(input())
    head2 = insert_at_tail(head2, x)

display_all(head1)
print("\n")

display_all(head2)
print("\n")

head=ll(head1,head2)

display_all(head)