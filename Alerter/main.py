import requests
from slacker import Slacker
import json 

json_data = {}

with open("token.json", "r", encode="cp494") as json_file:
    json_data = json.load(json_file)

print(json_data)
url = "https://fear-and-greed-index.p.rapidapi.com/v1/fgi"

headers = {
    'x-rapidapi-host': "fear-and-greed-index.p.rapidapi.com",
    'x-rapidapi-key': "af570ed540msh7f232a60dd5ddd5p1d2889jsne6b3fa11b4df"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

def slack_data() :
    df_slack = df.to_csv(file_name + '.csv',encoding = 'euc-kr') 
    token = ''
    slack = Slacker(token)
    slack.files.upload(file_name + '.csv',channels='#channels')

# slack_data()