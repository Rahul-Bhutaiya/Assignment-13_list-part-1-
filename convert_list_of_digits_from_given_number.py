#Write a Python script to create a list, where each element of the list is a digit of a given number

number=input('Enter any Number : ')
list=[]

for x in number:
    list.append(int(x))

print('List of Digits :',list)