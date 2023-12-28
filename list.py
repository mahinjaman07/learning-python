# list declare
# myList = ['Mahin', 'Manna', 'Rahim', 'Reduan'];
# print(myList);
# print(type(myList));

# access list item

# access first item use indexing
# firstItem = myList[0];
#
# print(firstItem);

#access last list item use Negative Indexing

# lastItem = myList[-1];
# print(lastItem);
#
# myFriends = ['Mahin', 'Manna', 'Rahim', 'Reduan', 'Ashrafe', 'Rifat'];

# access list item use Range of Indexes [first index : last index] ;

# mySpecialFriends = myFriends[2:5];
# print(mySpecialFriends);

# check list items in lists
# simple way

# print('Manna' in myFriends);

# use if else
# if 'Reduan' in myFriends:
#     print('Yes He is your friend Manna')
#
# else:
#     print('Sorry he is not your friend')
#

# Change list Items

# list1 = ['mahin', 'rahim', 'manna'];
# print(list1)
# list1[0] = 'nibir'; # change the list item use indexing
# print(list1);

# change the list item use range of index

# list2 = [1, 2, 3, 4, 5, 6, 7, 8];
# print(list2)
# list2[2:6] = [30, 40, 50, 60];
# print(list2)




# Add list item
# 1.Append("list item")
# 2.insert(index, "list item");
# 3.extend()


# fruits = ['Apple', 'Banana', 'Cherry'];

# list.append() eitar maddhome amara akta notun list item list item er last a add korte pari

# fruits.append('pynapple');

# use insert() to change the list / insert(index, "new item") diye amra index set kore new list item add korte pari

#
# print(fruits);
# fruits.insert(1, 'Lemon');
# print(fruits);

# list.extend(list2) eitar maddhome amra 2 ta list er je kono akta list er element onno list er moddhe diye 2 ta list er item akta list er vitore rakhte pari

# li1 = [1, 2, 3, 4];
# li2 = [5, 6, 7, 8];

# li1.extend(li2); #extend er madsdhome amra amader li1 er moddhe li2 er list item add kore dite pari

# print(li1);

# Remove list item
# 1.remove()
# 2.pop(index) index dile oi index er item ke delete korbe / pop() kono index na dile last item remove korbe;
# 3.del list[0] eityar maddhome amara amader list er indexing kore item ke delete kore dite pari
# 4.clear() eitar maddhome amra amder list ke akdom empty kore felte pari

# fruits1 = ['Apple', 'Banana', 'Cherry'];

# fruits1.remove("Banana");
# print(fruits1)
#
# fruits1.pop(2);
# print(fruits1)
#
# del fruits1[0];
# print(fruits1)
#
# fruits1.clear();
# print(fruits1)


# loop in list

myFriends = ['Mahin', 'Manna', 'Rahim', 'Reduan', 'Ashrafe', 'Rifat'];

# for loop in list

# for friend in myFriends:
#     print(friend)

# for loop use range of len

# Out put index and list item use for loop range of len
# for i in range(len(myFriends)):
#     index = i;
#     friend = myFriends[i]
#     print(i, friend);


# one line for loop


# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist];




# While loop

# i = 0;
#
# while i < len(myFriends):
#     # print(i)
#     print(myFriends[i])
#     i += 1;


# list comprehension  / eitar maddhome amra akta list ke onno akta list er vitore jotobar iccha copy kore rakhte pari

# newlist = [expression for item in iterable if condition == True]

# List = [1, 2, 3, 4, 5];
# listComprehension = [num *2 for num in List];
# print(listComprehension);


# Sort() list / etar maddhome amra akta elo melo list sajai te pari

# List = [2, 4, 3, 1, 5];
#
# List.sort()
# print(List)

# sort(reverse = True) / etar maddhome amra amr sajano list ke olta kore dite pari

# li1 = [1, 2, 3, 4, 5];
#
# li1.sort(reverse = True);
# print(li1)


# Copy List

# 1.copy()

# li1 = [1, 2, 3, 4, 5];
#
# liCopy = li1.copy();
#
# print(liCopy)

# 2.Method list()

# liCopy1 = list(li1);
# print(liCopy1);

#join list

# li1 = [1, 2, 3, 4, 5];
# li2 = ['a', 'b', 'c', 'd', 'e'];

# joinLi = li1 + li2;
# print(joinLi);

# extend()
# li1 = [1, 2, 3, 4, 5];
# li2 = ['a', 'b', 'c', 'd', 'e'];
#
# li2.extend(li1);
# print(li2)

# List Method

'''
1. append() Adds an element at the end of the list

2.clear()	Removes all the elements from the list

3.copy()	Returns a copy of the list

4.count()	Returns the number of elements with the specified value

5.extend()	Add the elements of a list (or any iterable), to the end of the current list

6.index()	Returns the index of the first element with the specified value

7.insert()	Adds an element at the specified position

8.pop()	Removes the element at the specified position

9.remove()	Removes the item with the specified value

10.reverse()	Reverses the order of the list

11.sort()	Sorts the list

'''
