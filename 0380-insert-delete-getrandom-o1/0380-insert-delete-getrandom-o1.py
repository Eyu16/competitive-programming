class RandomizedSet:

    def __init__(self):
        self.randomize_set = set()
        self.numbers = []

    def insert(self, val: int) -> bool:
        if val in self.randomize_set:
            return False
        else:
            self.randomize_set.add(val)
            self.numbers.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.randomize_set:
            self.randomize_set.remove(val)
            self.numbers.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.numbers)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()