import requests
import shutil
import os

class requestModule:

    def __init__(self):
        self.token = []

    def requestToken(self, token_name):

        headers = {
            'Content-Type':'application/json'
        }

        URL_REQUEST = "https://api.coingecko.com/api/v3/coins/" + token_name + "?tickers=true&market_data=true&developer_data=true"
        self.token = requests.get(URL_REQUEST)
        
        if self.token.status_code == 404:
            return "☠️ 404 - Token not Found"
    
    def getTokenPrice(self):

        return self.token.json()['market_data']['current_price']['usd']

    def getTokenTicker(self):

        return self.token.json()['symbol']

    def getTokenIconUrl(self):
        
        ### To Modify
        os.system("rm sources/" + self.token.json()['id'] + ".png")


        imageRequest = requests.get(self.token.json()['image']['thumb'], stream=True)
        imageName = self.token.json()['id'] + ".png"
        image = open(imageName, "xb")
        image.write(imageRequest.content)
        image.close()
        os.system("mv " + imageName + " sources/")


    def get24hTokenPercentage(self):

        return self.token.json()['market_data']['price_change_percentage_24h']