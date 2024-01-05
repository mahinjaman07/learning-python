# use my create module

# method 1 - use file name
# import module   #import module.py file
#
# module.MyModule()  #use the module function

# method 2 - use file name and then change the module name

import module as myModule


myModule.tee();
myModule.chips();
myBooks = myModule.books;
student = myModule.person;

print(myBooks);
print(student)