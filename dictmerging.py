
a = input("Enter the key :").split()
b = input("Enter the values :").split()


class_list = dict()
class_list[a] = int(b)
 
# Displaying the dictionary
for key, value in class_list.items():
	print('Name: {}, Score: {}'.format(key, value))
