"""

Simple API call script that returns DBZ characters!

"""

#import requests library
import requests
from requests.auth import HTTPBasicAuth
import pprint

#Creates a globabl variable that defines our URL string

URL = "https://dragon-ball-api.herokuapp.com/api/character/Goku" 
#Creates dictionary for the payload data and header information

payload = {}
header = {'Accept': 'application/json'}

#Creates variable response and stores the HTTP GET response using the requests
#library to make the API call and passing it the URL variable value, headers, and payload information

response = requests.get(URL, headers=header, data=payload)

#creates a variable labelled character storing our response variable in JSON format
#and filters out just the value tied to the key "character"

statusCode = response.status_code

character = response.json()
print("Status_Code is: " + str(statusCode))
pprint.pprint(character)
