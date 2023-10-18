"""Task 1"""


# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")
# valid = {"username": "admin", "password": "admin"}

# def authenticate(p_username, p_password, dct):
    
#     if p_username == dct["username"] and p_password == dct["password"]:
        
#         return f"Welcome, {username}"
#     else:
#         return 'Credentials are invalid'
    
# print(authenticate(username, password, valid))


"""Taks 2"""

# import datetime


# def isweekend(date = datetime.datetime.now()):
    
#     if date.weekday() == 5 or date.weekday() == 6:
#         return True
#     else:
#         return False
    
# print(isweekend(datetime.date(2021, 8, 6)))
# print(isweekend(datetime.date(2021, 8, 7)))
# print(isweekend(datetime.date(2021, 8, 8)))
# print(isweekend(datetime.date(2021, 8, 9)))


"""Task 3"""


# import datetime

# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")
# valid = {"username": "admin", "password": "admin"}
# today_1 = datetime.date(2021, 8, 7)
# today_2 = datetime.date(2021, 8, 6)

# def isweekend(date, p_username, p_password, dct):
    
#     if (date.weekday() == 5 or date.weekday() == 6) or (p_username == dct["username"] and p_password == dct["password"]):
#         return f'Welcome, {p_username}'
#     else:
#         return f'Credentials are invalid'


# result = isweekend(today_2, username, password, valid)

# print(result)



"""Task 4"""


# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")

# users = [
#     {
#         "name": "Holly",
#         "password": "hunter"
#     },
#     {
#         "name": "Peter",
#         "password": "pan"
#     },
#     {
#         "name": "Janis",
#         "password": "joplin"
#     }
# ]

# def get_user(p_username, p_password):
    
#     result = None
    
#     for user in users:
#         if (p_username, p_password) == (user['name'], user['password']):
#             result = user
#             return result
#     print('An error occurred. You are not authorized.')
#     return result



#------------------------------------------------------------

# def get_user(p_username, p_password):
#     for user in users:
#         if (p_username, p_password) == (user['name'], user['password']):
            
#             return user
#         else:
#             get_user(user['name'], user['password'])



# if not user:
#     print("An error occurred. You are not authorized.")

# user = get_user(username, password)


"""Task 5"""


username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")


users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan"
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]
def get_user(p_username, p_password):
    
    result = None
    
    for user in users:
        if (p_username, p_password) == (user['name'], user['password']):
            result = user
            return result
    # print('An error occurred. You are not authorized.')
    return result

def show_offers(p_username, p_password):
    
    # if (get_user(p_username, p_password) and get_user(p_username, p_password)['type'] == 'Student') or get_user(p_username, p_password) is None:
        
    #     print('We have great courses to offer you!')
    user = get_user(p_username, p_password)
    
    if (user and user['type'] == 'Student') or not user:
        print('We have great courses to offer you!')
    
    
    
    
show_offers(username, password)