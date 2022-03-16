from pickletools import uint1
import connector
import sftp
import sys


uInput = sys.stdin.readline()
uInput = uInput.strip()

if __name__ == '__main__':
    if uInput == "altanen":
      sp = connector.SavePictureToDisc()
      sp.save_picture(uInput)

      pp = sftp.SftpConnect()
      pp.sftp_put(uInput)
    else: 
        print("cake!")