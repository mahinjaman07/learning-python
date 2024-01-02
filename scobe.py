#  start global scope

# Python Scope
'''
 1.local scope
 2. global scope
'''
 
x = 20
y = 20


def localSum(): #  start local scope
     
    a = 10; #eta amder local scope er moddhe ase / karon etake amara ei function er baire access korte parbona
    b = 10; #eta amder local scope er moddhe ase / karon etake amara ei function er baire access korte parbona
    
    return a + b; #  end local scope
 
 
def globalSum():
     a = x;
     b = y;
     return a + b;
 
 
 
localScope = localSum();
globalScope = globalSum();

print(f"I am localSum {localScope}");
print(f"I am global {globalScope}")
 
#  code sesh howar age porjonto eta global scopre