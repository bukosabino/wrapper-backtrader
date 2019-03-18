from datetime import datetime
import backtrader as bt

from utils import run_strategy, add_analyzers

# https://community.backtrader.com/topic/122/bband-strategy
# https://backtest-rookies.com/2018/02/23/backtrader-bollinger-mean-reversion-strategy

class SmaCross(bt.SignalStrategy):
    params = (('pfast', 10), ('pslow', 30),)

    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=self.p.pfast), bt.ind.SMA(period=self.p.pslow)
        self.signal_add(bt.SIGNAL_LONG, bt.ind.CrossOver(sma1, sma2))

cerebro = bt.Cerebro()

# Microsoft
data = bt.feeds.YahooFinanceData(dataname='MSFT', fromdate=datetime(2011, 1, 1),
                                 todate=datetime(2015, 12, 31))
cerebro.adddata(data)

cerebro.addstrategy(SmaCross)

# Analyzer
cerebro = add_analyzers(cerebro)

# Set our desired cash start
cerebro.broker.setcash(10000.0)

# Add a FixedSize sizer according to the stake
cerebro.addsizer(bt.sizers.FixedSize, stake=5)

# Set the commission
cerebro.broker.setcommission(commission=0.002)

# Run Strategy
strats = run_strategy(cerebro)

# Plot the result
# cerebro.plot()
