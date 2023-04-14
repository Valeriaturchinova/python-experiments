# -
# ' ' внешние 
# "" - внутренние

print("I'm calculator")
 
first = input("Enter first number: ")
second: str = input("Enter second number: ")
 
result: int = int(first) - int(second)
 
# Result: 10
print('Result:' + str(result))
 
# Result of first - second: 10
print("Result" + " of " + first + " - " + second + ": " + str(result))
print("Result of " + first + " - " + second + ": " + str(result))
 
# Result of "15" - "5" = "10"
print('Result of ' + '"' + first + '"' + ' - ' + '"' + second + '"' + ': ' + '"' + str(result) + '"')
print('Result of "' + first + '" - "' + second + '": "' + str(result) + '"')
 
print(f'Result of "{first}" - "{second}": "{result}"')
 
 
# first = 15
# second = 5
# Result of "5" - "15" === "-10"
# Result of 10 = "15" - "5"

print('Result of "' + first + '" - "' + second + '" === "' + str(result) + '"')

print('Result of ' + str(result) + ' = "' + first + '" - "' + second + '"')
# "15" - "5" = "10"
print('"' + first + '" - "' + second + '" = "' + str(result) + '"')
print(f'"{first}" - "{second}" = "{result}"')

