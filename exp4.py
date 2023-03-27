def a(l):#fuction for adding elements to list
	el=int(input('Enter the element to add:'))
	l.append(el)
def p(l):#fuction for printing list
	print('List l=',l)
def v(l):#fuction for printing average of elements in list
	if(len(l)>0):
		c=len(l)
		sum=0
		for i in l:
			sum+=i
		average=sum/c
		print('Average value of elements in the list',average)
	else:
		print('add elements in the list and try again')
def r(l):#fuction for removing an element 
	i=int(input('Enter the index value to remove the element'))
	if(len(l)==0):
		print('add elements in the list')
	elif(i>len(l)):
		print('enter a valid index of list')
	else:
		l.pop(i)
def m(l):#fuction for finding the minimum value in list
	if(len(l)>0):
		mini=l[0]
		for i in l:
			if(i<mini):
				mini=i
		print('The minimum element in the list is ',mini)
	else:
		print('Add elements in the list and try again')
l=[]#empty list omayova
menu="""******
a - to add element
p - to print the list
v - find the average of list of values
r - to remove an element
m - to find the minimum
q - quit"""#menu for inputs
while(True):#looping the whole code
	print(menu)#prints menu
	user=input('Please enter your choice:')#takes input from user
	if(user=='a'):#calling funtion a
		a(l)
	elif(user=='p'):#calling funtion p
		p(l)
	elif(user=='v'):#calling funtion v
		v(l)
	elif(user=='r'):#calling funtion r
		r(l)
	elif(user=='m'):#calling funtion m
		m(l)
	elif(user=='q'):#for stoping the code
		print('End of the program')
		break
	else:#asking for a valid input
		print('enter the input in menu')
