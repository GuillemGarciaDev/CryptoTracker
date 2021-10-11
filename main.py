import rumps
import requests

class AwesomeStatusBarApp(rumps.App):
    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__("CryptoBar")

    @rumps.timer(2)
    def get_coin_price(self, _):
        headers = {
            'Content-Type':'application/json'
        }
        r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        self.title = "Bitcoin = " + str(r.json()['bitcoin']['usd']) + " $USD"
        self.icon = "./sources/bitcoin.png"
if __name__ == "__main__":
    AwesomeStatusBarApp().run()