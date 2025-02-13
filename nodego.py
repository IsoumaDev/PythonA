import requests
import json
import concurrent.futures
from time import sleep
SERVER_URL = "https://nodego.ai/api/user/nodes/ping"

def ping_node(access_token):
    if not access_token:
        print("Missing access token.")
        return
    
    try:
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        data = {"type": "extension"}
        
        response = requests.post(SERVER_URL, headers=headers, json=data)
        print(response.json())
        if response.ok:
            print("Ping successful.")
        else:
            print(f"Ping failed. {response.status_code}")
    except Exception as e:
        print("Error during ping:", e)
def ping_control(access_token):
    while True:
        ping_node(access_token)
        sleep(60)
if __name__ == "__main__":
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IjY0MWRldmVsb3BpbmdAZS1yZWNvcmQuY29tIiwidXNlcklkIjoiNjdhZTIyOTdkMmJmMTllNjg3OTVhMWVhIiwiaWF0IjoxNzM5NDY1MzY3LCJleHAiOjE3NDIwNTczNjd9.f8sdgzI-NslNcoDycR7Neb9R7g0wwqlHjsZodWwdjvg"
    ping_control(access_token)