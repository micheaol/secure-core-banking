# # # API_KEY="Super-secret-key"

# # # # List
# # # users = [
# # #     "Administrator",
# # #     "admin",
# # #     "guest",
# # #     "test"
# # # ]

# # # # for user in users:
# # # #     # print(f"Testing {user}")


# # # # Dictionary
# # # user = {
# # #     "username":"Michael",
# # #     "email":"test@gmail.com",
# # #     "role":"admin"
# # # }

# # # user["is_active"] = True

# # # # for key,value in user.items():
# # # #     print(value)

# # # # Turple: Once created, they cannot be changed.
# # users = [
# #     {
# #         "username": "john",
# #         "role": "user",
# #         "active": True
# #     },
# #     {
# #         "username": "admin",
# #         "role": "administrator",
# #         "active": True
# #     },
# #     {
# #         "username": "guest",
# #         "role": "user",
# #         "active": False
# #     },
# #     {
# #         "username": "backup_admin",
# #         "role": "administrator",
# #         "active": False
# #     }
# # ]

# # for user in users:
# #     if user["active"]:
# #         print(f"active_user {user["username"]}")

# # for user in users:
# #     if user["role"] == "administrator":
# #         print(user["username"])

# # active_user = 0
# # for user in users:
# #     if user["active"]:
# #         active_user +=1

# # print(active_user)

# api_response = {
#     "users": [
#         {
#             "username": "john",
#             "role": "user"
#         },
#         {
#             "username": "admin",
#             "role": "administrator"
#         }
#     ]
# }
# # 1. Where does parameter come from?

# # User?

# # API?

# # Database?

# # Third party?
# def is_admin(users):
#     for key,value in users.items():
#         for user in value:
#             if user["role"] == "administrator":
#                 print(f"admin_user: {user["username"]}")


# is_admin(api_response)
# # def greet_user(name):
# #     print(f"Hello, {name}")

# # greet_user("Michael")

# # def create_user(username, role):
# #     print(role)
# #     print(username)

# # create_user("Michael", "admin")

# Class
# class User:
#     def __init__(self, username, role):
#         self.role = role
#         self.username = username
#     def greet(self):
#         print(f"Welcome {self.username}")


# user_1 = User("michael", "admin")



# user_1.greet()

# Encapsulation
class AccountBalance:
    def __init__(self):
        self._balance = 1000
    
    def get_balance(self):
        return self._balance


account_balance = AccountBalance()
account_balance._balance = 2000000
print(account_balance.get_balance())
