import backtrader as bt

from strategy import Strategy
from utils import run_strategy, add_analyzers
from settings import CONFIG
# Based on: https://community.backtrader.com/topic/122/bband-strategy


# Create a Strategy
class AberrationSideway(Strategy):
    """This strategy uses Backtrader's BBand indicator and buys after the
    market dips into the lower band and sells on the moving average after the
    market hits the top band. This works great in sideways/bull markets.
    The idea is to buy during a low period and sell if the market dips below
    a moving average. Also note I am new to algotrading and programming in
    general so don't laugh to hard at this idea/strategy.
    """
    params = (
        ('period', 20),
        ('devfactor', 2),
    )

    def __init__(self):

        self.redline = None
        self.blueline = None

        # Add a BBand indicator
        self.bband = bt.indicators.BBands(self.datas[0],
                                          period=self.p.period,
                                          devfactor=self.p.devfactor)

        super(AberrationSideway, self).__init__()

    def next(self):
        super(AberrationSideway, self).next()

        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return

        if self.dataclose < self.bband.lines.bot and not self.position:
            self.redline = True

        if self.dataclose > self.bband.lines.top and self.position:
            self.blueline = True

        if self.dataclose > self.bband.lines.mid and not self.position and self.redline:
            # BUY, BUY, BUY!!! (with all possible default parameters)
            self.log('BUY CREATE, %.2f' % self.dataclose[0])
            # Keep track of the created order to avoid a 2nd order
            self.order = self.buy()

        if self.dataclose > self.bband.lines.top and not self.position:
            # BUY, BUY, BUY!!! (with all possible default parameters)
            self.log('BUY CREATE, %.2f' % self.dataclose[0])
            # Keep track of the created order to avoid a 2nd order
            self.order = self.buy()

        if self.dataclose < self.bband.lines.mid and self.position and self.blueline:
            # SELL, SELL, SELL!!! (with all possible default parameters)
            self.log('SELL CREATE, %.2f' % self.dataclose[0])
            self.blueline = False
            self.redline = False
            # Keep track of the created order to avoid a 2nd order
            self.order = self.sell()

cerebro = bt.Cerebro()

# Microsoft data input
# Acciones de Microsoft como entrada de datos
data = bt.feeds.YahooFinanceData(dataname=CONFIG['asset'],
                                 fromdate=CONFIG['init_date'],
                                 todate=CONFIG['end_date'])
cerebro.adddata(data)

cerebro.addstrategy(AberrationSideway)

# Analyzer
cerebro = add_analyzers(cerebro)

# Set our desired cash start
cerebro.broker.setcash(CONFIG['capital_base'])

# Add a FixedSize sizer according to the stake
cerebro.addsizer(bt.sizers.FixedSize, stake=5)

# Set the commission
cerebro.broker.setcommission(commission=CONFIG['commission'])

# Run Strategy
strats = run_strategy(cerebro)

# Plot the result
cerebro.plot()
