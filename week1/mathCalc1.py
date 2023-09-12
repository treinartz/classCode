'''
F-strings were introduced in Python 3.6 and provide a concise and convenient way to create strings with dynamic content.
You can include variables, expressions, or function calls inside f-strings, and Python will automatically replace them
with their values when youevaluate the string.
'''
# Addition
num1 = 10
num2 = 5
sum_result = num1 + num2
print(f"Addition: {num1} + {num2} = {sum_result}")

# Subtraction
num3 = 15
num4 = 7
difference_result = num3 - num4
print(f"Subtraction: {num3} - {num4} = {difference_result}")

# Multiplication
num5 = 8
num6 = 4
product_result = num5 * num6
print(f"Multiplication: {num5} * {num6} = {product_result}")

# Division
num7 = 20
num8 = 4
division_result = num7 / num8
print(f"Division: {num7} / {num8} = {division_result}")

# Exponentiation
base = 2
exponent = 3
power_result = base ** exponent
print(f"Exponentiation: {base} raised to the power of {exponent} = {power_result}")

# Modulus (Remainder)
dividend = 15
divisor = 7
remainder_result = dividend % divisor
print(f"Modulus (Remainder): {dividend} % {divisor} = {remainder_result}")
