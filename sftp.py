import pysftp
import credentials as cr

class SftpConnect:

    def sftp_connect():
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None

        sftp_conn = pysftp.Connection(host=cr.host, port=cr.port, username=cr.username, password=cr.password, cnopts=cnopts) # "cr." gets the correct host, port and so on
        return sftp_conn

    def sftp_put():
        localFilePath = cr.localFilePath                    # path to the local folder where it will get at picture
        remoteFilePath = cr.remoteFilePath                  # path the the remote folder where the picture will be put
        sftp_conn = SftpConnect.sftp_connect()
        sftp_conn.put(localFilePath, remoteFilePath)
        sftp_conn.close()