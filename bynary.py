# Binary type Data / etar akti number ei number gula amder image er kaje use hoy / etar low number 0 and high number 256

# 1.bytes / bytes number 0-256
# 2. byteArray / bytearray number 0-256

myNum = [10, 15, 56, 23, 14, 85, 255];
# bytes()
# bytesNum = bytes(myNum);
# bytesNum[2] = 155; bytes number amra change korte parbo na
# print(bytesNum);

# bytearray() / eta change able
bytarr = bytearray(myNum);
bytarr[0] = 150;
print(bytarr)



