import pysftp
import credentials as cr

class SftpConnect:

    def sftp_connect():
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None

        sftp_conn = pysftp.Connection(host=cr.host, port=cr.port, username=cr.username, password=cr.password, cnopts=cnopts)
        return sftp_conn

    def sftp_put():
        localFilePath = cr.localFilePath
        remoteFilePath = cr.remoteFilePath
        sftp_conn = SftpConnect.sftp_connect()
        sftp_conn.put(localFilePath, remoteFilePath)
        sftp_conn.close()

        print(cr.remoteUrl)