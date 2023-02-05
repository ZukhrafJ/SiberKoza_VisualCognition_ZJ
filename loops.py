# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_zj = ['ali', 'john', 'sare', 'nida']

# simple loop 
for person in people_zj:
    print(f'current person: {person}')

# break 
for person in people_zj:
    if person == 'sare':
        break
    print(f'current person: {person}')

# continue 
# for person in people_zj:
#     if person == 'sare':
#         continue
#     print(f'current person: {person}')

# range 

for i in range(len(people_zj)):
    print(people_zj[i])
for i in range(0, 11):
    print(f'Nuumber: {i}')
# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
    print(f'count: {count}')
    count +=1