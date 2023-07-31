import requests
from time import sleep
import json

#gc = gspread.service_account(filename='spry-sequence-357517-d1ca6ab92278.json')
#sh = gc.open_by_key('1NyJzWVc_HXPoMq6UOMml76x53Z1OkjM9qa-IUdY2C64')
#worksheet = sh.get_worksheet(1)

token = '2110681679:AAGNXSVnVJpc-bgYDIDlM8ckc-l_LIVmZSk'
url_base = f'https://api.telegram.org/bot{token}/'

def obter_novas_mensagens(update_id):
    link_requisicao = f'{url_base}getUpdates?timeout=100'
    if update_id:
        link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
    resultado = requests.get(link_requisicao)
    return json.loads(resultado.content)

def responder2(resposta, chat_id):
    link_requisicao = f'{url_base}sendMessage?chat_id={chat_id}&text={resposta}'
    requests.get(link_requisicao)


update_id = None 

while 1 == 1:
    atualizacao = obter_novas_mensagens(update_id)
            
    dados = atualizacao["result"]
    if dados:
        for dado in dados:
            
            update_id = dado['update_id']
            try:
                first_name = dado["message"]['from']['first_name']
                print(dado)        
                
                message_id = dado['message']['message_id']
                mensagem = str(dado["message"]["text"])
                chat_id = dado["message"]["chat"]["id"]
            except:
                mensagem = '0000'
                chat_id = 1154633217
            
            if ('status') in mensagem.lower():    
                resposta = "foi"            
                responder2(resposta, chat_id)
