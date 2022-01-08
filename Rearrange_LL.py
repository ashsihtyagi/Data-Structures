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

def rearrange(left,right):
    if right==None:
        return (left,right)

    result=rearrange(left,right.next)
    if left==None:
        return left

    if left!=right and left.next!=right:
        temp=left.next
        left.next=right
        right.next=temp
        left=temp

    else:
        right.next=None


def fold_helper(left,right):
    if right==None:
        return(left)

    left=fold_helper(left,right.next)
    if left==None:
        return left

    if left!=right and left.next!=right:
        temp=left.next
        left.next=right
        right.next=temp
        left=temp

    else:
        right.next=None
        left=None

    return left

def fold(head):
    head=fold_helper(head,head)
    return head

n=int(input())

head=None

while(n>0):
    n-=1
    data=int(input())
    head=insert_at_tail(head,data)


display_all(head)
print("\n")


x=fold(head)
#print(head.data)
#print(x[1].data)
display_all(head)