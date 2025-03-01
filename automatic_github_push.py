import requests
from bs4 import BeautifulSoup
import time

def check_leetcode_submission_status():
    # Create a session to maintain cookies
    session = requests.Session()
    
    # Login to LeetCode (this part is crucial)
    login_url = "https://leetcode.com/accounts/login/"
    
    # Get CSRF token first
    response = session.get(login_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'}).get('value')
    
    # Prepare login data
    login_data = {
        'login': 'saravana.polisetti@gmail.com',  # Replace with your username
        'password': 'n3wAcc0nt123&',  # Replace with your password
        'csrfmiddlewaretoken': csrf_token
    }
    
    # Send login request
    session.post(
        login_url,
        data=login_data,
        headers={'Referer': login_url}
    )
    
    # Now check your submissions page
    submissions_url = "https://leetcode.com/api/submissions/"
    response = session.get(submissions_url)
    
    if response.status_code == 200:
        submissions_data = response.json()
        
        # Look for the most recent submission
        if 'submissions_dump' in submissions_data:
            latest_submission = submissions_data['submissions_dump'][0]
            
            # Check if the submission was successful
            if latest_submission['status_display'] == 'Accepted':
                print(f"Success! Problem: {latest_submission['title']}")
                print(f"Language: {latest_submission['lang']}")
                print(f"Runtime: {latest_submission['runtime']}")
                return True, latest_submission
            else:
                print(f"Submission failed with status: {latest_submission['status_display']}")
                return False, latest_submission
    
    return False, None