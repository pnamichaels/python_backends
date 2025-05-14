
def user_info(firstname, lastname, age):
    user = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }

    return user

firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")
age = input("Please enter your age: ")

user_dict = user_info(firstname, lastname, age)

print(user_info)