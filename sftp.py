import pysftp
import credentials
class SftpConnect:

    def sftp_connect():

        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None

        sftp_conn = pysftp.Connection(host=credentials.host,port=credentials.port, username=credentials.username, password=credentials.password, cnopts=cnopts)
        print(f"Connection to {credentials.host} established!")
        return sftp_conn

    def sftp_put():
        
        localFilePath = credentials.localFilePath 
        remoteFilePath = credentials.remoteFilePath
        sftp_conn = SftpConnect.sftp_connect()
        sftp_conn.put(localFilePath, remoteFilePath)
        sftp_conn.close()
