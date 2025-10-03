def changeToLower(string):
    return string.lower()
def changeToUpper(string):
    return string.upper()

def discardWhiteSpaceFromRight(string):
    return string.rstrip()
def discardWhiteSpaceFromLeft(string):
    return string.lstrip()
def discardWhiteSpaceFromBothSides(string):
    return string.strip()

# contoh penggunaan
text = "Hello, World!"
print(changeToLower(text))  # Output: hello, world!
print(changeToUpper(text))  # Output: HELLO, WORLD!

text_with_spaces = "   Hello, World!   1"
print(discardWhiteSpaceFromRight(text_with_spaces))  # Output: "   Hello, World!"
print(discardWhiteSpaceFromLeft(text_with_spaces))   # Output: "Hello, World!   "
print(discardWhiteSpaceFromBothSides(text_with_spaces))  # Output: "Hello, World!"
