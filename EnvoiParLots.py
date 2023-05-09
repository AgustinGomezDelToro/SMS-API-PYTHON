# std
import logging
import json
from collections import OrderedDict

# 3p
import requests

# Clé d'API pour l'envoi de SMS via SMS Partner
API_KEY = "MY API KEY"

# URL de l'API SMS Partner
URL = "https://api.smspartner.fr/v1"

class SMSPartner():
    def send_sms(self, phone_numbers, msg, sender="SMSPartner"):
        # sender = "DEMOSMS"
        print(phone_numbers)

        # Dictionnaire contenant la clé d'API, le nom de l'expéditeur et la liste des SMS à envoyer
        data = {
            "apiKey": API_KEY,
            "sender": sender,
            "SMSList": [
                {"phoneNumber": "06xxxxxxx1", "message": "msg1"},
                {"phoneNumber": "06xxxxxxx2", "message": "msg2"}
            ]
        }

        # URL pour envoyer les SMS en masse via l'API SMS Partner
        url = URL + "/bulk-send"

        # Envoi de la requête HTTP POST à l'API SMS Partner avec les données JSON
        r = requests.post(url, data=json.dumps(data), verify=False)

        # Récupération de la réponse JSON
        r_json = r.json()

        # Vérification si l'envoi des SMS a réussi
        if r_json.get("success") == True:
            print(r_json)
            status = True
        else:
            print("SMS msg {} not delivered to {}".format(msg, phone_numbers))
            status = False

        # Retourne le statut de l'envoi des SMS
        return status
