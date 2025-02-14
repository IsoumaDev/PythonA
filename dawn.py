from curl_cffi import requests
import json
from time import sleep
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Berear 2056b72d0eb33beb2a6d2d39c67296afa677fc1f271efaf0d84b5d50cd08aee410c07f2f8a6510b58ab067551517964a9b712a207a15ea4f311b2b0364b0fd4ba1c8284075cd9789651e7fe939a050881bdc94d31f93b3e4fee18fd5c0c4460281cb35520757cf6c285c2a51d433c8adc08d5b4ad608ddcf5ed601a0a4b3b7e3a7c733f299bfbc95397723e88d858f08407fae1b80e74a12444548979ce51f854ac18e687cb09b1e782e65b87cfd33b0e4132101d02b36c4c21b2bb19c0adaa9b2c7e4afbb3cd20df567892d616efac2d1a325711614ee09dc656483d136a9198de73cbf200dc6b6efb96b73a9f773d9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'chrome-extension://fpdkjdnhkakefebpekbdhillbhonfjjp',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
}

params = {
    'appid': '67aeca354afe13af233c47b8',
}

# response = requests.get('https://www.aeropres.in/api/atom/v1/userreferral/getpoint', params=params, headers=headers,impersonate="chrome124")
# print(response.text)


data =  {
    'username':'keoviewtub@gmail.com',
    'extensionid':'fpdkjdnhkakefebpekbdhillbhonfjjp',
    'numberoftabs':0,
    '_v':'1.1.3'
}
headers = {
    'authorization': 'Berear 2056b72d0eb33beb2a6d2d39c67296afa677fc1f271efaf0d84b5d50cd08aee410c07f2f8a6510b58ab067551517964a9b712a207a15ea4f311b2b0364b0fd4b8c018a29840e14d0c347be7642ad93902b324a08767bc55c72bda83ecf4b5b8482e76babf3aed5ee423fd27b42bb8cb3396522b7a073e2f1ae244f087e5502847774e959bffb4a12cdd6d08d597dd58581b719b02213b37636b4774a4218e80aa3ff4c4d69310fc8cb8568bfa5435471c348f2c5f3605b8221f10584481e173681eb045d2c6035f9f4d624f289b48678f122d7a8f0d4e1741c509073776c93481dca7d4cb04330d4d61f170c6404728f',
    'content-type': 'application/json',
}
while True:
    response = requests.post('https://www.aeropres.in/chromeapi/dawn/v1/userreward/keepalive?appid=',params=params,data=json.dumps(data),headers=headers)
    print(response.text)
    sleep(5)
