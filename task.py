class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

         
class LinkedList:
    def __init__(self):
        self.head = None


    def add(self, value):
        pass


    def get_length(self):
        count = 0
        current = self.head 
        while current:
            count += 1
            current = current.next 
        return current


    def get_element(self):
        pass

    


