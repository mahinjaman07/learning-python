# Python Math
'''

Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

Built-in Math Functions

'''

#The min() and max() functions can be used to find the lowest or highest value in an iterable:

numbers = [10, 15, 22, 705, 3, 2, 50, 60];

minimumNumber = min(numbers);
print(minimumNumber)

maxNumer = max(numbers);
print(maxNumer)

# The abs() function returns the absolute (positive) value of the specified number:

negativeNumber = -70;

negativeToPosative = abs(negativeNumber);

print(negativeToPosative);


# The pow(x, y) function returns the value of x to the power of y (xy).

x = 20;
y = pow(x, 10);
print(y)