"""
Q1) Print the pattern 'JAVA', with each letter composed of smaller letters of the same type (pic provided)
"""
print("===Problem 1===")
inline = f'''
    J     A   V     V   A
    J    A A   V   V   A A
J   J   AAAAA   V V   AAAAA
 J J   A     A   V   A     A    
'''
print(inline)

"""
Q4) Assume a runner runs 14 kilometers in 45 minutes and 30 seconds. 
Write a program that displays the average speed in miles per hour. 
(Note that 1 mile is 1.6 kilometers.)
"""
print("\n===Problem 4===\n")
dist_km = 14
dist_miles = dist_km/1.6
time_m = 45
time_s = 30
time_total = (time_m + (time_s/60))/60  # hours

avg_speed = dist_miles/time_total  # mph

print(f"The average speed is {avg_speed:.2f} mph")

"""
The U.S. Census Bureau projects population based on the following assumptions:
* One birth every 7 seconds
* One death every 13 seconds
* One new immigrant every 45 seconds

Write a program to display the population for each of the next five years. 
Assume the current population is 312,032,486 and one year has 365 days.
"""
print("\n===Problem 5===\n")
start_pop = 312032486
s_conv = 60*60*24*365  # seconds in a year

i = 1
curr_pop = start_pop
for i in range(i,6):
    print(f"Year {i} results:")
    deaths = s_conv/13
    births = s_conv/7
    imm = s_conv/45
    net_growth = births + imm - deaths
    curr_pop += curr_pop + net_growth
    print(f"{curr_pop:,.0f}\n")
    i += 1





