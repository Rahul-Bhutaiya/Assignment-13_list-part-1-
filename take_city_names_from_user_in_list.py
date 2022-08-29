#Write a Python script to create a list of city names taken from the user.

list=[]
n_value=int(input('How Much City Names You Want To Enter...? : '))
print('Enter Values Below...')

while n_value>0:
    list.append(input('Enter - '))
    n_value-=1

print('List of City Names :',list)