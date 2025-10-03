x : list = ["laptop", "mouse", "keyboard" , "monitor" , "printer" , "speaker" , "webcam" , "headset" , "router" , "external hard drive"]
my_info : dict = {
    "name": "Alice",
    "age": 25,  
    "city": "Wonderland"
}
print(x)

print(x[2])
print(x[-1])
print(x[::2])

my_info["name"] = "Bob"
my_info["job"] = "Engineer"
del my_info["age"]
print(my_info)
print(my_info["name"])
