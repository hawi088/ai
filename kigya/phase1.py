# # # print(10//3)

# # user_input =""
# # while user_input != 'quiet':
# #     user_input = input('Enter "quiet" to exit')
# #     print(f"{user_input}")

# while True:
#     try:
#         age = int(input("Enter age: "))
#         if age > 0:
#             break
#         print("Age must be positive")
#     except ValueError:
#         print("Please enter a number")

with open('textFile.txt','r') as file:
    content = file.readlines()
    print(content)
    