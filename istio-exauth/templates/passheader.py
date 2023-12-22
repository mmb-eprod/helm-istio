import requests
from passheader.py import get_jwt_token

# Obtain the JWT token using your custom script
jwt_token = get_jwt_token()

# Make an HTTP request to an Istio-protected service with the JWT token
url = "https://your-protected-api.example.com/resource"
headers = {
    "Authorization": f"Bearer {jwt_token}"
}

response = requests.get(url, headers=headers)
# Handle the API response here