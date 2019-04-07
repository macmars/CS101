"""
Lab 1
McKenzie Marshall
"""

"""
Activity 1: Display the Pattern
Write a program that displays the following pattern:

    J     A   V     V   A
    J    A A   V   V   A A
J   J   AAAAA   V V   AAAAA
 J J   A     A   V   A     A  

Now display your own pattern.

"""
print("\n===Activity 1===\n")
inline = f'''
    J     A   V     V   A
    J    A A   V   V   A A
J   J   AAAAA   V V   AAAAA
 J J   A     A   V   A     A    
'''
print(inline)

"""
Activity 2: Finding the Error
There is an error within the code shown in the screenshot below. Create a class called Activity2. After typing this 
code and compiling, you will see a red line at the bottom. What does this line mean? How did you fix the error?
public class Activity2 {
public static void main(String[] args)
{
System.out.println("There is a Problem in this code!")
System.out.println("If this message is printed that means")
System.out.println("The errors are fixed! GOOD JOB")
}
}
"""
print("\n===Activity 2===\n")


class Activity2:
    @staticmethod
    def main():
        print("There is a Problem in this code!")
        print("If this message is printed that means")
        print("The errors are fixed! GOOD JOB")


Activity2.main()

"""
Activity 3: Finding the Error
There is an error within the code shown in the screenshot below. Create a class called Activity3, 
and replace all the code which was auto-completed by Eclipse with what is shown below. After typing everything 
in and compiling, you will see a red line in various places throughout the code. What does this red line mean? 
How did you fix the errors? What did you learn from this activity?
public class Potato {
	public static void main(String[] args);
	{
		String course = "ITCS 1212";
		system.out.println("The Course name is : " + course);
	}
}

"""
print("\n===Activity 3===\n")


class Potato:
    @staticmethod
    def main():
        course = "ITCS 1212"
        print(f"The course name is: {course}")


Potato.main()

"""

Activity 4: Average Speed in Miles
Assume a runner runs 14 kilometers in 45 minutes and 30 seconds. 
Write a program that displays the average speed in miles per hour. (Note that 1 mile is 1.6 kilometers.)

"""
print("\n===Activity 4===\n")
dist_km = 14
dist_miles = dist_km / 1.6
time_m = 45
time_s = 30
hrs_total = (time_m + (time_s / 60)) / 60

avg_speed = dist_miles / hrs_total  # mph

print(f"The average speed is {avg_speed:.2f} mph")

"""
Activity 5: Population Projection
The U.S. Census Bureau projects population based on the following assumptions:

•	One birth every 7 seconds
•	One death every 13 seconds
•	One new immigrant every 45 seconds

Write a program to display the population for each of the next five years. Assume the current population 
is 312,032,486 and one year has 365 days.

Hint: In Java, if two integers perform division, the result is an integer. The fractional part is dropped. 
For example, 5/4 is 1 (not 1.25) and 10/4 is 2 (not 2.5). To get an accurate result with the fractional part, 
one of the values involved in the division must be a number with a decimal point. For example, 5.0/4 is 
1.25 and 10/4.0 is 2.5.

"""
print("\n===Problem 5===\n")
start_pop = 312032486
s_conv = 60 * 60 * 24 * 365  # seconds in a year

i = 1
curr_pop = start_pop
for i in range(i, 6):
    print(f"Year {i} results:")
    deaths = s_conv / 13
    births = s_conv / 7
    imm = s_conv / 45
    net_growth = births + imm - deaths
    curr_pop += curr_pop + net_growth
    print(f"{curr_pop:,.0f}\n")
    i += 1
