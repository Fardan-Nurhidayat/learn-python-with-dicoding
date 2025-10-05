# var_list =  ["Fardan" , "Farhan" , "Alif" , "Gin-Gin"]
# for item in var_list:
#     print(id(item))

# var_arr = [0 for i in range(10)]
# print(var_arr)

# for i in range(10):
#     var_arr[i] = i * 10
# print(var_arr)

var_arr = [1,7,2,89,3]
left_pointer = var_arr[0]
for i in range(len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer
print(left_pointer)
print(max(var_arr))

