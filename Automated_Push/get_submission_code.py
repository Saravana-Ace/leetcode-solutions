import requests
import queries
import json
import os.path
import subprocess
import schedule
import time

with open("user_data.json", "r") as file:
    user_data = json.load(file)

# endpoint to send requests to
url = "https://leetcode.com/graphql"

# get the latest submission id
def get_user_latest_submission(username):
    query = queries.retrieve_latest_submission_id
    data = {
        "query": query,
        "variables": {"username": username}
    }

    response = requests.post(url=url, json=data).json()
    return response["data"]["recentAcSubmissionList"][0]

# get code from leetcode
def get_latest_ac_submission_code(submission_id):
    query = queries.retrieve_latest_submission_code
    data = {
        "query": query,
        "variables": {"submissionId": submission_id}
    }
    cookies = {
        'LEETCODE_SESSION': user_data["leetcode_session_id"]
    }
    response = requests.post(url=url, cookies=cookies, json=data).json()
    return response["data"]["submissionDetails"]["code"]

def write_code_to_file(submission_id, problem_name):
    submission_code = get_latest_ac_submission_code(submission_id)

    with open(f"/Users/saravanapolisetti/Desktop/LeetCode/{problem_name}.py", "w") as file:
        file.write(submission_code)

def check_and_update():
    latest_sub = get_user_latest_submission(user_data["username"])
    submission_id = latest_sub["id"]
    problem_name = latest_sub["title"]

    if not os.path.isfile("prev_id.txt"):
        with open("prev_id.txt", "w") as file:
            file.write(submission_id)
        
        write_code_to_file(submission_id, problem_name)
        
        subprocess.run(["git", "add", "."], cwd="..")
        subprocess.run(["git", "commit", "-m", problem_name], cwd="..")
        subprocess.run(['git', 'push'])

    else:
        with open("prev_id.txt", "r") as file:
            prev_submission_id = file.read()
            
        if submission_id != prev_submission_id:
            with open("prev_id.txt", "w") as file:
                file.write(submission_id)
            
            write_code_to_file(submission_id, problem_name)
            
            subprocess.run(["git", "add", "."], cwd="..")
            subprocess.run(["git", "commit", "-m", problem_name], cwd="..")
            subprocess.run(['git', 'push'])

schedule.every(30).seconds.do(check_and_update)

while True:
    schedule.run_pending()
    time.sleep(1)