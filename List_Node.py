class List_Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


a = List_Node(1)
b = List_Node(2)
a.next = b
print(a.value, a.next)