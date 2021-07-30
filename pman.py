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