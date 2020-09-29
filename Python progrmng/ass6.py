list1=[1,20,33,5,44]
list2=[12,43,1,33,56]
def diff(li1,li2):
    return(list(set(li1)-set(li2)))
print(list1)
print(list2)
print(diff(list1,list2))

