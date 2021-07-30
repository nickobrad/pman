#!/usr/bin/env python3.9

from user_class import User
from credentials_class import Credentials

def create_user(first_name, second_name, username, password):

    newUser = User(first_name,second_name,username,password)
    return newUser

def user_save(user):
    '''
    Saves the newly created user
    '''
    User.save_user(user)

def user_confirm(user):
    '''
    Confirms if ther user exists
    '''
    User.user_verification(user)

def create_account(account_name, account_username, account_password):
    '''
    Creates a new user credential
    '''
    newAccount = Credentials(account_name, account_username, account_password)

def save_account(account):
    '''
    Saves the new account
    '''
    Credentials.create_account(account)

def account_confirm(account):
    '''
    Confirms that there's such an account
    '''
    Credentials.account_verification(account)

def look_for_account(account):
    '''
    Searches for an account
    '''
    Credentials.search_account(account)

def remove_account(account):
    '''
    Deletes an account
    '''
    Credentials.delete_account(account)

def main():
    User.userCredentials = []
    Credentials.accountList = []

    print("Welcome new user. Please input your details to create your account to start using PMAN.")
    print('\n')

    while True:
    
        print("First Name:...")
        f_name = input()
        print('\n')
        print("Second Name:...")
        s_name = input()
        print('\n')
        print("Your PMAN username:...")
        print("Note that this is not your username for your individual accounts")
        u_name = input()
        print('\n')
        print("Password:...")
        pman_password = input()

        new_user = User (f_name, s_name, u_name, pman_password)
        user_save(new_user)
if __name__ == '__main__':
    main()