import requests
import credentials as cr

def callSendAPI():

    response = {                                                                            # response takes the remote url to the picture plus a text and sents it to me 
        "attachment":{
            "type":"template",
                "payload":{
                "template_type":"button",
                "text": f"Det är någon vid {cr.fbText}.",
                "buttons":[{
                    "type": "web_url",
                    "url": f"{cr.remoteUrl}",
                    "title": "Se vem det är!",
                }]
            }
        }
    }
    payload = {
    "recipient": {"id": cr.jlID},                                                           # facebook pid to me 
    "message": response,
    }
    headers = {"content-type": "application/json"}

    url = "https://graph.facebook.com/v2.6/me/messages?access_token=" + cr.pageAccessToken  # url and access token for the call 
    r = requests.post(url, json=payload, headers=headers)
#    print(r.text)
