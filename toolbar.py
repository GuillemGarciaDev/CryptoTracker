import rumps
import request as rq

class LaunchToolBar(rumps.App, ):
    def __init__(self):
        super(LaunchToolBar, self).__init__("CryptoBar")
        self.requestsModule = rq.requestModule()
        self.selectedToken = "bitcoin"
  
    @rumps.clicked("BTC - Bitcoin")
    def bitcoin(self, sender):
        self.selectedToken = "bitcoin"

    @rumps.clicked("ETH - Ethereum")
    def ethereum(self, sender):
        self.selectedToken = "ethereum"
    
    @rumps.clicked("ADA - Cardano")
    def bitcoin(self, sender):
        self.selectedToken = "cardano"
    
    @rumps.clicked("BNB - Binance Coin")
    def bitcoin(self, sender):
        self.selectedToken = "binancecoin"

    @rumps.clicked("SOL - Solana")
    def bitcoin(self, sender):
        self.selectedToken = "solana"

    @rumps.clicked("DOT - Polkadot")
    def bitcoin(self, sender):
        self.selectedToken = "polkadot"
    
    @rumps.clicked("LUNA - Terra")
    def bitcoin(self, sender):
        self.selectedToken = "terra-luna"

    @rumps.timer(2)
    def get_coin_price(self, _):
        
        print(self.selectedToken)
        self.requestsModule.requestToken(self.selectedToken)
        currentPrice = self.requestsModule.getTokenPrice()
        lastDayPercentage = self.requestsModule.get24hTokenPercentage()
        self.requestsModule.getTokenIconUrl()
        
        icon = "🟠"
        if lastDayPercentage > float(0):
            icon = "🟢"
        elif lastDayPercentage < float(0):
            icon = "🔴"

        self.icon = "./sources/" + self.selectedToken + ".png"
        self.title = self.requestsModule.getTokenTicker().upper() + " $" + str('{0:.2f}'.format(currentPrice)) + " " + icon + " " + str('{0:.2f}'.format(lastDayPercentage)) + "%"
        
