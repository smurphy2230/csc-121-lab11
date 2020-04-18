int_list = []

for i in range(5):
    try:
       user_input = int(input("Enter an integer: "))
    except:
        print("Input value cannot be converted to an integer.")
    else:
        user_input = user_input
        int_list.append(user_input)
print("Integer list: ", int_list)
