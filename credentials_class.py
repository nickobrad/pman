class Credentials:

    accountList = [] 

    def __init__(self, account_name, account_username, account_password):
        self.account_name = account_name
        self.account_username = account_username
        self.account_password = account_password

    def create_account(self):
        '''
        Saves the new account credentials
        '''
        Credentials.accountList.append(self)

    def delete_account(self):
        '''
        Deletes a specific account credential
        '''
        