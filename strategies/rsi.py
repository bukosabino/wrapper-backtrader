import backtrader as bt

from strategy import Strategy

class RSI(Strategy):

    params = (
        ('period', 21),
    )

    def __init__(self):
        self.rsi = bt.indicators.RSI_SMA(self.data.close,
                                         period=self.params.period)
        super(RSI, self).__init__()

    def next(self):
        if not self.position:
            if self.rsi < 30:
                self.buy()
        else:
            if self.rsi > 70:
                self.sell()

    def stop(self):
        from settings import CONFIG
        pnl = round(self.broker.getvalue() - CONFIG['capital_base'], 2)
        print('RSI Period: {} Final PnL: {}'.format(
            self.params.period, pnl))
