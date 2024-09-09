import requests
import json
import canvas_api.objects.user

class object_requester():
    def __init__(self, domain_address: str, access_token: int):
        self.domain_address = domain_address
        self.access_token = access_token
        self.auth_header = dict(Authorization=f"Bearer {self.access_token}")
    
    def get_user(self, user_id: str):
        address = self.domain_address + "/users/" + str(user_id)
        result = requests.get(address, headers=self.auth_header)
        if result.status_code != 200:
            print("Error retrieving user.")
            return result.status_code, result.content
        user = canvas_api.objects.user.user(**json.loads(result.content))
        return result.status_code, user
    
    def course_get_students(self, course_id: int):
        address = self.domain_address + f"/courses/{course_id}/students"
        result = requests.get(address, headers=self.auth_header)
        if result.status_code != 200:
            print("Error retrieving course students")
            return result.status_code, result.content
        users = json.loads(result.content)
        users = [canvas_api.objects.user.user(**user) for user in users]
        return result.status_code, users
