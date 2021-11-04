import requests
response = requests.get("http://api.open-notify.org/astros.json")
print(response.json())
#response.content() # Return the raw bytes of the data payload
#response.text() # Return a string representation of the data payload
response.json()