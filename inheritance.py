# Python Inheritance
'''
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
'''
# class parentBaba :  #parent class
#     car = "MBW";
#     home = "10Flore";
#     money = "100 crore"


# class childKaka(parentBaba) :   #child class
#     bhangaBari = "";
#     bhangaCar = "";


# x = childKaka();
#
# print(x.home);


# Multiple Inheritance

# class p1 :
#     car = "BMW";
#     home  = "10 flore";


# class p2 :
#     AC = "Fefine";
#     Laptop  = "MAQ m2";


# class p3 :
#     Phone = "i - phone";
#     Taka  = "10 crore";



# class child(p1,p2,p3):
#     bhangaBari ="";
#     bhangaCar = "";


# x = child();


# print(x.car) # p1 theke
# print(x.Laptop) # p2 theke
# print(x.Taka) # p3 theke
# #  
# multielevel intehitance

class parent :
    car = "BMW";
    home = "10 flore";
    bankBalance = "100 crores";
    
# child1 ke prent diye inheritance korar maddhome child1 er moddhe amra parent er shob data/object ke access korte parbo

class child1(parent): 
    Ac ="Samsung";
    laptop ="MAQ";
    
    
# child2 ke child1 diye inheritance korar maddhome child2 er moddhe child1 e thaka data/object and parent e thaka data/object er full access peye jabo
class child2(child1):
    phone = "I-phone";
    taka = "10 crores";


# child3 ke child2 diye inheritance korar maddhome child3 er moddhe child2 te thaka data/object and child2 te thaka data/object and parent e thaka data/object er full access peye jabo

class child3(child2):
    computer = "intel core i5";
    sunglasses = 1;
    
# child4 ke child3 diye inheritance korar maddhome child4 er moddhe child3 te thaka data/object and child1,child2,child3 te thaka data/object and parent e thaka data/object er full access peye jabo

class child4(child3):
    bhangaBari = "";
    bhangaPhone = "";
    
    
x = child4();

print(x.home) # child1 theke
print(x.Ac) # child2 theke
print(x.computer) # child3 theke
