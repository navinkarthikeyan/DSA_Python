lst = [1,2,3,4,5,6]
def linearSearch(list , value):
    for i in list:
        if i == value:
           return list.index(value)
    return 'It is not present in the list' 
print(linearSearch(lst,3))