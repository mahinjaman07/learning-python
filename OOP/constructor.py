# constructor
# contructor method
# class studentsInfo:
#      def studentInfo(self, name, classes, roll, group, id):
#          schoolAndcollege = "Balla Coronation High School And College"
#          print(f"My school & College name is {schoolAndcollege}. My name is {name}. I am in class {classes}. My roll no: is {roll}. My group is {group}. My id no: is {id} ");
#
#
#
#
# student = studentsInfo();
#
# student.studentInfo("Mahin Jaman", 10, 50, "science", 114);
# student.studentInfo("Rahim Ahmed", 11, 10, "Commerce", 11224);
# student.studentInfo("Rasel Rahman", 12, 60, "Arts", 1554);

# parameterize contructor

class studentsInfo:

    def __init__(self, name, roll, classes,  group):
         print(f"My name is {name}. My roll no: is {roll}. I am in class {classes} & My group is {group}");




MahinJaman = studentsInfo("Mahin jaman", 50, 10, "Science");
RahimAhmed = studentsInfo("Rahim Ahmed", 30, 11, "Arts");
MannaRahman = studentsInfo("Manna Rahman", 80, 12, "Commerce");


