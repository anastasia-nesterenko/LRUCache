from Node import Node


class LRUCache(dict):
    """A class to represent least-recently used cache

    Attributes
    ----------
    capacity : int
        capacity of the cache
    _head : Node
        dummy head node
    _tail : Node
        dummy tail node
    """

    def __init__(self, capacity: int):
        """Construct all the necessary attributes for the lru cache object

         :param capacity: int
        """
        super().__init__()
        self.capacity = capacity

        self._head = Node()
        self._tail = Node()

        self._head.next = self._tail
        self._tail.prev = self._head

    def get(self, key):
        """Get value from cache by key

        :param key: Any
        :return val: Any
        """
        if key not in self:
            return None
        node = self[key]
        self._move_to_head(node)
        return node.val

    def put(self, key, value):
        """Put element to cache

        :param key: Any
        :param value: Any
        """
        if key in self:
            node = self[key]
            node.val = value
            self._move_to_head(node)
        else:
            node = Node(key, value)
            self[key] = node

            self._add_to_head(node)

            if len(self) > self.capacity:
                self.delete(self._tail.prev.key)

    def delete(self, key):
        """Remove node from cache

        :param key: Any
        """
        if key in self:
            self._exclude(key)  # remove links
            del self[key]  # remove dict element

    def reset(self):
        """Reset cache"""
        self._head.next = self._tail
        self._tail.prev = self._head
        self.clear()

    def _add_to_head(self, node):
        """Add a new node to cache

        :param node: Node
        """
        node.prev = self._head
        node.next = self._head.next

        self._head.next.prev = node
        self._head.next = node

    def _move_to_head(self, node):
        """Move existing node to the head of cache

        :param node: Node
        """
        self._exclude(node.key)
        self._add_to_head(node)

    def _exclude(self, key):
        """Exclude node from the chain of links

        :param key: Any
        """
        node = self[key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def __str__(self):
        """Custom __str__

        :return text: str
        """
        text = self.__class__.__name__ + '['
        node = self._head.next
        while node.next is not None:
            text += "({}, {})".format(node.key, node.val)
            node = node.next
        return text + ']'
