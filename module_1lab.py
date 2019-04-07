"""

"""

"""
Question 1:
Print the following using for loops:

*
**
***
****
...
n(*)

for an int the user gives
"""

print("Please enter a number")
x = input()

if not int(x):
    raise TypeError("Input must be an integer")

else:
    current_str = ""
    for i in range(0, int(x)):
        current_str = current_str + "*"
        print(current_str)





