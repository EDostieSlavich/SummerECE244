def mergeSort_3_way(alist):
    print("Splitting ",alist)
    if len(alist) > 1:
        third = len(alist)//3
        lefthird = alist[:third]
        middle = alist[third:2*third]
        righthird = alist[2*third:]

        mergeSort_3_way(lefthird)
        mergeSort_3_way(middle)
        mergeSort_3_way(righthird)

        i=0
        j=0
        k=0
        l=0
        while i < len(lefthird) and j < len(middle) and k < len(righthird):
            if lefthird[i] > middle[j] and lefthird[i] > righthird[k]:
                alist[l]=lefthird[i]
                i=i+1
            elif middle[j] > lefthird[i] and middle[j] > righthird[k]:
                alist[l]=middle[j]
                j=j+1
            else:
                alist[l] = righthird[k]
                k=k+1
            l=l+1

        while i < len(lefthird) and j < len(middle):
            if lefthird[i] > middle[j]:
                alist[l] = lefthird[i]
                i=i+1
            else:
                alist[l] = middle[j]
                j=j+1
            l=l+1

        while j < len(middle) and k < len(righthird):
            if middle[j] > righthird[k]:
                alist[l] = middle[j]
                j=j+1
            else:
                alist[l] = righthird[k]
                k=k+1
            l=l+1

        while i < len(lefthird) and k < len(righthird):
            if lefthird[i] > righthird[k]:
                alist[l] = lefthird[i]
                i=i+1
            else:
                alist[l] = righthird[k]
                k=k+1
            l=l+1

        while i < len(lefthird):
            alist[l]=lefthird[i]
            i=i+1
            l=l+1
        while j < len(middle):
            alist[l]=middle[j]
            j=j+1
            l=l+1
        while k < len(righthird):
            alist[l]=righthird[k]
            k=k+1
            l=l+1

    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort_3_way(alist)
print(alist)
