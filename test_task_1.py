import unittest

from task_1 import HashMap


class MyTestCase(unittest.TestCase):
    def test_hashmap(self):
        hashmap = HashMap()

        hashmap.put("apple", 10)
        self.assertEqual(hashmap.get("apple"), 10)

        hashmap.put("apple", 20)
        self.assertEqual(hashmap.get("apple"), 20)

        self.assertEqual(hashmap.get("banana"), None)

        hashmap.put("lemon", 30)
        hashmap.put("melon", 40)
        self.assertEqual(hashmap.get("lemon"), 30)
        self.assertEqual(hashmap.get("melon"), 40)


if __name__ == "__main__":
    unittest.main()
