# can be used for comparison, sounds like english

today = 'wednesday'
yoga_day = 'Thursday'

a = 23
c = 12

print(a is c)
print(c is not a)

print(today is yoga_day)
print(today is not yoga_day)

'''
applies in lists and tuples
checks if key or value is a member of a list tuple or dictionary 
'''
# tuple
e = (1,2,3,4,5)
print(4 in e)

# list
A = [1,2,3,4,5,'edureka!']
print('edureka!' in A)
print('edureka' not in A)

'''
Dictionary to check if a key is a member of a dictionary
'''
f = {'Age':12, 'Name':'John', 'Jobs' : [], 'Cities': {'Nairobi':'Kenya', 'Mombasa':'Kenya'}}
print('Age' in f)
print('Nairobi' in 'Cities')