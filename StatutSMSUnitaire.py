# std
import logging
import json
from collections import OrderedDict
 
# 3p
import requests
 
API_KEY = "MY API KEY"
URL = "https://api.smspartner.fr/v1"
 
class SMSPartner():
    def get_delivery(self, phone_numbers, message_id):
        # Vérification que phone_numbers et message_id sont des chaînes de caractères
        if not isinstance(phone_numbers, str) or not isinstance(message_id, str):
            raise TypeError("phone_numbers and message_id should be strings")

        # Concaténation de l'URL avec les arguments passés à la méthode
        url = URL + "/message-status?apiKey=" + API_KEY + "&phoneNumber=" + phone_numbers + "&messageId=" + message_id

        # Envoi de la requête HTTP GET à l'API SMS Partner
        r = requests.get(url)

        # Récupération de la réponse JSON
        r_json = r.json()

        # Vérification si la récupération des informations de livraison a réussi
        if r_json.get("success") == True:
            print(r_json)
            status = True
        else:
            print(r_json)
            status = False

        # Retourne le statut de la récupération des informations de livraison
        return status
