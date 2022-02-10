
n=int(input('Enter Number:'));

for i in range(1,n+1):

    d={i:i*i};
    print("Dictionary is:",d);


dic={i: i*i for i in range(1,n+1)};
print("Dictionary is",dic);