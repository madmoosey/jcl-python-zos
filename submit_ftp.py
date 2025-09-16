from ftplib import FTP

host = "mainframe.host"
user = "YOURID"
password = "YOURPASS"

ftp = FTP(host)
ftp.login(user, password)

# Submit JCL from local file
with open("HELLOCLG.jcl", "rb") as jcl:
    ftp.storlines("STOR SUBMIT", jcl)

ftp.quit()
