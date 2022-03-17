import connector
import sftp
import sys
from connector import SavePictureToDisc as sp
from sftp import SftpConnect as sf

uInput = sys.stdin.readline()
uInput = uInput.strip()

if __name__ == '__main__':
   
    if uInput == "altanen":
      sp.save_picture()
      sf.sftp_put()

    elif (uInput == "pergolan"): 

      sp.save_picture()
      sf.sftp_put()
      
    else: 
      print("Something went wrong!")