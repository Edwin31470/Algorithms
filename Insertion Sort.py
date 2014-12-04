import pdb

def insertion_sort(List,First,Last):
    for CurrentPtr in range(First+1,Last):
        CurrentValue = List[CurrentPtr]
        Ptr = CurrentPtr - 1
        while (List[Ptr] > CurrentValue) and (Ptr >= 0):
            List[Ptr+1] = List[Ptr]
            Ptr = Ptr -1
        List[Ptr+1] = CurrentValue
    print(List)

if __name__ == "__main__":
    List = [10,15,3,7,11,6,79,1024,6,8,6]
    First = 0
    Last = len(List)
    insertion_sort(List,First,Last)
