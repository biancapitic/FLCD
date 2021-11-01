class SymbolTable:

    def __init__(self):
        self.capacity = 19
        self.elements = []

        for i in range(self.capacity):
            self.elements.append([])

    def hash_function(self, elem):
        s = 0
        for chr in elem:
            s += ord(chr)
        return s % self.capacity

    def search(self, elem):
        hashVal = self.hash_function(elem)
        for i in range(len(self.elements[hashVal])):
            if self.elements[hashVal][i] == elem:
                return hashVal, i

        return -1, -1

    def getElemPos(self, elem):
        return self.search(elem)[1]

    def add(self, elem):
        hashVal = self.hash_function(elem)
        pos = self.search(elem)
        if pos != (-1, -1):
            return pos
        self.elements[hashVal].append(elem)
        return hashVal, len(self.elements[hashVal]) - 1

    def __str__(self):
        return str(self.elements)