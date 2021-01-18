import unittest

from LRUCache import LRUCache

cache = LRUCache(3)


class TestLRUCache(unittest.TestCase):

    def test0_init(self):
        self.assertEqual(0, len(cache))
        self.assertEqual(cache._tail, cache._head.next)
        self.assertEqual(cache._head, cache._tail.prev)

    def test1_put(self):
        cache.put(3, 57)
        cache.put(4, 44)
        cache.put(12, 4)
        self.assertCacheValues([(12, 4), (4, 44), (3, 57)])

    def test2_get(self):
        self.assertEqual(cache.get(4), 44)

    def test3_get_none(self):
        self.assertEqual(cache.get(100), None)

    def test4_move_to_head(self):
        cache.get(4)
        self.assertCacheValues([(4, 44), (12, 4), (3, 57)])

    def test5_capacity(self):
        cache.put(5, 5)
        self.assertCacheValues([(5, 5), (4, 44), (12, 4)])

    def test6_delete(self):
        cache.delete(4)
        self.assertCacheValues([(5, 5), (12, 4)])
        self.assertEqual(cache.get(4), None)

    def test7_reset(self):
        cache.reset()
        self.assertEqual(0, len(cache))
        self.assertEqual(cache._tail, cache._head.next)
        self.assertEqual(cache._head, cache._tail.prev)

    def assertCacheValues(self, nodes: list):
        cache_nodes = list()
        node = cache._head.next

        while node.next is not None:
            cache_nodes.append((node.key, node.val))
            node = node.next

        self.assertEqual(cache_nodes, nodes)
