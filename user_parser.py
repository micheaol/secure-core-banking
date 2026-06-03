# # API_KEY="Super-secret-key"

# # # List
# # users = [
# #     "Administrator",
# #     "admin",
# #     "guest",
# #     "test"
# # ]

# # # for user in users:
# # #     # print(f"Testing {user}")


# # # Dictionary
# # user = {
# #     "username":"Michael",
# #     "email":"test@gmail.com",
# #     "role":"admin"
# # }

# # user["is_active"] = True

# # # for key,value in user.items():
# # #     print(value)

# # # Turple: Once created, they cannot be changed.
# users = [
#     {
#         "username": "john",
#         "role": "user",
#         "active": True
#     },
#     {
#         "username": "admin",
#         "role": "administrator",
#         "active": True
#     },
#     {
#         "username": "guest",
#         "role": "user",
#         "active": False
#     },
#     {
#         "username": "backup_admin",
#         "role": "administrator",
#         "active": False
#     }
# ]

# for user in users:
#     if user["active"]:
#         print(f"active_user {user["username"]}")

# for user in users:
#     if user["role"] == "administrator":
#         print(user["username"])

# active_user = 0
# for user in users:
#     if user["active"]:
#         active_user +=1

# print(active_user)

api_response = {
    "users": [
        {
            "username": "john",
            "role": "user"
        },
        {
            "username": "admin",
            "role": "administrator"
        }
    ]
}

for key,value in api_response.items():
    for user in value:
        if user["role"] == "administrator":
            print(f"admin_user: {user["username"]}")