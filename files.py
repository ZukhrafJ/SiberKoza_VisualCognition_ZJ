# Python has functions for creating, reading, updating, and deleting files.
# opena file 
zukfile = open('zukfile.txt', 'w')

# get info 

print('Name: ', zukfile.name )
print('Is Closed: ', zukfile.closed)
print('Opening Mode: ', zukfile.mode)

# write to file 

zukfile.write('I am totally new to python')
zukfile.write(' and lets learn')
zukfile.close()

# append 

zukfile = open('zukfile.txt', 'a')
zukfile.write(' I also like MATLAB')
zukfile.close()

# read from file 
zukfile = open('zukfile.txt', 'r+')
text = zukfile.read(100)
print(text)