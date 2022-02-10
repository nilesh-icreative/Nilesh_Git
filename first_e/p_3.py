
number = [111,11,1002,9999,0,1000,999,1014,1008]

x = [i for i in range(1000,9999+1) if i in number]

y = [i for i in x if int(str(i)[0])%2!=0 and int(str(i)[3])%2==0]

z = [ i for i in y if i%3==0 or i%7==0]

print("The Number is:",z)
