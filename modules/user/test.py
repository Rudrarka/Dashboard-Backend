import requests

url = "https://shazam.p.rapidapi.com/auto-complete"

querystring = {"locale":"en-US","term":"kiss the"}

headers = {
    'x-rapidapi-host': "shazam.p.rapidapi.com",
    'x-rapidapi-key': "9837861294msh8d24501459580b3p11cd68jsn2de3aeac522f"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)