import ftplib

server = input("Enter the FTP server address: ")
ftp = ftplib.FTP(server)
ftp.login("anonymous", "")
print("Logged in as anonymous")

try:
    ftp.cwd("/")
    print("Current directory:", ftp.pwd())
    files = ftp.nlst()
    print("Files in current directory:")
    for file in files:
        print(file)
except ftplib.all_errors as e:
    print("Error:", e)
finally:
    ftp.quit()
    