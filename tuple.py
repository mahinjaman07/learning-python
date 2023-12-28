# declare and syntax tuple list
# mytuple = ("apple", "banana", "cherry", "lemon", "pynapple");

# access tuple list data

# access tuple list item use indexing
# firstItem = mytuple[0];
# print(firstItem)

# access tuple list last item use negative indexing

# lastItem = mytuple[-1];
# print(lastItem);

# access tuple list item use Range of Indexes

# someitems = mytuple[1:4];
# print(someitems)


# check tuple list item

# if "cherry" in mytuple:
#     print(f"Yes cherry in the list");
#
# else:
#     print("cherry is out of this tuple");



# Update tuple list

#typle list is not changeable list / eta amra directly change and update na korte parleo amra kiso opay babohar kore tuple list ke change ba update korte pari

# add item to update tuple list
# mytuple = ("apple", "banana", "cherry");
#
# myLi = list(mytuple);
# myLi.append("Aluu");
# mytuple =tuple(myLi);
#
# print(mytuple)

# another way to add tuple list item
# x = (1, 2, 3, 4);
# y = (5,);
# x += y;
# print(x);

# remove item in tuple list

# mytuple = ("apple", "banana", "cherry", "lemon", "pynapple");
# myLi = list(mytuple);
# myLi.remove("lemon");
# mytuple = tuple(myLi);
# print(mytuple);

# Unpack tuple list

# 1. use variable
# mytuple = ("apple", "banana", "cherry" );

# a, b, c = mytuple;
# print(b);

# Using Asterisk *  etar maddhome amra amader jei list item ke kono variable a rakha hoy nai oi item guluke akta array/ list er moddhe return pabo


# mytuple = ("apple", "banana", "cherry", "lemon", "pynapple");
#
# a, b, c, *d = mytuple;
# print(a);
# print(b);
# print(c);
# print(d);

# Loop tuple

# for loop
# mytuple = ("apple", "banana", "cherry", "lemon", "pynapple");

# for fruit in mytuple:
#     print(fruit)

# Loop Through the Index Numbers

# for i in range(len(mytuple)):
    # print(i) #index
    # print(mytuple[i]); #access tuple list item Loop Through the Index Numbers

# Join tuple list

# tupleList1 = (1, 2, 3, 4);
# tupleList2 = (5, 6, 7, 8);
#
# tupleList3 = tupleList1 + tupleList2;
# print(tupleList3)


# Multiply Tuples
# tpList = (1, 5, 10, 3, 4)
# DbTuple = tpList * 2;  # etar maddhome amra ekta tuple list ke onno arekta tuple list er maddhome jotobar iccha copy kore rakhte pari
# print(DbTuple)

# touple method

# 1. count()
# 2. index()


tpList = (1, 5, 10, 3, 4, 1, 4, 5, 1, 10, 5, 1, 5, 4, 5, 1);
# c1 = tpList.count(1);  # tuplr.list er madhome amra amader tuple list er moddhe akta item koybar ase oita dekhte pari
# print(c1);

i10= tpList.index(10);
print(i10)
