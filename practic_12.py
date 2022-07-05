"""write a python program to get a username from the user that should have alphanumeric characters, then pass that username to function parameter, to display that username"""
username = input("enter your username:\t")
def get_username(usernames):
    if (usernames.isalnum()):
        print(f"Please enter {usernames}")
        
    else:
        print("your username is false")
get_username(username)