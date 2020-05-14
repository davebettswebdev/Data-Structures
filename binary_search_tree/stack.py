
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0               
        self.storage = LinkedList() 

    def __len__(self):     
        return self.size
        # return len(self.storage)
    
    def len(self):
        return self.size

    def push(self, value):  
        self.storage.add_to_head(value)
        self.size = self.size +1 
        # return self.storage.append(value)

    def pop(self):
        if self.size > 0: 
            self.size = self.size -1 
        return self.storage.remove_from_head() 
       
    #    if not self.storage:
    #        return None
    #    else:
    #        return self.storage.pop()class Node:

class Node: 
      def __init__(self, value=None, next_node=None):
          self.value = value
          self.next_node = next_node
          
      def get_value(self): 
          return self.value
    
      def get_next(self): 
          return self.next_node

      def set_next(self, new_next): 
          self.next_node = new_next 

class LinkedList: 
    def __init__(self):
        self.head = None 

    def remove_from_head(self): 
        if not self.head:
            return None
        else: 
            value = self.head.get_value() 
            self.head = self.head.get_next()
            return value
            
    def add_to_head(self, value): 
        node = Node(value) 
        node.next_node = self.head 
        self.head = node 
      
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size
#         # return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)
#         self.size = self.size +1
#         # return self.storage.append(value)

#     def pop(self):
#         if self.size > 0:
#             self.size = self.size -1
#             return self.storage.pop()
#         else:
#             return None
#     #    if not self.storage:
#     #        return None
#     #    else:
#     #        return self.storage.pop()class Node:

