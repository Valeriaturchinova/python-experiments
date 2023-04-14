print("I'm calculator")
 
first = input("Enter first number: ")
second: str = input("Enter second number: ")
 
result: int = int(first) + int(second)
 
# Result: 4
print('Result:' + str(result))
 
# Result of first + second: 4
print("Result" + " of " + first + " + " + second + ": " + str(result))
print("Result of " + first + " + " + second + ": " + str(result))
 
# Result of '2' + '2' = '4'
print("Result of " + "'" + first + "'" + " + " + "'" + second + "'" + ": " + "'" + str(result) + "'")
print("Result of '" + first + "' + '" + second + "': '" + str(result) + "'")
 
print(f"Result of '{first}' + '{second}': '{result}'")
 
 
# first = 5
# second = 3
# Result of '3' + '5' === '8'
# Result of 8 = '3' + '5'

print("Result of '" + first + "' + '" + second + "' === '" + str(result) + "'")

print("Result of " 
      + str(result) + " = '" + second + "' + '" + first + "'")
# '5' + '3' = '3' + '5' = '8'
print("'" + first + "' + '" + second + "' = '" + second + "' + '" + first + "' = '" + str(result) + "'")
print(f"'{first}' + '{second}' = '{second}' + '{first}' = '{result}'")
print(f"Result of {result} = '{second}' + '{first}'")
print(f"Result of {result + result} = '{second}' + '{first}'")
print(f"Result of {int(first) + int(second)} = '{second}' + '{first}'")
print(f"Result of {result - result} = '{int(second) - int(second)}' + '{int(first) - int(first)}'")