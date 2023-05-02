a=input("enter a name")
b=['a','e','i','o','u']
count=0
for i in a:
    for j in b:
      if i==j:
          count+=1
          print(i)
print(count)
