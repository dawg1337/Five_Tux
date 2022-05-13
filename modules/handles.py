import os,requests,json
from utils import messages



def get_handles():
            headers = {
                'Host' : 'runtime.fivem.net',
                'User-Agent' : 'CitizenFX/1',
                'Accept' : '*/*'
            }
            r = requests.get('https://runtime.fivem.net/nui-blacklist.json',headers=headers)
            print(f'{messages.line}')
            print(r.text)
            print(f'{messages.line}')
