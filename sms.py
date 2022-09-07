from time import sleep
from bs4 import BeautifulSoup
import requests

while True:
    sleep(1)
    cookies =  {
    '_uc_referrer': 'https://www.bing.com/',
    '_pbjs_userid_consent_data': '3524755945110770',
    'ts': '1662534792',
    }

    headers = {
    'authority': 'receivesms.cc',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_uc_referrer=https://www.bing.com/; _pbjs_userid_consent_data=3524755945110770; ts=1662534792',
    'referer': 'https://receivesms.cc/sms/13478188349',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}

    url = 'https://receivesms.cc/sms/13478188349'

    req = requests.post(url, cookies=cookies, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    html = soup.findAll('ul')[3:4]

    for txt in html:
       print(txt.text)

        

    

   
    



    

 




