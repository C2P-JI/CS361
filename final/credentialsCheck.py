import time

# import current user login database
with open('user_login.txt', 'r') as f:
    lines = f.read().split('\n')  # usernames and passwords separated by lines in text file
authorizedUsers = {}  # initialize empty dictionary of credentials
index = 1  # initialized to track line number
for line in lines:
    if index % 2 != 0:  # usernames stored on odd-numbered lines
        key = line
    else:  # passwords stored on even-numbered lines
        val = line
        authorizedUsers[key] = val
    index += 1

# assess login attempt
while True:
    time.sleep(1)

    with open('credentialsCheckSrv.txt', 'r') as f:
        runStatus = f.read()

    if runStatus == 'run':
        with open('loginAttempt.txt', 'r') as f:
            loginAttempt = f.read().split()
        userName = loginAttempt[0]
        enteredPassword = loginAttempt[1]


        if userName in authorizedUsers:  # if username exists, check password
            correctPassword = authorizedUsers.get(userName)
            if enteredPassword == correctPassword:
                results = 'access granted'
            else:
                results = 'wrong password'
        else:  # username does not exist
            results = 'wrong username'

        with open('authorizationResults.txt', 'w') as f:
            f.write(results)
        with open('credentialsCheckSrv.txt', 'w') as f:  # opens and clears text file
            f.truncate(0)
        


