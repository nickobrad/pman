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
    return User.user_verification(user)

def create_account(account_name, account_username, account_password):
    '''
    Creates a new user credential
    '''
    newAccount = Credentials(account_name, account_username, account_password)

def add_account(account):
    '''
    Saves the new account
    '''
    Credentials.save_account(account)

def account_confirm(account):
    '''
    Confirms that there's such an account
    '''
    return Credentials.account_verification(account)

def look_for_account(account):
    '''
    Searches for an account
    '''
    return Credentials.search_account(account)

def remove_account(account):
    '''
    Deletes an account
    '''
    Credentials.delete_account(account)

def main():
    User.userCredentials = []
    Credentials.accountList = []

    print("Welcome new user. Please input your details to create your account to start using PMAN.")

    while True:
    
        print("First Name:...")
        f_name = input()
        print("Second Name:...")
        s_name = input()
        print("Your PMAN username:...")
        print("Note that this is not your username for your individual accounts")
        u_name = input()
        print("Password:...")
        pman_password = input()

        new_user = User (f_name, s_name, u_name, pman_password)
        user_save(new_user)

        print('--'*20)

        while True:
            print("Please use your details to now login")
            print('\n')
            print("Username: ")
            userName = input()
            print("Password: ")
            passWord = input()

            for usr in User.userCredentials:
                if ((usr.username == userName) and (usr.password == passWord)):

                    while True:
                        print(f"Welcome {usr.first_name}! What would you like to do?")
                        print("To add a new account type na, search for an account type sa, show all accounts type sc, delete an account type da and to exit type ex")
                        code = input().lower()

                        if code == 'na':
                            print("Let's add your account credentials to PMAN")
                            print('--'*20)
                            print('\n')
                            print("Account Name: ")
                            acc_name = input()
                            for conts in Credentials.accountList:
                                if conts.account_name == acc_name:
                                    print("Name already taken. Add another name!")
                                    print ("Account Name:...")
                                    acc_name = input()

                            print("Account Username: ")
                            acc_usrname = input()
                            print("Account Password: ")
                            print("Would you like us to create a password for you or would you like to use your own?")
                            print("Type in 1 to have us generate a password and 2 for you to use yours")
                            code_p = int(input())

                            if code_p == 1:
                                acc_pword = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
                                new_Acc = Credentials(acc_name, acc_usrname, acc_pword)
                                add_account(new_Acc)
                                print(f"Your {acc_name} with password {acc_pword} has been created")
                                print('\n')
                            elif code_p == 2:
                                acc_pword = input()
                                new_Acc = Credentials(acc_name, acc_usrname, acc_pword)
                                add_account(new_Acc)
                                print(f"Your {acc_name} with password {acc_pword} has been created")
                                print('\n')
                            else:
                                print("Please choose a number either 1 or 2 to proceed")

                        elif code == 'sa':
                            if len(Credentials.accountList) >= 1:
                                print(f"Thank you {u_name} for wanting to search. ")
                                print("The search feature only works with account names.")
                                print("Type in a valid account name and its details will be shown below:")
                                searchTerm = str(input())
                                if account_confirm(searchTerm):
                                    obtainedAcc = look_for_account(searchTerm)
                                    print("--"*20)
                                    print(f"The account {obtainedAcc.account_name} with password {obtainedAcc.account_password}")
                                    print('\n')
                                else:
                                    print("This account doesn't exist!")
                                    print('\n')
                            else:
                                print("You have no accounts saved! Save some to see some.")
                                print('\n')
                        
                        elif code =='sc':
                            print("Your saved accounts are: ")
                            print('--'*20)
                            if len(Credentials.accountList) >= 1:
                                for conts in Credentials.accountList:
                                    print(f"Account Name: {conts.account_name} | Account Username: {conts.account_username} | Account Password: {conts.account_password}")
                                    print("--"*10)
                                print('\n')

                            else:
                                print("You have no accounts!")
                                print('\n')

                        elif code == 'da':
                            print(f"Hello {u_name}. Below is a list of your saved accounts")
                            print("Use the account name to search for the account you would like to delete")

                            for const in Credentials.accountList:
                                print(f"Account Name: {const.account_name}")
                                print(f"Account Password: {const.account_password}")
                                print("--"*10)
                            print('\n')
                            print("Type in below the account you would like to delete.")    
                            searchAccount = str(input())
                            if account_confirm(searchAccount):
                                toBeDeleted = look_for_account(searchAccount)
                                print(f"Your account with name {toBeDeleted.account_name} and username {toBeDeleted.account_username} has been deleted!")
                                print("--" * 20)
                                remove_account(toBeDeleted)
                                print("Your new accounts list is: ")
                                print("--"*10)
                                for list in Credentials.accountList:
                                    print(f"Account Name: {list.account_name}")
                                    print(f"Account Password: {list.account_password}")
                                    print("--"*10)
                            else:
                                print("The Account you entered is not on the list. Please search for a valid account")
                                print('\n')

                        elif code == 'ex':
                            print("Good bye! Thank you!")
                            print("Sign in again to use PMAN")
                            break

                        else:
                            print("Please use a code to use the application!")

                else:
                    print("Please use your username and password")
                    break

if __name__ == '__main__':
    main()