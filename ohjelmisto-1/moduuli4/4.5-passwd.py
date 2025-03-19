# Username and password

# Credentials = user, 1234

uname = "user"
passwd = "1234"

print("Enter credentials")
while True:
    uname_answer = input("username: ")
    passwd_answer = input("password: ")
    if uname_answer == uname and passwd_answer == passwd:
        print("Welcome")
        break
    else:
        print("Access denied")

