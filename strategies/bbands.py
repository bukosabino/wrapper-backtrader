import backtrader as bt

from strategy import Strategy
from utils import run_strategy, add_analyzers
from settings import CONFIG


class Aberration(Strategy):
    """Bollinger Bands Strategy
    """

    params = (
        ('period', 20),
        ('devfactor', 2),
    )

    def __init__(self):
        # Add a BBand indicator
        self.bband = bt.indicators.BBands(self.datas[0],
                                          period=self.p.period,
                                          devfactor=self.p.devfactor)
        super(Aberration, self).__init__()

    def next(self):
        super(Aberration, self).next()

        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return

        if self.dataclose < self.bband.lines.bot and not self.position:
            self.log('BUY CREATE, %.2f' % self.dataclose[0])
            self.order = self.buy()

        if self.dataclose > self.bband.lines.top and self.position:
            self.log('SELL CREATE, %.2f' % self.dataclose[0])
            self.order = self.sell()

cerebro = bt.Cerebro()

# Microsoft data input
# Acciones de Microsoft como entrada de datos
data = bt.feeds.YahooFinanceData(dataname=CONFIG['asset'],
                                 fromdate=CONFIG['init_date'],
                                 todate=CONFIG['end_date'])
cerebro.adddata(data)

cerebro.addstrategy(Aberration)

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
