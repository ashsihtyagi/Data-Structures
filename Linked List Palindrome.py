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

left=None
def checkPalindrome(left,right):

    if right!=None:
        print("right11:", right.data)
        print("left11:", left.data)
        result=checkPalindrome(left,right.next)
        left=result[1]
        print("Result_right:",bool(result[0]))
        print("Result_left:",result[1].data)
        if not result[0]:
            return (False,left)
        if left.data!=right.data:
            return (False,left)

        left=left.next

    return (True,left)

def palindrome(head1,head2):
    result=checkPalindrome(head1,head2)
    return result[0]




n=int(input())
head=None

while n>0:
    n-=1
    x=int(input())
    head=insert_at_tail(head,x)

display_all(head)
print("\n")

l=head

print(palindrome(head,head))