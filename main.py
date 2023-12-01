# list method sort example
list=[1,1,2,2,3,4,4,4,4]
list.sort()
print(list)

# list method append means add a number in list
list1=[1,3,3,3,4,4,48,]
list.append(9)
print(list)

# list reverse
list2=[1,3,4,45,5,6,56,5,5,5,5,5,5,]
list2.reverse()
print(list2)
# print(list[0])

# index in list
list4=[1,1,2,3,3,5,3,5,3,3,2,4,4,5.4,3]
print(list4.index(3))

# count method in list

list5=[23,5335,54343,"rahul","yelow",23,3,4,4,3,2,1]
print(list5.count(23))

# insert list  method
list6=[1,2,3,3,3,3,3,3,3,3]
list6.insert(2,20)
print(list6)

#  extend method in list

list7=[2,3,4,5,5,5,5,5,8395833]
list7.extend(list6)
print(list7)

# concatinate in two list
list8=[2,4,2,2,2,2,2,2,2,3,4,4,4,76543,6]
rahul=list8+list7
print(rahul)