import requests

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
        data_string = data_string.strip().rstrip("&")
        return requests.post(address, headers=dict(Authorization=f"Bearer {self.access_token}"), data=data_string)

    def raw_put(self, address: str, data: dict):
        pass

    def raw_delete(self, address: str, data: dict):
        pass