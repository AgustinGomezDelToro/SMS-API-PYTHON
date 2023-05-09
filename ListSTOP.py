# std
import logging
import json
from collections import OrderedDict
 
# 3p
import requests
 
API_KEY = "MY API KEY"
URL = "https://api.smspartner.fr/v1"
 
class SMSPartner():
    def get_list_stop(self):
        # Concaténation de l'URL avec la clé d'API
        url = URL + "/stop-sms/list?apiKey=" + API_KEY

        # Envoi de la requête HTTP GET à l'API SMS Partner
        r = requests.get(url)

        # Récupération de la réponse JSON
        r_json = r.json()

        # Vérification si la récupération de la liste des numéros stop a réussi
        if "success" in r_json and r_json["success"] == True:
            print(r_json)
            status = True
        else:
            print(r_json)
            status = False

        # Retourne le statut de la récupération de la liste des numéros stop
        return status
