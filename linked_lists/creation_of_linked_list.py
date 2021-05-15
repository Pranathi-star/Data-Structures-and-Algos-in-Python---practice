class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_end(self, data, tail):
        new_node = Node(data)
        if self.head:
            tail.next = new_node
            tail = new_node
            return tail
        else:
            self.head = new_node
            self.tail = new_node
            return self.tail

    def print_ll(self):
        ptr = self.head
        while(ptr):
            print(ptr.data, end=" ")
            print("->", end = " ")
            ptr = ptr.next
        print("NULL")

llist = Linked_list()
tail = None
tail1 = None
for i in range(int(input().strip())):
    if i == 0:
        tail1 = llist.insert_at_end(int(input().strip()), tail)
    else:
        tail1 = llist.insert_at_end(int(input().strip()), tail1)

llist.print_ll()

             