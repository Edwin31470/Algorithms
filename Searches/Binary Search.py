
def BinarySearch(List,first,last,itemSought):
    itemFound = False
    searchFailed = False
    while not itemFound and not searchFailed:
        midpoint = (first+last)//2
        print("Comparing {0} and {1}".format(first,last))
        if List[midpoint] == itemSought:
            itemFound = True
        else:
            if first >= last:
                searchFailed = True
            else:
                if List[midpoint] > itemSought:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
                    
    if searchFailed:
        print("Item not in list")
    else:
        print("Item found in list")

if __name__ == "__main__":
    List = [0,2,5,6,9,11,15,17,21,25]
    itemSought = int(input("Input a number to find: "))
    BinarySearch(List,0,10,itemSought)
