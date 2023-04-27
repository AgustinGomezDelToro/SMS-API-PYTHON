Ce code permet d'envoyer un message SMS en utilisant l'API de SMSPartner en Python.

La première étape consiste à importer les bibliothèques http.client et json. Ensuite, une connexion est établie avec le serveur de SMSPartner à travers la ligne conn = http.client.HTTPSConnection("api.smspartner.fr").

Ensuite, un objet JSON est créé pour contenir les informations du message à envoyer. Les informations comprennent la clé API, le numéro de téléphone du destinataire, le nom de l'expéditeur, la gamme (niveau de qualité) du message, le contenu du message et l'URL de rappel (webhook) pour les notifications.

Les en-têtes HTTP sont également spécifiés pour indiquer que le contenu est au format JSON et pour indiquer la longueur du contenu.

La requête HTTP est ensuite envoyée à l'aide de la méthode conn.request("POST", "/v1/send", payload, headers). La réponse est ensuite stockée dans la variable res.

Enfin, la réponse est lue et affichée à l'aide de data.decode("utf-8").

Il est important de remplacer les champs apiKey, phoneNumbers et sender par les informations correspondantes pour pouvoir utiliser ce code avec succès.
#   S M S - A P I - S M S P A R T N E R - P Y T H O N  
 