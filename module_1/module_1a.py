"""
1) Write  a  program  that  prints  your  full  name and  says  how  many  character  each  name  has.
For  example,the  output  should  be  displayed  in  the  following  format:

Name: Nasrin Dehbozorgi
(one line space)
This name has 16 characters. 
"""
print("\n===Problem 1===\n")
print("Name: ")
input_name = input()
if str(input_name):
    name_char = len(input_name.replace(" ", ""))
    print(f"This name has {name_char} characters")
else:
    print("You've done something interesting here. Don't do it again.")


"""
2) Write  a  program  that  displays  the  area and  perimeter of  a  rectangle  with  the 
width  of  4.5  and  height  of  7.9.
"""
print("\n===Problem 2===\n")
w = 4.5
h = 7.9
a = .5*4.5*7.9
p = (2*4.5)+(2*7.9)
print(f"Triangle area is {a:.2f} and perimeter is {p:.2f}")

"""
3) Write  a  program  that  that  solves  the  following  equations and displays  the  value  
for  x  and  y.  
a) 3.4x + 5.6x = 12
b) 5y – 6.7y = 21

The  output  should  be  displayed  in  the  following  format:
The  value  of  x is  .....
The  value  of  y is  .....
"""
print("\n===Problem 3===\n")
x = 12/(3.4+5.6)
y = 21/(5-6.7)
print(f"The value of x is {x:.2f}")
print(f"The value of y is {y:.2f}")
