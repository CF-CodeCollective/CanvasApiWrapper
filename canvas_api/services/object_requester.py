import requests
import json
import canvas_api.objects.user

class object_requester():
    def __init__(self, domain_address: str, access_token: int):
        self.domain_address = domain_address
        self.access_token = access_token
    
    def get_user(self, user_id: str):
        address = self.domain_address + "/users/" + str(user_id)
        print(address)
        result = requests.get(address, headers=dict(Authorization=f"Bearer {self.access_token}"))
        if result.status_code != 200:
            print("Error retrieving user.")
            return result.status_code, result.content
        user = canvas_api.objects.user.user(**json.loads(result.content))
        return result.status_code, user