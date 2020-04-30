name = str(input("Please enter your name :"))

flag = 0
for i in name:
       i = ord(i)
       if((i>=65 and i<=90)or(i>=97 and i<=122)):
              continue;
       else:
              flag=1
              print("Invalid name")
              break;
              
if flag == 0:
       
       pan = str(input("please enter your PAN card no. :"))

       for j in pan:
              j = ord(j)
              if((j>=65 and j<=90)or(j>=48 and j<=57)):
                     continue;
              else:
                     print("Invalid pan")
                     break;
