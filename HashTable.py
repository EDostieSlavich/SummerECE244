class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.side = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def getSide(self):
        return self.side

    def setSide(self, newside):
        self.side = newside


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
        self.orderedSlots = [None] * self.size
        self.orderedData = [[None]* self.size] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.orderedSlots[hashvalue] = OrderedList()
            self.slots[hashvalue] = key
            self.orderedSlots[hashvalue].add()
            self.data[hashvalue] = data
            self.orderedSlots[hashvalue].head.setSide(data)

        else:
            found = False
            current = self.orderedSlots[hashvalue].head
            while current is not None and not found:
                if current.getData() == key:
                    current.setSide(data)
                    found = True
                else:
                    current = current.getNext()
            else:
                found = False
                self.orderedSlots[hashvalue].add(key)
                current = self.orderedSlots[hashvalue].head
                while current is not None and not found:
                    if current.getData() == key:
                        current.setSide(data)
                        found = True
                    else:
                        current = current.getNext()

                # nextslot = self.rehash(hashvalue,len(self.slots))


            #while self.slots[nextslot] != None and \

                   # self.slots[nextslot] != key and count != self.size:
                #nextslot = self.rehash(nextslot, len(self.slots))


            # if self.slots[nextslot] == None:
            #     self.slots[nextslot] = key
            #     self.data[nextslot] = data
            # else:
            #     self.data[nextslot] = data  # replace


    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        current = self.orderedSlots[position].head
        while current is not None and not found:
            if current.getData() == key:
                data = current.getSide()
                found = True
            else:
                current = current.getNext()
        # while self.slots[position] != None and \
        #         not found and not stop:
        #     if self.orderedSlots[position].head.getData() == key:
        #         found = True
        #         data = self.data[position]
        #     else:
        #         position = self.rehash(position, len(self.slots))
        #         if position == startslot:
        #             stop = True
        return data

    def getList(self, value):
        current = self.orderedSlots[value].head
        table = []
        while current is not None:
            table.append(current.getData())
            current = current.getNext()
        return table


    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"
print(H.slots)
print(H.data)

H[31] = "water bear"
print(H.slots)
print(H.data)
print(H.get(31))
print(H.getList(9))
