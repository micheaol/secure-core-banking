# user_parser.py

class User:
    def __init__(self, username, role, is_verified):
        self.username = username
        self.role = role
        self.is_verified = is_verified

    def get_access_summary(self):
        return f"User: {self.username} | Role: {self.role} | Verified: {self.is_verified}"

# Mock data payload (resembles an API output database entry)
raw_users = [
    {"username": "admin", "role": "Administrator", "is_verified": True},
    {"username": "guest_user", "role": "Guest", "is_verified": False},
    {"username": "alice_dev", "role": "Developer", "is_verified": True}
]

# Instantiate class objects using data loop logic
active_profiles = []
for data in raw_users:
    user_obj = User(data["username"], data["role"], data["is_verified"])
    active_profiles.append(user_obj)

# Security Logic: Print access summaries only for verified profiles
print("--- Verified System Profiles ---")
for profile in active_profiles:
    if profile.is_verified:
        print(profile.get_access_summary())