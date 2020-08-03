class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = []
        

    def add(self, key: int) -> None:
        self.d.append(key)
        

    def remove(self, key: int) -> None:
        self.d=[a for a in self.d if a != key]
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.d:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))
print(obj.contains(3))
obj.add(2)
print(obj.contains(2))
print(obj.d)
obj.remove(2)
print(obj.d)
print(obj.contains(2))

#alter
def _init_(self):
        """
        Initialize your data structure here.
        """
        self.res = {}

    def add(self, key: int) -> None:
        self.res[key] = key


    def remove(self, key: int) -> None:
        if key in self.res:
            del self.res[key]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.res