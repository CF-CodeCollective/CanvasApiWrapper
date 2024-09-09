import requests
import urllib.parse
from canvas_api.objects import *
from canvas_api.services import *

class Canvas():
    '''Root class for interacting with the Canvas API'''
    def __init__(self, domain_address: str, access_token: int):
        self.domain_address = domain_address.strip(" /") + "/api/v1"
        self.access_token = access_token

    def raw_get(self, address: str):
        '''Makes a get request at the specified address, returning the result.'''
        return requests.get(address, headers=dict(Authorization=f"Bearer {self.access_token}"))

    def raw_post(self, address: str, data: dict):
        '''Makes a post request at the specified address, passing a dictionary of args, and returning the result.'''
        data_string = ""
        for key, value in dict:
            data_string += f"{key}={value}&"
        data_string = urllib.parse.quote(data_string.strip().rstrip("&"))
        return requests.post(address, headers=dict(Authorization=f"Bearer {self.access_token}"), data=data_string)

    def raw_put(self, address: str, data: dict):
        pass

    def raw_delete(self, address: str, data: dict):
        pass

    def get_object_requester(self):
        return object_requester.object_requester(self.domain_address, self.access_token)
    
    def get_enrollment_service(self):
        return enrollment_service.enrollment_service(self.domain_address, self.access_token)