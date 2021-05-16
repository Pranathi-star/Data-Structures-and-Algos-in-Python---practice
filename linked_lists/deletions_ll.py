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

    def delete_at_begin(self):
        if self.head:
            self.head = self.head.next
            return self.head
        else: return None
        
    def delete_at_pos(self, pos):
        if pos == 0:
            self.delete_at_begin()
        else:
            length = 0
            ptr = self.head
            while(ptr):
                length += 1
                ptr = ptr.next
            if pos == length - 1:
                ptr = self.head
                while(ptr.next.next):
                    ptr = ptr.next
                ptr.next = None
                return self.head
            else:
                counter = 0
                ptr = self.head
                while(counter != pos - 1):
                    counter += 1
                    ptr = ptr.next
                link = ptr.next
                ptr.next = ptr.next.next
                link = None
                return self.head

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
llist.delete_at_begin()
llist.print_ll()
llist.delete_at_pos(1)
llist.print_ll()


             