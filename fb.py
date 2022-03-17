import requests
import credentials as cr

def callSendAPI():

    response = {
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
    "recipient": {"id": cr.jlID},
    "message": response,
    }
    headers = {"content-type": "application/json"}

    url = "https://graph.facebook.com/v2.6/me/messages?access_token=" + cr.pageAccessToken
    r = requests.post(url, json=payload, headers=headers)
#    print(r.text)
