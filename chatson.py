import requests
import json

url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"

payload = json.dumps({
  "enable_google_results": False,
  "enable_memory": False,
  "input_text": "HI",
  "X-API-KEY": "77976f3d-de79-473d-98a3-27a631c998b6"
})
headers = {
  'X-API-KEY': '77976f3d-de79-473d-98a3-27a631c998b6',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
