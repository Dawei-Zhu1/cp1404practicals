minimum_password_length = 8

user_password = input("Enter your password: ")
while len(user_password) < minimum_password_length:
    print("Password must be at least {} symbols.".format(minimum_password_length))
    user_password = input("Enter your password: ")

print(len(user_password) * "*")