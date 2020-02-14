import subprocess
import os
import requests
from bs4 import BeautifulSoup
from googler import Googler


class QueryProcessor:
    def __init__(self):
        self.confirm = ["yes", "yup", "alright", "sure", "go for it", "yeah", "confirm"]
        self.cancel = ["no", "nah", "negative", "cancel", "wait","nope"]

    def Processor(self, text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("You have not told your name is..") # dont use apostrophy here
            elif "your" in text:
                self.respond("My name is Jarvis.")
        else:
            f = Googler("https://www.google.co.uk/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)

    def respond(self, response):
        subprocess.call('say ' + response, shell=True)
