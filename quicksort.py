list1 = [3,1,4,2,5]
def quicksort(list2):
    #recursion,end condition
    if len(list2)<2:
        return list2
    mid = list2[0]
    left = [x for x in list2 if x<mid]
    right = [x for x in list2 if x>mid]
    middle = [x for x in list2 if x==mid]
    return quicksort(left)+middle+quicksort(right)
print(quicksort(list1))