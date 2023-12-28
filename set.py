# python set er moddhe amra indexing kore kichu korte parbo na / karon eta amder index maintain na kore nijer iccha moto kaj korbe / nijer iccha motot outpur dibe

# mySet = {"mahin", "rahim", "manna"};
# print(mySet[0]) / not use indexing
# print(mySet)

# The set() Constructor

# li = [1, 2, 3, 4, 5];
# liToSet = set(li);
# print(liToSet);


# access set item

# amra set ke akmatro loop er maddhome tar item ke out put pete pari

# li = {1, 2, 3, 4, 5};
#
# for num in li:
#     print(num)


# amra akta item ke check korte pari je oi item ti amder ser er moddhe ase kina

# print(3 in li)

# use if else

# if 5 in li:
#     print('yes this number in li');
#
# else:
#     print("this number is not found of this li")


#     if 10 in li:
#     print('yes this number in li');
#
# else:
#     print("this number is not found of this li")


# add item in set
# 1. add()
# 2.update()
# mySet = {"mahin", "rahim", "manna"};

# mySet.add('reduan');
#
# print(mySet)

# mySet1 = {"Emon", "Hasan", "Nibir", "Hannan"};

# mySet.update(mySet1); # update er maddhome amra akta set er vitore onno arekta set er item add kore dite pari
# print(mySet)

# abar chaile amra  akta list diye o tar item ke set er vitore add kore dite pari

# myLi =  [2, 4, 5, 10, 3, 1]
# mySet1.update(myLi)
# print(mySet1);


# remove set item
# 1. remove()
# 2.discard()
# 3.clear()
# 4.del
# mySet = {"Emon", "Hasan", "Nibir", "Hannan"};
# mySet.remove("Hasan");
# print(mySet);

# discard()

# mySet.discard("Nibir")
# print(mySet);

# pop()

# mySet.pop();

# clear()

# mySet.clear()

# del /etar maddhome amra amder set ke akdom delete kore dite pari

# print(mySet);
# del mySet
# print(mySet);


# set loop
# mySet = {"Emon", "Hasan", "Nibir", "Hannan"};
# for name in mySet:
#     print(name)

# join set

# 2.union()
# 2.update()

# set1 ={"Emon", "Hasan", "Nibir"};
# set2 = {"mahin", "rahim", "manna"};
# set3 = set1.union(set2)
# print(set3);

# update
set1 ={"Emon", "Hasan", "Nibir"};
set2 = {"mahin", "rahim", "manna"};
print(set1);
set1.update(set2);
print(set1);