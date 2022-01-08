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


def reverse(head):
    temp=head
    #print(head.data)
    if head==None or head.next==None:
        print(head.data, end='->')
        return head

    result=reverse(temp.next)
    print(head.data,end='->')
    #print(head.data)
    return head


def reverse_recur(head):

    #print(head.data)
    if head==None or head.next==None:
        return head

    result=reverse_recur(head.next)
    head.next.next=head
    head.next=None

    return result

def reversePI(head):
    if head==None:
        return head
    prev_,curr_,next_=None,head,head.next
    while next_!=None:
        curr_.next=prev_
        prev_=curr_
        curr_=next_
        next_=next_.next

    curr_.next=prev_
    return curr_







n=int(input())

head=None

while(n>0):
    n-=1
    data=int(input())
    head=insert_at_tail(head,data)


display_all(head)
print("\n")

#reverse(head)

#head=reversePI(head)
head=reverse_recur(head)

display_all(head)