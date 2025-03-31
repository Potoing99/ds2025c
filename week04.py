class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link # 이동 move current
        current.link = Node(data)


    def __str__(self):
        # current = self.head
        # while current is not None:
        #      print(current.data)
        #      current = current.link
        # #return "Linked list!"
        # return "end"
        current = self.head
        out_texts = ""
        while current is not None:
            out_texts = out_texts + str(current.data) + " -> "
            current = current.link
        # return "Linked list!"
        return out_texts + "END"



ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)