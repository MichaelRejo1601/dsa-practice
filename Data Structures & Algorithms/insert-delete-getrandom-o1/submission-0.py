import random

class RandomizedSet:

    def __init__(self):
        self.countmap = {}
        self.valmap = {}
        self.count = -1

    def insert(self, val: int) -> bool:
        if val in self.valmap:
            return False
        
        self.count += 1
        self.countmap[self.count] = val
        self.valmap[val] = self.count

        return True

    def remove(self, val: int) -> bool:
        if val in self.valmap:
            index = self.valmap[val]
            last_val = self.countmap[self.count]

            if index != self.count:
                #swap
                self.countmap[index] = last_val
                self.valmap[last_val] = index

            del self.countmap[self.count]
            del self.valmap[val]

            self.count -= 1 
            return True
            
        return False

    def getRandom(self) -> int:
        return self.countmap[random.randint(0,self.count)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()