from array import *
arr1 = array ('i', [1,2,3,4,5,6])
def searchElement( array , value ):
    for i in array :
        if i == value:
            return array.index(value)
        else:
            print("Invalid Value")
print(searchElement(arr1,3))
#to remove an element from an array just use arr1.remove(1) function 

