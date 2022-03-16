import requests
import credentials
class SavePictureToDisc:

    def save_picture(self, camera):
        url = credentials.localUrlCred
        picSave = f"/home/pi/ToMessenger/{camera}.jpg"
#        picSave = f"C:/Users/Jonathan/Pictures/altanen.jpg"
        r = requests.get(url, allow_redirects = True)
        open(picSave, "wb").write(r.content)
