# Python RegEx

''''
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module:

'''

'''
RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:


Function	Description
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string
'''
import re

# match() / eta amader dewa string er moddhe sodho first word er moddhe check korbe

myPattern = r"mahin";

if re.match(myPattern, "I am mahin jaman, i am a stuident"):
    print(f"pawa gese {myPattern}");

else:
    print(f"{myPattern} pawa jay ni");


# search / amader dewa string er moddhe thaka shob word er moddhe khujbe

myPattern1 = r"student";

if re.search(myPattern1, "I am mahin jaman, i am a student"):
    print(f"{myPattern1} pawa gese ");

else:
    print(f"{myPattern1} pawa jay ni");


# findall() / eta amader pattern onujaye khujar por je koybar amader khuje pabe oi koyta pattern niye amader akta list return korbe

myPattern2 = r"Lorem";

mytext = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.";

regEx = re.findall(myPattern2, mytext);
print(regEx)



# extra function

'''
1.start()
2.end()
3.span()
'''

pt = r"color";

text = "My favorite color is red";

match = re.search(pt, text);


if match:
    print(match.start())
    print(match.end())
    print(match.span())