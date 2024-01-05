#polymorphism

class vehicle :
    def __init__(self, brand, model, component):
        self.brand = brand;
        self.model = model;
        self.component = component;



class myVehicle(vehicle):  # amra inheritance er maddhome  Vehicle ke inherit kore tar shob kichur access niyesi
     pass;  # pass keyword er maddhome amra vehicle er shob kichu use amader myVehicle er moddhe use kore felesi kinto eta abstruction method er karone amader internal data gula hide kore diyese


myPlane = myVehicle("DetectiveSEO", "Mahin 420", "All_component"); #convert class to object
print(myPlane.brand, myPlane.model, myPlane.component);

myCar = myVehicle("BMW", "B112", "Main_component"); #convert class to object
print(myCar.brand, myCar.model, myCar.component);

myBike = myVehicle("Apache", "Apache RTR  4V", "All_component"); #convert class to object
print(myBike.brand, myBike.model, myBike.component);
