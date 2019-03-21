import backtrader as bt

from utils import run_strategy, add_analyzers
from settings import CONFIG

cerebro = bt.Cerebro()

# Data input
data = bt.feeds.YahooFinanceData(dataname=CONFIG['asset'],
                                 fromdate=CONFIG['init_date'],
                                 todate=CONFIG['end_date'])
cerebro.adddata(data)

for strat in CONFIG['strategy']:
    cerebro.addstrategy(strat)

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
