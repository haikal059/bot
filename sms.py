from time import sleep
import requests
from bs4 import BeautifulSoup


cookies = {
    '_ga': 'GA1.2.2021142155.1659227818',
    '__gads': 'ID=2921c594f2561082-22dd80e697d400b3:T=1659227819:RT=1659227819:S=ALNI_MbVkkkYiET2sW7DtzWUmo0UFQR9fg',
    '__gpi': 'UID=00000822b8942ee6:T=1659227819:RT=1659227819:S=ALNI_MaDAoqMlaYbrO9IlQvJ9XlK169GCQ',
    '_ga_LLL30FE8DG': 'GS1.1.1659227818.1.1.1659227924.0',
    'PHPSESSID': 'utseppt2qm6osgpq2nhdf79rvg',
    'phps': '1662430121',
}


headers = {
    'authority': 'receive-smss.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_ga=GA1.2.2021142155.1659227818; __gads=ID=2921c594f2561082-22dd80e697d400b3:T=1659227819:RT=1659227819:S=ALNI_MbVkkkYiET2sW7DtzWUmo0UFQR9fg; __gpi=UID=00000822b8942ee6:T=1659227819:RT=1659227819:S=ALNI_MaDAoqMlaYbrO9IlQvJ9XlK169GCQ; _ga_LLL30FE8DG=GS1.1.1659227818.1.1.1659227924.0; PHPSESSID=utseppt2qm6osgpq2nhdf79rvg; phps=1662430121',
    'referer': 'https://receive-smss.com/sms/15714788202/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}



while True:
    sleep(2)
    url = 'https://receive-smss.com/sms/15714788202/'
    res = requests.get(url, cookies=cookies, headers=headers)
    
    soup = BeautifulSoup(res.content, 'html.parser')
    
    

    sms = soup.findAll('tr')[2:3]

    for el in sms:
        print(el.text)
        
        

    

   
    



    

 




