import requests

# Replace 'yourStoredToken' with your actual token value
yourStoredToken = 'yourActualToken'

url = 'https://api.yourservice.com/data'
headers = {
    'Authorization': f'Bearer {yourStoredToken}'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.HTTPError as errh:
    print ("Http Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else", err)



# import requests
# from passheader.py import get_jwt_token

# # Obtain the JWT token using your custom script
# jwt_token = get_jwt_token()

# # Make an HTTP request to an Istio-protected service with the JWT token
# url = "https://your-protected-api.example.com/resource"
# headers = {
#     "Authorization": f"Bearer {jwt_token}"
# }

# response = requests.get(url, headers=headers)
# # Handle the API response here   
