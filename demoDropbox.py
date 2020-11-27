import dropbox
class Transfer_Data:
    def __init__(self, acces_token):
        self.acces_token = acces_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.acces_token)
        with open(file_from, 'rb')as f:
            dbx.files_upload(f.read(), file_to)

def main():
    acces_token = 'sl.AmUr3deFNccNdM5J4Ojkb3apON7eKkpbBnBx2aRwPPfccLNWxnB_BbKN5L1bWdIKYZap5W9n2qOYKPjucgGk31-2BdCPKOXlfoOB7f50kzSmnoP_MBl2fFC6_BpPre4_nna4GZ0'
    transferData = Transfer_Data(acces_token)
    file_from = 'C:/Users/HP USER/Desktop/White Hat Jr/Python files/demoClass.py'
    file_to = '/Python_stuff_1'
    transferData.upload_file(file_from, file_to)
main()