print("I'm calculator")
 
first: str = input("Enter first number: ")
second: str = input("Enter second number: ")

result: int = int(first) * int(second)
 
# Result: 4
print('Result:' + str(result))
print('Result:', str(result))
print('Result:', result)
print('Result:', result, first + second)
# print(x + y, z, x)
print('Result:', result + int(first + second))
print('Result:', result + int(first) + int(second))
# Result of first * second: 4
print("Result" + " of " + first + " * " + second + ": " + str(result))
print("Result of " + first + " * " + second + ": " + str(result))

# ^Result of '2' |*| '2' = '4'
print("^Result of " + "'" + first + "'" + " |*| " + "'" + second + "'" + ": " + "'" + str(result) + "'")
print("^Result of '" + first + "' |*| '" + second + "': '" + str(result) + "'")
 
print(f"Result of '{first}' * '{second}': '{result}'")
out=f"'{first}' * '{second}' = '{result}'"
print(out)
# first = 2
# second = 6
# Result of '2' * '6' === '12'
# Result of 12 = '6' * '2'

print("Result of '" + first + "' * '" + second + "' === '" + str(result) + "'")

print("Result of " + str(result) + " = '" + second + "' * '" + first + "'")
print(str(result) + " = '" + second + "' * '" + first + "'")

# '2' * '6' = '6' * '2' = '12'
print("'" + first + "' * '" + second + "' = '" + second + "' * '" + first + "' = '" + str(result) + "'")
print(f"'{first}' * '{second}' = '{second}' * '{first}' = '{result}'")

