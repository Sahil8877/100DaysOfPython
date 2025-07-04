
class DataChecker():
    #data checker class to check user input and US states df
    def check_user_guess(self,user_guess,state_data):
        #func to check if the user input is in US states df
        self.data = state_data
        self.state_names = self.data["state"]
        if user_guess in list(self.state_names):
            #if the state is present in US states df return true, false otherwise
            print("state verified")
            return True
        else:
            return False