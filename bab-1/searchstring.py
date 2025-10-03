def startWith(searchString, targetString):
    return targetString.startswith(searchString)

def endWith(searchString, targetString):
    return targetString.endswith(searchString)

print(startWith("Hello", "Hello, World!"))  # True
print(endWith("Hello!", "Hello, World!"))   # True

