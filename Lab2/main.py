class SymbolTable:

    def __init__(self):
        self.capacity = 41
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

    def add(self, elem):
        hashVal = self.hash_function(elem)
        pos = self.search(elem)
        if pos != (-1, -1):
            return pos
        self.elements[hashVal].append(elem)
        return hashVal, len(self.elements[hashVal]) - 1


def main():
    st = SymbolTable()

    id1 = st.add("green")
    id2 = st.add("apple")
    id3 = st.add("pie")

    assert id1 == st.add("green")
    assert id2 == st.add("apple")
    assert id3 == st.add("pie")

main();