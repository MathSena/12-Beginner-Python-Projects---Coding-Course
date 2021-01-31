import random
import time

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i

    return -1

def binary_search(l, target, low=None, high=None):
    if low is None:
        low=0
    if high is None:
        high = len(l) -1 
        
    if high<low:
        return -1


    if l(mindpoint) == target:
        return mindpoint

    elif target>l[mindpoint]:
        return binary_search(l, target, low, mindpoint-1)
    else:
        return binary_search(l, target, mindpoint+1, high)


if __name__=="__main__":
    sorted_list = set()
    while len(sorted_list)<length:
        sorted_list.add(random.randit(-3*length,3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()

    for targetin sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end-start)/length, "seconds")

    for targetin sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end-start)/length, "seconds")