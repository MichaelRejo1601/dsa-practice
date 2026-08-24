# Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

# LRUCache(int capacity) Initialize the LRU cache of size capacity.

# int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.

# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.

# # what happpens when something in the middle is changes

# [C, A, B, C, D]

# #dictionary holds value and age 
# #problem is that we have to maintain the relative order which is still O(m)
# #linked list

# # we could use a doubly linked list to rearrange the item as needed based on age

# # temp = entrance
# # entrance = A
# # temp -> A
# # remove from exit
# # exit = A 

# exit <-- Node -- entrance

class Node:

    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.right = None
        self.left = None
    
    def remove_self(self):
        if self.right:
            self.right.left = self.left

        if self.left:
            self.left.right = self.right

    def insert_self_between(self, l, r):
        self.left = l
        self.right = r

        if l:
            l.right = self

        if r:
            r.left = self


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.count = 0

        self.entrance = Node(None, None)
        self.exit = Node(None, None)

    def get(self, key: int) -> int:

        node = self.cache.get(key, -1)

        if node == -1:
            return -1

        node.remove_self()
        node.insert_self_between(
            self.entrance.left,
            self.entrance
        )

        return node.val

    def put(self, key: int, value: int) -> None:

        if self.count == 0:

            node = Node(key, value)

            self.exit.right = node
            node.left = self.exit

            node.right = self.entrance
            self.entrance.left = node

            self.cache[key] = node
            self.count += 1

        elif key in self.cache:

            node = self.cache[key]
            node.val = value

            node.remove_self()
            node.insert_self_between(
                self.entrance.left,
                self.entrance
            )

        else:

            node = Node(key, value)

            self.cache[key] = node

            node.insert_self_between(
                self.entrance.left,
                self.entrance
            )

            self.count += 1

            if self.count > self.capacity:

                lru = self.exit.right

                del self.cache[lru.key]

                lru.remove_self()

                self.exit.right = lru.right

                self.count -= 1
