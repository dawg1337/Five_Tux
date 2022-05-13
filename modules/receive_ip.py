from http import client
from re import I
from time import sleep
import requests,json
from utils import messages

headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
            "sec-ch-ua": '"Chromium";v="96", "Opera GX";v="82", ";Not A Brand";v="99"',
	        "origin": "https://servers.fivem.net",
	        "referer": "https://servers.fivem.net/",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.25"
}

def receive_ip(ip): #eg 8xyke4
    print(f'{messages.title} Retreiving IP...')
    sleep(2)
    r = requests.get(f'https://servers-frontend.fivem.net/api/servers/single/' + ip,headers=headers)
    print(f'{messages.line}')
    Endpoint = r.json()["Data"]["connectEndPoints"][0]
    EndpointCFX = r.json()['EndPoint']
    Maxclients = r.json()["Data"]["svMaxclients"]
    sv_gamebuild = r.json()["Data"]["vars"]['sv_enforceGameBuild']
    sv_desc = r.json()['Data']['vars']['sv_projectDesc']
    sv_origin = r.json()['Data']['server']
    sv_clients = r.json()['Data']['clients']
    sv_avat = r.json()['Data']['ownerAvatar']
    #Clients = r.json()['clients']
    print(f'{messages.title} ServerIP {messages.arrow} {Endpoint} Confirmed: {messages.checkmark}' )
    sleep(1)
    print(f'{messages.title} CFX-Endpoint {messages.arrow} {EndpointCFX} Confirmed: {messages.checkmark}')
    print(f'{messages.title} MaxClients {messages.arrow} {Maxclients} Confirmed: {messages.checkmark}')
    print(f'{messages.title} GameBuild {messages.arrow} {sv_gamebuild} Confirmed: {messages.checkmark}')
    print(f'{messages.title} Description {messages.arrow} {sv_desc} Confirmed: {messages.checkmark}')
    print(f'{messages.title} Origin {messages.arrow} {sv_origin} Confirmed: {messages.checkmark}')
    print(f'{messages.title} Online Players {messages.arrow} {sv_clients} Confirmed: {messages.checkmark}')
    print(f'{messages.line}')
    print(f'{messages.title} Server Owner {messages.title}' )
    print(f'{messages.title} {messages.arrow} Avatar: {messages.arrow} {sv_avat}')