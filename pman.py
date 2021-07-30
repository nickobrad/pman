#!/usr/bin/env python3.9

from user_class import User
from credentials_class import Credentials
import random
import string

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

        print('--'*20)
        print("Please use your details to now login")
        print('\n')
        print("Username: ")
        userName = input()
        print("Password: ")
        passWord = input()
        for usr in User.userCredentials:
            if usr.username == userName & usr.password == passWord:
                print(f"Welcome {usr.first_name}! What would you like to do?")
                print("To add a new account type na, search for an account type sa and delete and account type da")
                code = input().lower()

                if code == 'na':
                    print("Let's add your account credentials to PMAN")
                    print('--'*20)
                    print('\n')
                    print("Account Name: ")
                    acc_name = input()
                    print("Account Username: ")
                    acc_usrname = input()
                    print("Account Password: ")
                    print("Would you like us to create a password for you or would you like to use your own?")
                    print("Type in 1 to have us generate a password and 2 for you to use yours")
                    code = int(input())

                    if code == 1:
                        acc_pword = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
                        new_Acc = Credentials(acc_name, acc_usrname, acc_pword)
                        save_account(new_Acc)
                        print(f"Your {acc_name} with password {acc_pword} has been created")
                    elif code == 2:
                        acc_pword = input()
                        new_Acc = Credentials(acc_name, acc_usrname, acc_pword)
                        save_account(new_Acc)
                        print(f"Your {acc_name} with password {acc_pword} has been created")
                    else:
                        print("Please choose a number either 1 or 2 to proceed")

                    
if __name__ == '__main__':
    main()