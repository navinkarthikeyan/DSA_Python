from array import *
arr1 = array('i',[1,2,3,4,5,6])
def accessElement(array,index):
    if index >= len(array):
        print("Not a valid input")
    else:
        print(array[index])
accessElement(arr1,4)