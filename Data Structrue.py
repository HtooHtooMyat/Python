
number= [] # empty list
subjects = ["CP140", "CP240"]  # list of strings
scores = [18,25,96]  # list of integers
print(number,subjects, scores)

my_list =[1,2,3,4]
for element in my_list:
    print (element, end=',')


my_list =['a',1,True]
my_list.append ([1,2])
print (my_list)

my_list =['a',1,2,True]
my_list.extend ([1,2])
print (my_list)

my_list = [1,2,3,True]
my_list.pop (1)
print (my_list)

my_list = [1,2,3,True]
my_list.insert(4,5)
print (my_list)


my_list = [1,2,3,True]
my_list.remove(3)
print (my_list)

vowel=['e','a','i','o','u','e']
index= vowel.index ('e')
print ('The index of e:',index)

# Operating System List
os = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for os in reversed(os):
    print(os)

vowels=['e','a','u','o','i']
vowels.sort( )
print('Sorted list:', vowels)

# mixed list
list = ['cat', 0, 6.7]

# copying a list
new_list = list.copy()

# Adding element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List: ', list)
print('New List: ', new_list)