'''
Created on

@author: ywkim
'''


import requests.auth

client_auth = requests.auth.HTTPBasicAuth('', '')      #client ID and secret deleted for obvious reasons
post_data = {"grant_type": "password", "username": "semperzen", "password": ""}     #password deleted for obvious reason
headers = {"User-Agent": "ChangeMeClient/0.1 by semperzen"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
print(response.json())


"""

Output:
{'access_token': '102490050456-ogiNx72p9RdPdr5RY6ExeLbPX2k', 
'token_type': 'bearer', 
'expires_in': 3600, 
'scope': '*'}

"""