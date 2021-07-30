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
        Credentials.accountList.remove(self)

    def account_verification(text):
        '''
        Verifies if the account is ready
        '''
        for acc in Credentials.accountList:
            if acc.account_username == text:
                return True

        return False

    def search_account(text):
        '''
        Searches for a specific account
        '''
        for acc in Credentials.accountList:
            if acc.account_username == text:
                return acc

    def show():
        '''
        Shows all the accounts stored
        '''
        return Credentials.accountList