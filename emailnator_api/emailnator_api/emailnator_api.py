"""Main module."""
import requests
import json
from urllib.parse import unquote
class EmailnatorAPI:
    
    def __init__(self, proxy=None):
        self.session = requests.Session()

        self.proxy = proxy
        self.email = ""
        r = self.session.get("https://www.emailnator.com")#, proxy=self.proxy)
        csrf_token = unquote(r.cookies.get('XSRF-TOKEN'))

        self.session.headers["Authorization"] = f"Bearer {unquote(r.cookies['XSRF-TOKEN'])}"
        self.session.headers["X-XSRF-TOKEN"] = csrf_token
    def get_email(self):
        headers = {
            'authority': 'www.emailnator.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.emailnator.com',
            'pragma': 'no-cache',
            'referer': 'https://www.emailnator.com/',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        json_data = {
            'email': [
                'dotGmail',
            ],
        }
        url = 'https://www.emailnator.com/generate-email'

        generate_email = self.session.post(url, headers=headers, json=json_data)#, proxy=self.proxy)

        # json_dump = json.loads(generate_email.text) # I JUST SAW THIS AND WHAT THE FUCK
        json_dump = generate_email.json()

        self.email = json_dump["email"][0]

        return self.email

    def get_inbox(self):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://www.emailnator.com',
            'Referer': 'https://www.emailnator.com/inbox/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
        }
        json_data = {
            'email': self.email,
        }
        response = self.session.post('https://www.emailnator.com/message-list', headers=headers, json=json_data)#, proxy=self.proxy)

        return response.json()
    
    def get_message(self, message_id):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://www.emailnator.com',
            'Referer': 'https://www.emailnator.com/inbox/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
        }
        
        json_data = {
            'email': self.email,
            "messageID": message_id
        }
        response = self.session.post('https://www.emailnator.com/message-list', headers=headers, json=json_data)#, proxy=self.proxy)

        return response.text