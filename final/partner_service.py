import time

class CredentialCheck():
    def __init__(self, username, password):
        self.name = username
        self.key = password

    def run_service(self):
        self.write_to_loginAttempt()
        self.write_credentialsCheckSrv()
        time.sleep(2)
        result = self.read_results()
        self.clear_files()

        return result
    

    def write_to_loginAttempt(self,):
        with open('loginAttempt.txt', 'w') as txt_file:
            txt_file.write(self.name)
            txt_file.write('\n')
            txt_file.write(self.key)

    def write_credentialsCheckSrv(self):
        with open('credentialsCheckSrv.txt', 'w') as txt_file:
            txt_file.write("run")


    def read_results(self):
        with open('authorizationResults.txt', 'r') as file:
            result = file.readline()
            return result
        
    def clear_files(self):
        with open('loginAttempt.txt', 'r+') as file:
            file.truncate(0)
    
        with open('credentialsCheckSrv.txt', 'r+') as file:
            file.truncate(0)

        with open('authorizationResults.txt', 'r+') as file:
            file.truncate(0)    