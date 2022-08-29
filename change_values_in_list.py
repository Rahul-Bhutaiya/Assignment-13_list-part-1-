"""
Write a python script to Change the values "SQL" and "Reactnative" with the values
"NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative",
"Javascript", "Python"]
"""

list1=["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
print('Original List :',list1)

for x in list1:
    if x=='SQL':
        list1[list1.index('SQL')]='NoSQL'
    if x=='Reactnative':
        list1[list1.index('Reactnative')]='Flutter'

print('Values Changed In List :',list1)