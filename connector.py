import requests
import credentials as cr
class SavePictureToDisc:

    def save_picture():
        localUrlCred = cr.localUrlCred                              # url to the camera to trigger "take a picture"
        localFilePath = cr.localFilePath                            # path to the folder where the picutre is stored 
        r = requests.get(localUrlCred, allow_redirects = True)
        open(localFilePath, "wb").write(r.content)