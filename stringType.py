# -----------------------------------String----------------------------------
# String Type variable
myName = 'Mahin Jaman';
print(myName);
print(type(myName));

# slicing String  / slicing amader indexing formate a kaj kore amra [er vitore indexing korbo] / [start index : end index]

b = "Hello, World!"
print(b[2:5]);

#Modify string
# 1.upper()
name = 'Mahin  Jaman';
upperName = name.upper();
print(upperName)

# 2. lower()

lowerName = name.lower();
print(lowerName)

# 3. strip()

helloWorld = " Hello, World Mahin ";
stripHello = helloWorld.strip();
print(stripHello)

# 4. string replace() / replace str diye amra amder je kono string type data er specific latter / word ke change kore dite pari

repText = 'Jelle World';
newText = repText.replace("Jelle" , "Hello");
print(newText)

# split() / ei split er maddhome amra amader string ke alada korte korte pari /sei jonno amader split(e vitor bole dite hobe ki dekhe se string ke alada korbe)

spText = "'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.'";
splitText = spText.split(".") # jei jei jaygay (.) dot ase oi jaygate amader string ke alada korbe
print(splitText)


# String Concatenation / String Concatenation mane amader 2 ta string ke jora lagano

a = 'Hello';
b = 'World';
c = a +" "+ b;
print(c);

# String Format

book = 'Bangla';
quantity = 50;
price = 500;

formatString = f"amader kache {quantity} ti {book} boi ache. prottekta {book} boi er price {price} Taka kore";
print(formatString)



