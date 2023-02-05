# A List is a collection which is ordered and changeable. Allows duplicate members.
# creae list 

numbers = [1, 2, 3, 4, 5]
fruits_zj = ['mango' , 'banana', 'grapes']
# use a constructor 

numbers2 = list((1, 2, 3, 4, 5))

# get a value

print(fruits_zj[1])

#print(numbers, numbers2)

print(len(fruits_zj))

#append list
fruits_zj.append('oranges')
#remove from list

fruits_zj.remove('grapes')

# insert into position 

fruits_zj.insert(2, 'dragonfruit')

# Remove with pop

fruits_zj.pop(2)

# reverse list 

fruits_zj.reverse()
# sort list 

fruits_zj.sort()

# reverse sort

fruits_zj.sort(reverse=True)

# change value 

fruits_zj[0] = 'blueberry'
print(fruits_zj)
