import http.client
import json
conn = http.client.HTTPSConnection("api.smspartner.fr")

payload = json.dumps({
"apiKey": "your api key smspartner", #remplacez par votre clé API SMSPartner
"phoneNumbers": "+336xxxxxxxx", #remplacez par votre numéro de téléphone
"sender": "Your sender name",
"gamme": 1,
"message": "Cest un message test PYTHON", #remplacez par votre message
 "webhookUrl": "https://webhook.site/TOKEN" #remplacez TOKEN par votre token webhook.site
})

headers = {
'Content-Type': 'application/json',
'Content-Length': str(len(payload)),
'cache-control': 'no-cache'
}

conn.request("POST", "/v1/send", payload, headers) #Une requête POST est envoyée au serveur SMSPartner avec le chemin d'URL "/v1/send"

res = conn.getresponse() #La réponse est ensuite stockée dans la variable res.

data = res.read() 

print(data.decode("utf-8")) #Cette ligne lit les données de la réponse HTTP.