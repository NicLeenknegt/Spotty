
from data.api_caller import set_url,add_query_parameters

class SetupView:

    def __init__(self):
        self.check =  None

    @set_url("localhostt")
    @add_query_parameters()
    def get_client_config(self)-> dict:
        print("Welcome to Spotty!")
        print("To start the config you need a client id and a client secret.")
        print("You can find these on your app on the spotify dashboard.")
        print("If you do not already have a developer account you can make one by going to https://developer.spotify.com/dashboard/login .")
        print("Afterwards go to your dashboard and create an app.")
        print("You find your client id and client secret there.")
        client_id:str = input("CLIENT_ID:")
        client_secret:str = input("CLIENT_SECRET:")
        return { 'CLIENT_ID':client_id, 'CLIENT_SECRET':client_secret }
