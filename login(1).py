# Predefined username and password
correct_username = "admin"
correct_password = "1234"

attempts = 3

while attempts > 0:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful ")
        break
    else:
        attempts -= 1
        print("Invalid Username or Password ")
        print("Attempts left:", attempts)

if attempts == 0:

    print("Account Locked  Too many failed attempts.")
