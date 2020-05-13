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

    def add_to_end(self, value):   
        new_node = Node(value)
        if not self.head:
           self.head = new_node
        else:
           current = self.head 
           while current.get_next() is not None:
               current = current.get_next()
               current.set_next(new_node)

    def remove_from_head(self):
        # return None if there is no head (i.e. the list is empty)
        if not self.head:
            return None
        # if head has no next, then we have a single element in our list
        if not self.head.get_next():
            # get a reference to the head
            head = self.head
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None
            # return the value
            return head.get_value()
        # otherwise we have more than one element in our list
        value = self.head.get_value()
        # set the head reference to the current head's next node in the list
        self.head = self.head.get_next()
        return value