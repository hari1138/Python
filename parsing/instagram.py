import requests
import datetime
import json

def getFollowerCount(accountName):
        response = requests.get('https://www.instagram.com/'+ accountName +'/?__a=1')
        data = response.json()
        followers = data.get("graphql").get("user").get("edge_followed_by").get("count")
        return followers