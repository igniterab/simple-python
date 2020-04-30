x = str(input("Enter the string to be encrypted : "))
y = int(input("Enter the key: "))
s=""
z = []
d=0

if x.isupper():
       
       for i in x:
              i = ord(i)+3
              if i >90:
                     d=90-i
                     z.append(chr(64-(d)))
              else:     
                     z.append(chr(i))
else:
       for i in x:
              i = ord(i)+4
              if i >122:
                     d=122-i
                     z.append(chr(96-(d)))
              else:     
                     z.append(chr(i))
       
print(s.join(z))
