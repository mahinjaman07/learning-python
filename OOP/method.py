class method:

    #instace method
    def instanceMethod(self):
        print("Hello I am instanceMethod");

    #class method

    @classmethod # classmethod decorator

    def classMethod(cls):
        print("hello i am class method");

    @staticmethod #ststic method decorator

    def staticMethod():
        print("Hello i am static method")


x = method(); #amader class ke output pete sobar age amader class ke object a convert korte hbe

x.instanceMethod();
x.classMethod();
x.staticMethod();

# problem instance method

method.classMethod(); #class er name diye amra class method ke access korte pari kintu
# method.instanceMethod(); #amra class er nam diye amader instance method ke access korte pari na / jode korte chai amader error dibe
method.staticMethod() # class er name diye o amra static method ke access korte pari




