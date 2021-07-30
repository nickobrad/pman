class User:
    userCredentials = []

    def __init__(self, first_name, second_name, username, password):
        '''
        These are the properties of the object that will be created when a user signs up
        '''
        self.first_name = first_name
        self.second_name = second_name
        self.username = username
        self.password = password

    def save_user(self):
        '''
        Method saves the user details in the credentials list
        '''
        User.userCredentials.append(self)

    def user_verification(text):
        '''
        Method that confirms there's an actual user
        '''
        for user in User.userCredentials:
            if user.username == text:
                return True
                
        return False

