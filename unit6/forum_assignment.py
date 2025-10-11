#Equivalent vs Identical

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
list3 = list1

list1 == list2
list1 is list2
list1 is list3

print(list1 == list2) #list1 and list2 are equivalent but not identical, same data different references
print(list1 is list2) #list1 is not qual to list2 
print(list3 is list1) #list3 is equal to list1,with the same reference
