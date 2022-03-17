import sys
from credentials import Credentials as cr
from connector import SavePictureToDisc as sp
from sftp import SftpConnect as sf
import fb

#uInput = sys.stdin.readline()
#uInput = uInput.strip()

uInput = "altanen"

if __name__ == '__main__':

    if uInput == "altanen":
        cr.Urls(uInput)
        sp.save_picture()
        sf.sftp_put()
        fb.callSendAPI()

    elif (uInput == "pergolan"):
        cr.Urls(uInput)
        sp.save_picture()
        sf.sftp_put()
        fb.callSendAPI()

    else:
        print("Shit happened!")