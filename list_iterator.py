from node import Node

class LinkedList: 
    def __init__(self,collection=None): 
        self.head = None
        if collection: 
            for item in reversed(collection): 
                self.insert(item)

    def __iter__(self): 
        def value_generator(): 
            current = self.head
            while current: 
                yield current.value
                current = current.next 
        return value_generator() 

    def __len__(self): 
        return len(list(iter(self))) 

    def __str__(self): 
        output = "" 
        for stuff in self: 
            output += f"[ {stuff} ] -> " 
        output += "None"
        return output 

    def __eq__(self, other): 
        return list(self) == list(other) 

    def insert(self,stuff): 
        self.head = Node(stuff, self.head) 

    def append(self,stuff): 
        node = Node(stuff) 
        if not self.head:
            self.head = Node 
            return
        current = self.head 
        while current.next: 
            current = current.next 
        current.next = node 

def list_comp(arr): 
    new_arr = [num + 1 for num in arr] 
    return new_arr 

def make_a_tuple(arr): 
    new_tup = tuple(arr)
    return new_tup 
        

        