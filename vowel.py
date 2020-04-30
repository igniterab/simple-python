word = input("Enter the strings")
s = ""
d = []
l = ['a','e','i','o','u']
for i in word:
       if i in l:
              continue;
       else:
              d.append(i)
print(s.join(d))

       
