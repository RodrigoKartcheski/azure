# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:18:47 2023

@author: Rodrigo
"""

import requests
import os
#import dotenv


########### fim ##############################
new_list = []
list_doc_workspaces = []


########### inicio ##############################
#Carrega variaveis de ambiente
#load_dotenv()
dotenv.load_dotenv(dotenv.find_dotenv())
# Gera o Token para fazer conexão no ambiente
def generate_token():
    url_token = "https://login.microsoftonline.com/a886859c-9933-4215-b77b-325e24126235/oauth2/token"
    
    data_get_token = {
        'client_Id': os.getenv("client_Id"),
        'client_secret': os.getenv("client_secret"),
        'grant_type': 'client_credentials',
        'resource': 'https://analysis.windows.net/powerbi/api'
    }

    r_get_token = requests.post(url_token, data=data_get_token)

    if r_get_token.status_code == 200:
        res_get_token = r_get_token.json()
        print('Não foi possível resgatar o valor do TOKEN...')

        if res_get_token.get('error_description') is not None:
            print('Não foi possível resgatar o valor do TOKEN...')
            return False
        
        # print('TOKEN gerado com sucesso!')
        #return res_get_token.get('access_token')
        t = "aaasa"
    return r_get_token


p = generate_token()
print(p)
