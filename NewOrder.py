class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.orderedSlots = [OrderedList()] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
            self.orderedSlots[hashvalue].add((key, data))
        else:
            current = self.orderedSlots[hashvalue].head
            stop = False
            while current is not None and not stop:
                for x in current.getData():
                    if isinstance(x, int):
                        if x == key:
                            current.head.setData((key, data))
                            stop = True
                    else:
                        current = current.getNext()

            if not stop:
                self.orderedSlots[hashvalue].add((key, data))

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        stop = False
        found = False
        position = startslot
        data = None
        if self.slots[position] is key:
            data = self.data[position]
            found = True
        current = self.orderedSlots[position].head
        while current is not None and \
                not found and not stop:
            for x in current.getData():
                if isinstance(x, int):
                    if x == key:
                        data = current.getData()
                        found = True
                        for x in data:
                            if isinstance(x, str):
                                data = x
                    else:
                        current = current.getNext()


        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


H = HashTable()
H[45] = "kitty"
H[66] = "cat"
H[44] = "tiger"
print(H.get(45))
