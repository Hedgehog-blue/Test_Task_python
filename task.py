class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

         
class LinkedList:
    def __init__(self):
        self.head = None


    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return 
        current = self.head 
        while current.next:
            current = current.next
        current.next = new_node


    def get_length(self):
        count = 0
        current = self.head 
        while current:
            count += 1
            current = current.next 
        return count


    def get_element(self):
        n = self.get_length()
        if n <= 1:
            return None 
        index = (2 * n) // 3 - 1
        current = self.head 
        for i in range(index):
            if current is None:
                return None 
            current = current.next 
        return current.value if current else None

    


