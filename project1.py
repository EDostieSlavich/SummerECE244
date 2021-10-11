"""
UMass ECE 241 - Advanced Programming
Project #1   Fall 2021
project1.py - Sorting and Searching

"""

import matplotlib.pyplot as plt


"""
Stock class for stock objects
"""
class Stock:

    """
    Constructor to initialize the stock object
    """
    def __init__(self, sname, symbol, val, prices):
        self.sname = sname
        self.symbol = symbol
        self.val = val
        self.prices = prices

        pass


    """
    return the stock information as a string, including name, symbol, 
    market value, and the price on the last day (2021-02-01). 
    For example, the string of the first stock should be returned as: 
    “name: Exxon Mobil Corporation; symbol: XOM; val: 384845.80; price:44.84”. 
    """
    def __str__(self):

        pass


"""
StockLibrary class to mange stock objects
"""
class StockLibrary:

    """
    Constructor to initialize the StockLibrary
    """
    def __init__(self):

        pass


    """
    The loadData method takes the file name of the input dataset,
    and stores the data of stocks into the library. 
    Make sure the order of the stocks is the same as the one in the input file. 
    """
    def loadData(self, filename: str):

        pass


    """
    The linearSearch method searches the stocks based on sname or symbol.
    It takes two arguments as the string for search and an attribute field 
    that we want to search (“name” or “symbol”). 
    It returns the details of the stock as described in __str__() function 
    or a “Stock not found” message when there is no match. 
    """
    def linearSearch(self, query: str, attribute: str):

        pass


    """
    Sort the stockList using QuickSort algorithm based on the stock symbol.
    The sorted array should be stored in the same stockList.
    Remember to change the isSorted variable after sorted
    """
    def quickSort(self):

        pass


    """
    build a balanced BST of the stocks based on the symbol. 
    Store the root of the BST as attribute bst, which is a TreeNode type.
    """
    def buildBST(self):

        pass

    """
    Search a stock based on the symbol attribute. 
    It returns the details of the stock as described in __str__() function 
    or a “Stock not found” message when there is no match. 
    """
    def searchBST(self, query, current='dnode'):

        pass



# WRITE YOUR OWN TEST UNDER THIS IF YOU NEED
if __name__ == '__main__':

    stockLib = StockLibrary()
    testSymbol = 'GE'
    testName = 'General Electric Company'


    print("\n-------load dataset-------")
    stockLib.loadData("stock_database.csv")
    print(stockLib.size)


    print("\n-------linear search-------")
    print(stockLib.linearSearch(testSymbol, "symbol"))
    print(stockLib.linearSearch(testName, "name"))


    print("\n-------quick sort-------")
    print(stockLib.isSorted)
    stockLib.quickSort()
    print(stockLib.isSorted)


    print("\n-------build BST-------")
    stockLib.buildBST()


    print("\n---------search BST---------")
    print(stockLib.searchBST(testSymbol))

