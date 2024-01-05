#Encapsulation

class parent:
    def __init__(self, name, fatherName):
        self.__name = name;   # (__) eita amder encapsulation korar maddhom/. eitar maddhome amader je kono variable ke encapsulation korte pari / ar amader kono function ba class er kono code encapsulathon korle amra sei varable ke sei function ba calss er baire theke access korte parbo na

        self.__fatherName = fatherName;

        print(name); # amader encapsulation code amader function ba class er vitor ei access korte hobe
        print(fatherName)  # amader encapsulation code amader function ba class er vitor ei access korte hobe




p1 = parent("Mahin Jaman", "Md. NurZaman Miah");

#print(p1.name) #/ amader encapsulation code amra class ba function er baire theke access korte parbo na