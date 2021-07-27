import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def _init_(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)



upload_file function
# enumerate local file recursively 
for root, dris, files in os.walk (file_form):

# construct the full dropbox path 
relative_path = os .path.relpath(locl_path, file form)
dropbox_path = os.path.join(file_to, relative_path)

#upload the files 
with open (local_path, 'rb') as f:
    dbx,files_upload(f,read(), dropbox_path, mode=WriteNode('overwrite'))



def main(): 
    
    access_token = 'sl.AbKQY7cwlr949HZB7JxLOMrnYKuY39PSkiEnMjmzkLJ8mukldzSQjT8oLVfn_A-kB4yn6O0erRD07aV-9JeaGvvRPoLFEVvwg3_p2AufnKjhGlCgTVtpR4YV0SKhk6nbU2-ztZAB' 
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -") 
    file_to = input("enter the full path to upload to dropbox:- ") 
    # This is the full path to upload the file to, including name that you wish the file to be called once uploaded. 
    # # API v2 
    transferData.upload_file(file_from, file_to) 
    print("file has been moved !!!") 
    
main()







