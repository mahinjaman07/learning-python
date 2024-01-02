import datetime

x = datetime.datetime.now(); #year, date , hour, minute , second , milisecond
print(x)

y = x.strftime("%A") # etar maddome amra ajke ki bar eiya full dekhte pari and half er jonno "%a" ei directive use korte hbe

print(y)



b = x.date();  #only year , date, and day show korbe

print(b)