print("Hello World!".islower())  # False
print("hello world!".islower())  # True

print("Hello World!".isupper())  # False
print("HELLO WORLD!".isupper())  # True

print("HelloWorld".isalpha())  # True
print("Hello World".isalpha())  # False (ada spasi)

print("Hello123".isalnum())  # True
print("Hello 123".isalnum())  # False (ada spasi)