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
    def send_sms(self, to, sender, msg):
        # Affiche le numéro de téléphone du destinataire
        print(to)
 
        # Création d'un dictionnaire ordonné contenant la clé d'API, le destinataire, l'expéditeur et le message à envoyer
        data = OrderedDict([
            ("apiKey", API_KEY),
            ("to", to),
            ("from", sender),
            ("message", msg)
        ])
 
        # URL pour envoyer les SMS via l'API SMS Partner
        url = URL + "/vn/send"
 
        # Envoi de la requête HTTP POST à l'API SMS Partner avec les données JSON
        r = requests.post(url, data=json.dumps(data), verify=False)
 
        # Récupération de la réponse JSON
        r_json = r.json()
 
        # Vérification si l'envoi des SMS a réussi
        if r_json.get("success") == True:
            print(r_json)
            status = True
        else:
            print("SMS msg {} not delivered to {}".format(msg, to))
            status = False
 
        # Retourne le statut de l'envoi des SMS
        return status
