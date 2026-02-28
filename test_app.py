# This script file to test the application (unit testing)
# Test 1: Calculation and Logic (Functional test)
base = 10
height = 5
area = 0.5 * base * height
print(f"Testing Geometry Logic...")
print(f"The area of the triangle is: {area}")

# Test 2: Error Capture (error handeling)
print("Standard output is working...")
# The following line will cause a traceback error
result = 10 / 0

# Test 3: Environment Check(system info check)
import platform
import sys
print(f"Operating System: {platform.system()}")
print(f"Python Version: {sys.version}")

# Test 4: Loop iteration (recursive)
items = ['Socket', 'Payload', 'Buffer', 'Proxy']
for index, item in enumerate(items):
    print(f"Scanning element {index}: {item}")