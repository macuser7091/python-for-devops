import requests
import json

api_url = "https://api.github.com/users/macuser7091"

response = requests.get(url=api_url)

required_data_key = ["login", "id", "name", "bio", "email", "location", "public_repos", "url", "twitter_username", "user_view_type", ""]

def user_data():
    data = response.json()
    output_list = []
    for key, value in data.items():
       if key in required_data_key:
           output_list.append(f"{key} -- {data.get(key)}")

    with open('data.json', 'w') as f:
        json.dump(output_list, f, indent=4)

    for data in output_list:
        print(data)
       
          
def server_response():
    if response.status_code == 200:
        user_data()
    else:
        print(f"Server ne aapke liye error code bheja hai - {response.status_code}")

server_response()



