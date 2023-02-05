# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 #  Create tuple 
fruits_zj = ('Mango','banana','grapes')
fruits_zj2 = tuple(('Mango','banana','grapes'))

fruits_zj2 = ('Mango')

# Get value
print(fruits_zj[1])

# Can't change value 
#fruits_zj[0] = 'pears'

# delete tuple

#del fruits_zj2

# Get length

print(len(fruits_zj))
print(fruits_zj, fruits_zj2)

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set 

fruits_zj_set = {'apples', 'mango', 'oranges'}

# Check if in set 

print('apples' in fruits_zj_set)

# Add to set 
fruits_zj_set.add('grapes')

# Remove from set
fruits_zj_set.remove('apples')

# Clear set
fruits_zj_set.clear()

# Delete set 

del fruits_zj_set

print(fruits_zj_set)