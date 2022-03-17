import requests
import credentials as cr
class SavePictureToDisc:

    def save_picture():
        localUrlCred = cr.localUrlCred
        localFilePath = cr.localFilePath
        r = requests.get(localUrlCred, allow_redirects = True)
        open(localFilePath, "wb").write(r.content)