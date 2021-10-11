"""
UMass ECE 241 - Advanced Programming
Homework #2     Fall 2021
question4.py - position of partial sorted list

"""

"""
A shelf contains some products sorted according to their width,
e.g.     |||10, 20|||

we place more already sorted products with lesser width than
the one that are already present.
e.g.     |||10,20||1,2,4,7|||

Find the position of a given product (no sorting allowed and find it in O(log n))

e.g.     |||10, 20||1, 2, 4, 7|||
         position of product with width 10 is 0
         position of product with width 7 is 5
"""


class Shelf:

    def search_product(self, shelf_contents, lower_l, upper_l, product):
        # TODO Fill this function to find the position of the product in shelf_contents
        # TODO return the position of the product
        # TODO 'return -1' if the product is not in the shelf
        if not shelf_contents:
            return -1

        mid = int((upper_l - lower_l)/2)

        if shelf_contents[mid] <= shelf_contents[lower_l]:

            for index in range(0, maxIndex+1):
                if shelf_contents[index] == product:
                    return int(index)
        # elif product < shelf_contents[lower_l]:
        #     for index in range(maxIndex+1, upper_l):
        #         if shelf_contents[index] == product:
        #             found = index
        # else:
        #     found = -1
        # return found
        # mid = (upper_l - lower_l) // 2
        # for mid in range(1, len(shelf_contents)-1):
        #     if shelf_contents[mid] < shelf_contents[mid+1]:  # find where new sorted list starts
        #         if shelf_contents[mid] < shelf_contents[mid - 1]:
        #             if shelf_contents[len(shelf_contents) - 1] >= product >= shelf_contents[mid]:
        #                 k = mid
        #                 j = 0
        #                 for k in range(mid, len(shelf_contents)):
        #                     if product == shelf_contents[k]:  # find product in right list
        #                         return k
        #                     else:
        #                         for j in range(mid):
        #                             if product == shelf_contents[j]:  # find product in left list
        #                                 return j
        #                             else:
        #                                 return -1  # no such product exists




    def locate_product(self, pos, shelf_contents):
        '''
        (Don't Modify this function) Notifies the position of the product under consideration
        '''
        if pos < -1:
            print("\nFill in the search function and remove 'return -2'")
            return

        if pos is not -1:
            print("\n########### Found product on the Shelf ###########")

            print("Found product with width:{} at position:{} ".format(shelf_contents[pos],pos))

            print("\n##################################################")
        else:
            print("\nNo such product!!")


def main():
    shelf_contents = [10, 20, 1, 2, 3, 6, 7]
    shelf_obj = Shelf()
    product_to_be_found = 20
    pos = shelf_obj.search_product(shelf_contents, 0, len(shelf_contents) - 1, product_to_be_found)
    print("pos:{}".format(pos))
    shelf_obj.locate_product(pos, shelf_contents)


if __name__ == '__main__':
    main()
