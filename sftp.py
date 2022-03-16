import pysftp
import os
import credentials
class SftpConnect:

    def sftp_connect():

        host = credentials.host
        port = credentials.port
        username = credentials.username
        password = credentials.password
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        sftp_conn = pysftp.Connection(host=host, username=username, password=password, cnopts=cnopts)
        print(f"Connection to {host} established!")
        return sftp_conn

    def sftp_put(self, camera):
        localFilePath = f"/home/pi/ToMessenger/{camera}.jpg"
#        localFilePath = f"C:/Users/Jonathan/Pictures/{camera}.jpg"
        remoteFilePath = credentials.serverUrlCred
        sftp_conn = SftpConnect.sftp_connect()
        sftp_conn.put(localFilePath, remoteFilePath)
        sftp_conn.close()
