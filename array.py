'''
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''

myArr = [1, 12, 5, 45, 11, 21, 5, 23, 41, 5, 33];
print(myArr);

# access array item

x = myArr[2];
print(x);

# add array item

# append()

myArr.append(404);
print(myArr);

# insert()
myArr.insert(1, 505);
print(myArr);


# extend
myArr1 = [55, 66, 7];
myArr.extend(myArr1);
print(myArr);


# copy

x = myArr.copy();
print(x);

# count

y = myArr.count(5);
print(y)

# remove item

myArr.remove(5);
print(myArr);


# pop()

myArr.pop(5);
print(myArr);


# sort()

myArr.sort();
print(myArr);


# sort(reverse = True)

myArr.sort(reverse= True);
print(myArr);


# clear()

# myArr.clear();
# print(myArr)

# change item use indexing

myArr[0] = 5055;
print(myArr);
