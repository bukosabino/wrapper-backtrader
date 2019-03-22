import backtrader as bt

from strategy import Strategy

class StrategyTemplate(Strategy):
    params = ()

    def __init__(self):
        super(StrategyTemplate, self).__init__()

    def next(self):
        if something:
            pass
            # self.buy()
        else:
            pass
            # self.sell()
