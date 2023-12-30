# Python Loops
# Python has two primitive loop commands:
#
# while loops
# for loops

# 1.while loop
# num = 0;
# while num <= 100:
#     # print(num);
#     num += 1;


# for loop

myLi = [20, 45, 10, 11, 24, 51, 46];
newLi = [];
for num in range(len(myLi)):
    newLi.append(myLi[num])


print(newLi)