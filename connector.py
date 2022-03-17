import requests
import credentials
class SavePictureToDisc:

    def save_picture():
        url = credentials.localUrlCred
        localFilePath = credentials.localFilePath
        r = requests.get(url, allow_redirects = True)
        open(localFilePath, "wb").write(r.content)