# keyshave to be strings and the values can be anything
A = {'Age' :24, 'Name' : 'john'}
print(A)
print(A['Age']) # this is way more readable


# Or
A = [24,'john']
print(A[0])

# we can have a dictionry within a dictionary
A = {'Age' : 24, 'Name' : 'John', 'jobs' : [], 'cities' : {}}

print(A['Age'])
A = [24,'john']

print(A[0])