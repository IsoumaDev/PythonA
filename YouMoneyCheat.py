import requests
import time
from bs4 import BeautifulSoup


RawTime = int(time.time()*1000)
TokenTime = RawTime+23
headers = {
    'accept': 'text/plain, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://88bet.bike',
    'referer': 'https://88bet.bike/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

data = {
    'url_order': 'https://88bet.bike/',
    'ref': 'https://www.google.com/',
    'TOP_NUT': '63',
    'LEFT_NUT': '8',
    'NO_NUT': 'NO',
}
url = f'https://traffic-user.net/GET_VUATRAFFIC.php?token={str(TokenTime)},https://88bet.bike/,https://www.google.com/,IOS900,hidden,nullNO&clk={str(RawTime)}'
CodexRes = requests.post(url=url,data=data,headers=headers).text
CodeXN = CodexRes.split("localStorage.codexn = '")[1].split("'")[0]

GetCode = requests.post(
    f'https://traffic-user.net/GET_MA.php?codexn{CodeXN}=&url=https://88bet.bike&loai_traffic=https://www.google.com/&clk={str(RawTime)}',
    headers=headers,
)
GetCodebs4 = BeautifulSoup(GetCode.content, 'html.parser')
Code = GetCodebs4.find(id="layma_me_vuatraffic").get_text()
print('Code của bạn đây:',Code.strip())