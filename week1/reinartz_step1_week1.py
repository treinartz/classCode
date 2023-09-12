#DrR data week1--Runestone
#1--100% me!
print(5 ** 2)
print(9 * 5)
print(15 / 12)
print(12 / 15)
print(15 // 12)
print(12 // 15)
print(5 % 2)
print(9 % 5)
print(15 % 12)
print(12 % 15)
print(6 % 6)
print(0 % 7)

#3--80% me!
current_time_string = input("What is the current time (in hours)? ")
waiting_time_string = input("How many hours do you have to wait? ")

current_time_int = int(current_time_string)
waiting_time_int = int(waiting_time_string)

hours = current_time_int + waiting_time_int
timeofday = hours % 24

print(timeofday)

#5--100%!
word1 = "All"
word2 = "work"
word3 = "and"
word4 = "no"
word5 = "play"
word6 = "makes"
word7 = "Jack"
word8 = "a"
word9 = "dull"
word10 = "boy."
print(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10)

#7--70% me!
P = 10000
n = 12
r = 0.08

t = int(input("Compound for how many years? "))
final = P * ( ((1 + (r/n)) ** (n * t)) )

print ("The final amount after", t, "years is", final)

#9 100% me!
width = int(input("Width? "))
height = int(input("Height? "))
area = width * height
print("The area of the rectangle is", area)

#11--100% me!
deg_c = int(input("What is the temperature in Celsius? "))
# formula to convert C to F is: (degrees Celcius) times (9/5) plus (32)
deg_f = deg_c * (9 / 5) + 32
print(deg_c, " degrees Celsius is", deg_f, " degrees Farenheit.")

#######################skill-builders

#1. area_of_circle
import math
radius = float(input("What is the radius? "))
area = math.pi * radius ** 2
print("The area of the circle is", area)









#2.  weight_on_mars
weight_on_earth = float(input("Enter the weight of the item in pounds: "))
weight_on_mars = round(weight_on_earth * 0.38, 2)
print(f"The weight of the item on Mars is {weight_on_mars} pounds.")








#3. pizza_price
diameter = float(input("Enter the diameter of the pizza in inches: "))
price = float(input("Enter the price of the pizza in dollars: "))

radius = diameter / 2
area = math.pi * radius ** 2
cost_per_square_inch = price / area

print(f"The cost per square inch of the pizza is ${cost_per_square_inch:.2f}")










#4 Eggs in Cartons
num_eggs = int(input("How many eggs do you have? "))
num_full_cartons = num_eggs // 12
num_eggs_in_last_carton = num_eggs % 12

print("You need", num_full_cartons, "full cartons and", num_eggs_in_last_carton, "eggs in the last carton.")
