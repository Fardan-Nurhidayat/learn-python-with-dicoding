def mergeString(string , separator):
    return separator.join(string)
def splitString(string):
    return string.split()
# contoh penggunaan 
print(mergeString(["Hello", "World"], ", "))  # Output: Hello, World
print(mergeString(["2023", "10", "05"], "-"))  # Output: 2023-10-05

print(splitString("Hello World from Python"))  # Output: ['Hello', 'World', 'from', 'Python']
print(splitString("2023-10-05"))  # Output: ['2023-10-05']