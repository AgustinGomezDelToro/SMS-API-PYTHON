# std
import logging
import json
from collections import OrderedDict
 
# 3p
import requests
 
API_KEY = "MY API KEY"
URL = "https://api.smspartner.fr/v1"
 
class SMSPartner():
    def add_stop(self, phone_numbers):
        # Vérification que phone_numbers est une chaîne de caractères
        if not isinstance(phone_numbers, str):
            raise TypeError("phone_numbers should be a string")

        # Création d'un dictionnaire ordonné contenant la clé d'API et les numéros de téléphone à stopper
        data = OrderedDict([
            ("apiKey", API_KEY),
            ("phoneNumbers", phone_numbers)
        ])
 
        # URL pour ajouter des numéros de téléphone à la liste stop
        url = URL + "/stop-sms/add"

        # Envoi de la requête HTTP POST à l'API SMS Partner avec les données JSON
        r = requests.post(url, data=json.dumps(data), verify=False)
 
        # Récupération de la réponse JSON
        r_json = r.json()

        # Vérification si l'ajout des numéros de téléphone à la liste stop a réussi
        if "success" in r_json and r_json["success"] == True:
            print(r_json)
            status = True
        else:
            print(r_json)
            status = False

        # Retourne le statut de l'ajout des numéros de téléphone à la liste stop
        return status
