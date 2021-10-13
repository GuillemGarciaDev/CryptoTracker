import rumps
import request as rq


class LaunchToolBar(rumps.App):
    def __init__(self):
        super(LaunchToolBar, self).__init__("CryptoBar")
        self.selectedToken = "beta-finance"
        self.requestsModule = rq.requestModule()

    @rumps.timer(2)
    def get_coin_price(self, _):
        
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
        