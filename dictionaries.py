# Python Dictionaries

# myDict = {
#     "Mahin":{
#         "Name": "Mahin Jaman",
#         "location": "Dhaka, Bangladesh",
#         "study": "10",
#         "group": "Science",
#         "age": 19
#     },
#
#     "Rahim":{
#     "Name": "Rahim Ahmed",
#         "location": "Dhaka, Bangladesh",
#         "study": "11",
#         "group": "Arts",
#         "age": 20
#     }
# };

#Python - Access Dictionary Items

# 1. use key name access dict item
# Mahin = myDict["Mahin"];
# print(Mahin["age"]);

# access dict item use get() method

# group = Mahin.get("group");
# print(group)

#2. keys() / eta diye amra akta dict er shob gula keys ke paite pari / and ei key diye tar prottekta valu o ber korte pari

# myDictKeys = Mahin.keys();
# print(myDictKeys)
# for key in myDictKeys:
#     personValue = Mahin[key]
#     print(key, personValue)
# print(myDictKeys)

#3. values() / etar maddhome amara amader dict er shob gula keys er value print korte pari

# person = {
#         "Name": "Mahin Jaman",
#         "location": "Dhaka, Bangladesh",
#         "study": "10",
#         "group": "Science",
#         "age": 19
#     };
#
#
# personValue = person.values();
# print(personValue);


#4. items() / etar maddhome amra dict er prottekta keys and value ke akekta tuple list hisabe return pabo

# person = {
#         "Name": "Mahin Jaman",
#         "location": "Dhaka, Bangladesh",
#         "study": "10",
#         "group": "Science",
#         "age": 19
#     };

# x = person.items();
#
# print(person.items() )


# Python - Change Dictionary Items

# 1. amra dictionaries er keys babohar kore key er value change korte pari
# person = {
#         "Name": "Mahin Jaman",
#         "location": "Dhaka, Bangladesh",
#         "study": "10",
#         "group": "Science",
#         "age": 19
#     };
#
# person["location"] = "Tangail";
# print(person)

# 2. update({"key" : "new value"}) method er maddhome keys er value change korte pari

# person.update({"group": "Arts"})
# print(person)


# Python - Add Dictionary Items
# 1. adding items
# 2.Update Dictionary
# 1.Adding Items / amra dictName["keys"] = value ; diye dict er moddhe notun keys and value add korte pari

# person = {
#         "Name": "Mahin Jaman",
#         "location": "Dhaka, Bangladesh",
#         "group": "Science",
#         "age": 19
#     };
#
# person["class"] = "Ten";
# print(person);

# 2.Update Dictionary / amra dictName.update({"keys" : "value" / num value}) ei bhabe update method er maddhome notun item ke set korte pari;


# person = {
#         "Name": "Mahin Jaman",
#         "location": "Dhaka, Bangladesh",
#         "group": "Science",
#         "age": 19
#     };
#
# person.update({"class" : 10});
# print(person);


# Python - Remove Dictionary Items
# 1.pop("keys");'
# 2.popitems(); / eta diye amra amader dict er last key and value ke remove korte pari
# 3.del  / The del keyword can also delete the dictionary completely:
# 4.clear()
# person = {
#         "Name": "Mahin Jaman",
#         "location": "Dhaka, Bangladesh",
#         "group": "Science",
#         "age": 19
#     };

# remove item use pop("keys") / amra jei key name debo oi key and value ke remove korbe

# person.pop("age");
# print(person);

# remove item use popitems() / remove the last item

# person.popitem();
# print(person)

# del / The del keyword can also delete the dictionary completely:

# del person();
#
# print(person)


# clear() / eta diye amra amader dict ke akdom empty dict kore dite pari

# person.clear();
#
# print(person)


# Python - Loop Dictionaries

# Loop Through a Dictionary

# You can loop through a dictionary by using a for loop.

# print keys
# person = {
#         "Name": "Mahin Jaman",
#         "location": "Dhaka, Bangladesh",
#         "group": "Science",
#         "age": 19
#     };

# for k in person:
#     print(x);

# You can also use the values() method to return values of a dictionary:

# for v in person.values():
#     print(v);

# You can use the keys() method to return the keys of a dictionary:

# for k in person.keys():
#     print(k)


# Loop through both keys and values, by using the items() method:

# for k,v in person.items():
#     print(k , v)

# Python - Copy Dictionaries
# 1. copy();
# 2. dict(main dict name)

# person = {
#         "Name": "Mahin Jaman",
#         "location": "Dhaka, Bangladesh",
#         "group": "Science",
#         "age": 19
#     };


# Make a copy of a dictionary with the copy() method:
# person2 = person.copy();
# print(person2);

# Another way to make a copy is to use the built-in function dict().

# person3 = dict(person);
# print(person3)


# Python - Nested Dictionaries
# Nested Dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# access Nested Dictionaries item

child2Name = myfamily["child2"]["name"];
print(child2Name)