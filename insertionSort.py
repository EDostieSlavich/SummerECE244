def insertionSort(alist=[]):
    if len(alist) > 1:
        sorted = alist[0]
        i = 1
        nextSort = alist[i]
        while i < len(alist):
            if nextSort < sorted:
                j = i
                while j > 0:
                    if alist[j] < alist[j-1]:
                        temp = alist[j]
                        alist[j] = alist[j-1]
                        alist[j-1] = temp
                        j = j - 1
                    else:
                        j = 0
                i = i + 1
            else:
                j = i
                while j < len(alist) - 1:
                    if alist[j] > alist[j+1]:
                        temp = alist[j]
                        alist[j] = alist[j+1]
                        alist[j+1] = temp
                        j = j + 1
                    else:
                        j = len(alist) - 1
                i = i + 1
    return alist


list1 = [76, 67, 93, 22, 97, 74, 10, 8, 18, 63]
ordered = insertionSort(list1)
print(ordered)
print(len(list1))
last = len(list1) -1
first = 0
midpoint = (first + last)//2
print(list1[midpoint])
newList = list1[0:midpoint]
print(newList)

