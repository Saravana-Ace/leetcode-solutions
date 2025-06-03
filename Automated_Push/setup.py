import json
import getpass

username = input("Enter your LeetCode username: ")

leetcode_session_id = getpass.getpass("Enter your LeetCode session ID: ")

user_data = {
   "username": username,
   "leetcode_session_id": leetcode_session_id
}

with open("user_data.json", "w") as file:
   json.dump(user_data, file, indent=2)

print("User data saved to user_data.json")