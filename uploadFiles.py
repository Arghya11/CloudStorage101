import os 
import dropbox
from dropbox.fles import WriteMode
#
class TransferData:
    def _init_(self,access_token):
        self.access_token = access_token

    def upload_flie(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = oslpath.jion(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.flies_upload(f.read(), dropbox_path, mode=WriteMode("overwrite"))

def main():
    access_token = 'sl.BEeV6aTUlSLQVIGZ9Uw2-6sCb_pnsmn_XM0MP51jHxcpcjtoAFQ1e50vA-88ZJibIXs37fI6YAFaneByGCoFoHo2mYkwnOEhWjpEVpMGXde7lcRAfhjQO4_ZWYbwS6xqaH9i51GN66g'
    tranferData =TransferData(access_token)

    file_from = str(input("Enter the folder path to tranfer : -"))
    file_to = input("enter the full path to upload to dropbox:- ")

    tranferData.upload_file(file_from,file_to)
    print("file has been moved !!!")

main()

