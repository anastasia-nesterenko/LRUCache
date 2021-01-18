class Node:
    """A class to represent a node of doubly linked list

    Attributes
    ----------
    key : Any
        key of the node
    val : Any
        value of the node
    next : Node
        link to the next node in cache
    prev : Node
        link to the previous node in cache
    """

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val

        self.next = None
        self.prev = None
