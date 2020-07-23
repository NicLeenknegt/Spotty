#!/usr/bin/python3

import sys,  getopt, urllib.parse, webbrowser, time, concurrent.futures, queue
from typing import Union, Callable
from data.api_caller import set_url,add_query_parameters
from views.MainView import MainView
from enum import Enum

def main(argv):
    try:
        opts,args = getopt.getopt(argv,"i",["init"])
    except:
        print ('spotty [--init|-i]')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i",  "--init"):
            #print(get_client_config())
            pipeline = queue.Queue(maxsize=1)
            view = MainView()
            view.start_loading_animation()
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
                executor.submit(run_thread, pipeline)
            message = pipeline.get()
            view.stop_loading_animation()
            sys.exit()

def run_view(view:MainView, queue:queue):
    message = queue.get()
    print(message)
    view.stop_loading_animation()

def run_thread(queue:queue):
    time.sleep(5)
    queue.put("nice") 

@set_url("localhostt")
@add_query_parameters()
def get_client_config()-> dict:
    print("Welcome to Spotty!")
    print("To start the config you need a client id and a client secret.")
    print("You can find these on your app on the spotify dashboard.")
    print("If you do not already have a developer account you can make one by going to https://developer.spotify.com/dashboard/login .")
    print("Afterwards go to your dashboard and create an app.")
    print("You find your client id and client secret there.")
    client_id:str = input("CLIENT_ID:")
    client_secret:str = input("CLIENT_SECRET:")
    return { 'CLIENT_ID':client_id, 'CLIENT_SECRET':client_secret }

if  __name__ ==  "__main__":
    main(sys.argv[1:])

