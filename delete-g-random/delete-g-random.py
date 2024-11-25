import random
class RandomizedSet(object):

    def __init__(self):
        self.mySet = {}
        self.array = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.mySet:
            return False
        self.array.append(val)
        self.mySet[val] = len(self.array)-1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.mySet:
            pos = self.mySet[val]
            self.array[pos] = self.array[-1]
            self.mySet[self.array[-1]] = pos
            self.array.pop()
            del self.mySet[val]

            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
#["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
#[[],[a],[b],[b],[],[a],[b],[]]
obj = RandomizedSet()

print(obj.insert("a"))
print(obj.remove('b'))
print(obj.insert('b'))
print(obj.getRandom())
print(obj.remove('a'))
print(obj.insert('b'))
print(obj.remove('b'))
print(obj.getRandom())



